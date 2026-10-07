from __future__ import annotations
import argparse
import json
import os
from pathlib import Path
from mcp.server.fastmcp import FastMCP, Image
from mcp.server.transport_security import TransportSecuritySettings
from mcp.types import ToolAnnotations
from .store import Store

ROOT=Path(os.environ.get('COURSE_ROOT',Path(__file__).resolve().parents[1])).resolve()
INSTRUCTIONS=(ROOT/'teaching/system_prompt.md').read_text(encoding='utf-8')
HOST=os.environ.get('MCP_HOST','127.0.0.1')
allowed_hosts=[x.strip() for x in os.environ.get('MCP_ALLOWED_HOSTS','127.0.0.1:*,localhost:*').split(',') if x.strip()]
allowed_origins=[x.strip() for x in os.environ.get('MCP_ALLOWED_ORIGINS','http://127.0.0.1:*,http://localhost:*').split(',') if x.strip()]
mcp=FastMCP('DCOM_MCP',instructions=INSTRUCTIONS,host=HOST,port=int(os.environ.get('MCP_PORT','8000')),
    stateless_http=True,json_response=True,transport_security=TransportSecuritySettings(enable_dns_rebinding_protection=True,allowed_hosts=allowed_hosts,allowed_origins=allowed_origins))
store=Store(ROOT)
READ=ToolAnnotations(readOnlyHint=True,destructiveHint=False,idempotentHint=True,openWorldHint=False)

@mcp.tool(annotations=READ)
def get_course_metadata() -> dict:
    """Get scope, primary sources, release status, and retrieval limitations before teaching."""
    return dict(store.metadata,release=store.release,unavailable=store.rejected)

@mcp.tool(annotations=READ)
def list_chapters() -> list[dict]:
    """List verified chapters available for teaching. Omitted chapters are not ready."""
    out=[]
    for n,c in store.cards.items():
        store.assert_fresh(n);out.append({'chapter':n,'title':c['title'],'status':'ready'})
    return out

@mcp.tool(annotations=READ)
def get_data_card(chapter: int) -> dict:
    """Retrieve prerequisites, source provenance, topics, key terms, and quality metadata."""
    store.assert_fresh(chapter);return store.cards[chapter]

@mcp.tool(annotations=READ)
def get_chapter_outline(chapter: int) -> list[dict]:
    """List stable section IDs with parent/child relationships and asset IDs."""
    store.assert_fresh(chapter)
    return [{k:s[k] for k in ('id','title','parent','children','source','kind','asset_ids')} for s in store.rows if s['chapter']==chapter]

@mcp.tool(annotations=READ)
def search_course(query: str, chapter: int | None=None, limit: int=5) -> list[dict]:
    """Find source sections by course terms, acronyms, or phrases. Fetch full sections before explaining."""
    return store.search(query,chapter,limit)

@mcp.tool(annotations=READ)
def get_section(section_id: str) -> dict:
    """Get one complete source unit, including atomic examples, citations, children, and asset references."""
    return store.get_section(section_id)

@mcp.tool(annotations=READ)
def get_teaching_context(section_id: str) -> dict:
    """Bundle a section, relevant asset descriptions, and practice question IDs for focused teaching."""
    s=store.get_section(section_id)
    return {'section':s,'assets':[store.assets[a] for a in s['asset_ids']],
            'practice':store.list_questions(section_id=section_id,limit=10),
            'teaching_sequence':['purpose','mechanism','source figure','worked example','recall','section practice']}

@mcp.tool(annotations=READ)
def list_questions(chapter: int | None=None, section_id: str | None=None, include_descendants: bool=True, offset: int=0, limit: int=10) -> dict:
    """Select practice questions by exact section or chapter. Answers are not fabricated or revealed."""
    return store.list_questions(chapter,section_id,include_descendants,offset,limit)

@mcp.tool(annotations=READ)
def get_question(question_id: str) -> dict:
    """Get a complete book question by stable ID or printed label, with section and figure references."""
    return store.get_question(question_id)

@mcp.tool(annotations=READ)
def get_asset_metadata(asset_id: str) -> dict:
    """Inspect an asset's caption, labels, structure, source, and when it should be used."""
    return store.asset(asset_id)[0]

@mcp.tool(annotations=READ)
def get_asset(asset_id: str) -> list:
    """Return the original course image and its description as MCP content; no local viewer is required."""
    a,path=store.asset(asset_id)
    return [json.dumps(a,ensure_ascii=False),Image(path=str(path))]

@mcp.tool(annotations=READ)
def get_teaching_methodology() -> str:
    """Get the source-grounding, explanation, asset-use, and section-practice teaching contract."""
    return INSTRUCTIONS

@mcp.tool(annotations=READ)
def search(query: str) -> dict:
    """Search verified course sources; returns IDs for fetch, titles, and source URLs."""
    return {'results':[{'id':r['id'],'title':r['title'],'url':r['url']} for r in store.search(query)]}

@mcp.tool(annotations=READ)
def fetch(id: str) -> dict:
    """Fetch a complete source unit returned by search."""
    s=store.get_section(id)
    return {'id':s['id'],'title':s['title'],'text':s['text'],'url':s['url'],'metadata':{k:s[k] for k in ('chapter','source','children','asset_ids','content_sha256')}}

@mcp.resource('course://metadata')
def metadata_resource() -> str:
    return json.dumps(get_course_metadata(),ensure_ascii=False)

@mcp.resource('course://teaching')
def teaching_resource() -> str:
    return INSTRUCTIONS

@mcp.prompt()
def teach_section(section_id: str) -> str:
    """Start a grounded lesson with a verified section and its linked practice."""
    store.get_section(section_id)
    return INSTRUCTIONS+'\n\nTeach '+section_id+' using get_teaching_context. Fetch each needed child unit and source image. End with one linked question and wait for the learner.'

def main():
    parser=argparse.ArgumentParser();parser.add_argument('--http',action='store_true');args=parser.parse_args()
    mcp.run(transport='streamable-http' if args.http else 'stdio')

if __name__=='__main__':main()

