"""Export a compact semantic routing index from the pinned release."""
import json,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT))
from dcom_mcp.store import Store,tokens
store=Store(ROOT)
if store.rejected:raise SystemExit(str(store.rejected))
index={'schema_version':1,'method':store.metadata['retrieval'],'aliases':store.aliases,
       'chapters':[{'chapter':n,'title':c['title'],'key_terms':c['key_terms'],'prerequisites':c['prerequisites']} for n,c in store.cards.items()],
       'sections':[{k:s[k] for k in ('id','chapter','title','parent','children','source','kind','asset_ids')} | {'terms':sorted(set(tokens(s['title']))),'question_ids':[q['id'] for q in store.questions.values() if s['id'] in q['ref_sections']]} for s in store.rows]}
(ROOT/'course/semantic_index.json').write_bytes((json.dumps(index,ensure_ascii=False,indent=2)+'\n').encode('utf-8'))
print(f'Indexed {len(store.cards)} chapters, {len(store.rows)} sections, {len(store.assets)} assets, {len(store.questions)} questions.')
