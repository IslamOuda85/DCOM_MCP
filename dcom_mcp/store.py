from __future__ import annotations
import hashlib
import json
import re
from pathlib import Path
from typing import Any
import yaml
from rank_bm25 import BM25Okapi

FRONT = re.compile(r'\A---\n(.*?)\n---\n', re.S)
STOP = set('a an and are as at be by for from how in is it of on or that the this to was what when which with'.split())

def read_md(path: Path) -> tuple[dict, str]:
    text = path.read_text(encoding='utf-8-sig')
    m = FRONT.match(text)
    if not m:
        raise ValueError(f'Missing YAML front matter: {path.name}')
    return yaml.safe_load(m[1]) or {}, text[m.end():]

def tokens(text: str) -> list[str]:
    return [t for t in re.findall(r'[\w]+', text.lower(), re.UNICODE) if t not in STOP]

def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()

def safe_path(root: Path, relative: str) -> Path:
    path = (root / relative).resolve()
    if not path.is_relative_to(root.resolve()):
        raise ValueError('Path escapes the course root')
    return path

def fields(line: str) -> dict[str, str]:
    return dict((k.strip(), v.strip()) for part in line.removeprefix('>').split('|') if ':' in part for k,v in [part.split(':',1)])

def list_field(value: str) -> list[str]:
    return [v.strip() for v in value.strip('[] ').split(',') if v.strip()]

def parse_sections(body: str, chapter: int) -> list[dict]:
    """Preserve source hierarchy; examples and solutions stay within the same unit."""
    headings = list(re.finditer(r'(?m)^(#{2,6}) (.+)$', body))
    result = []; stack = []; ids = set()
    for i,h in enumerate(headings):
        level, title = len(h[1]), h[2]
        end = headings[i+1].start() if i+1 < len(headings) else len(body)
        text = body[h.end():end].strip()
        meta = fields(text.splitlines()[0]) if text.startswith('> id:') else {}
        while stack and stack[-1]['level'] >= level: stack.pop()
        parent = stack[-1]['id'] if stack else None
        slug = re.sub(r'[^a-z0-9]+','-',title.lower()).strip('-')
        sid = meta.get('id') or f'{parent or f"ch{chapter:02d}"}-{slug}'
        if sid in ids: raise ValueError(f'Duplicate section ID: {sid}')
        ids.add(sid)
        item = {'id':sid,'chapter':chapter,'title':title,'level':level,'parent':parent,
                'source':meta.get('src') or (stack[-1]['source'] if stack else ''),
                'kind':meta.get('kind','concept'),'text':text,
                'asset_ids':list(dict.fromkeys(re.findall(r'\[ASSET(?:_REF)? ([\w-]+)\]',text))),
                'children':[]}
        if stack: stack[-1]['children'].append(sid)
        result.append(item);stack.append(item)
    return result

def parse_questions(body: str, chapter: int) -> list[dict]:
    out=[]
    for part in re.split(r'(?=^### )',body,flags=re.M):
        m=re.match(r'### (\S+)\s*\n> ([^\n]+)\n',part)
        if not m:continue
        meta=fields(m[2])
        out.append({'id':meta['id'],'label':m[1],'chapter':chapter,'type':meta.get('type'),
                    'ref_sections':list_field(meta.get('ref_sections','')),
                    'has_figure':meta.get('has_figure')=='true',
                    'asset_ids':list_field(meta.get('figure_assets','')),
                    'source':meta.get('src',''),'text':part[m.end():].strip(),'answer':None})
    return out

class Store:
    def __init__(self, root: Path):
        self.root=root.resolve()
        self.metadata=json.loads((self.root/'course/metadata.json').read_text(encoding='utf-8'))
        self.release=json.loads((self.root/'course/release.json').read_text(encoding='utf-8'))
        self.cards={};self.sections={};self.assets={};self.questions={};self.rejected={}
        self.fingerprints={}
        for entry in self.release['chapters']:
            n=int(entry['chapter'])
            if entry.get('status')!='ready':continue
            directory=safe_path(self.root,f'Data_Communications/Chapter_{n:02d}')
            try:
                expected=entry.get('files',{})
                required={'content.md','questions.md','data_card.md','assets/manifest.json'}
                if not required.issubset(expected):raise ValueError('Incomplete release fingerprints')
                for name,sha in expected.items():
                    if digest(safe_path(directory,name))!=sha:raise ValueError(f'Fingerprint mismatch: {name}')
                card,_=read_md(directory/'data_card.md')
                _,content=read_md(directory/'content.md');_,question_text=read_md(directory/'questions.md')
                manifest=json.loads((directory/'assets/manifest.json').read_text(encoding='utf-8'))
                parsed_sections=parse_sections(content,n);parsed_questions=parse_questions(question_text,n)
                section_ids={s['id'] for s in parsed_sections}
                parsed_assets={a['id']:dict(a,chapter=n) for a in manifest['assets']}
                external_ids={r['id'] for r in card.get('external_section_refs',[])}
                external_asset_ids=set(card.get('external_asset_refs',[]))
                if card.get('open_issues'):raise ValueError('Data card contains unresolved issues')
                for a in parsed_assets.values():
                    if a.get('needs_review'):raise ValueError(f'Unreviewed asset: {a["id"]}')
                    name='assets/'+a['file']
                    if name not in expected:raise ValueError(f'Unpinned asset: {a["id"]}')
                    safe_path(directory,name)
                for q in parsed_questions:
                    if not q['ref_sections'] or not set(q['ref_sections']).issubset(section_ids | external_ids):raise ValueError(f'Invalid question references: {q["id"]}')
                    if bool(q['asset_ids'])!=q['has_figure'] or not set(q['asset_ids']).issubset(set(parsed_assets)|external_asset_ids):raise ValueError(f'Invalid question figures: {q["id"]}')
                    if not (set(q['asset_ids'])-set(parsed_assets)).issubset(self.assets):raise ValueError(f'Unavailable external question figure: {q["id"]}')
                for s in parsed_sections:
                    if not set(s['asset_ids']).issubset(parsed_assets):raise ValueError(f'Unknown section asset: {s["id"]}')
                self.cards[n]=card;self.sections.update({s['id']:s for s in parsed_sections})
                self.questions.update({q['id']:q for q in parsed_questions});self.assets.update(parsed_assets)
                self.fingerprints[n]=(directory,expected)
            except (ValueError,KeyError,OSError) as e:self.rejected[n]=str(e)
        self.rows=list(self.sections.values())
        self.index=BM25Okapi([tokens(s['title']+' '+s['title']+' '+s['text']) for s in self.rows]) if self.rows else None
        self.aliases=self.metadata.get('aliases',{})

    def assert_fresh(self, chapter: int):
        if chapter not in self.cards:raise ValueError('Chapter is not in the verified release')
        directory,expected=self.fingerprints[chapter]
        # In-memory text and on-disk images must belong to the same pinned release.
        for name,sha in expected.items():
            if digest(safe_path(directory,name))!=sha:raise ValueError('Course files changed after startup; rebuild the release and restart')

    def source_url(self, chapter: int, filename='content.md') -> str:
        return f'{self.metadata["repository"]}/blob/{self.release.get("ref","main")}/Data_Communications/Chapter_{chapter:02d}/{filename}'

    def search(self, query: str, chapter: int | None=None, limit: int=5) -> list[dict]:
        if not query.strip() or not self.index:return []
        if len(query)>1000:raise ValueError('Use a query of at most 1000 characters')
        expanded=query
        for key,values in self.aliases.items():
            if re.search(r'(?<!\w)'+re.escape(key)+r'(?!\w)',query,re.I):expanded+=' '+' '.join(values)
        scores=self.index.get_scores(tokens(expanded));qt=set(tokens(expanded))
        ranked=[]
        for s,score in zip(self.rows,scores):
            if chapter is not None and s['chapter']!=chapter:continue
            if not qt.intersection(tokens(s['text']+' '+s['title'])):continue
            score=float(score)+2*len(qt.intersection(tokens(s['title'])))
            ranked.append((score,s))
        result=[]
        for score,s in sorted(ranked,key=lambda x:(-x[0],x[1]['id']))[:max(1,min(limit,20))]:
            self.assert_fresh(s['chapter'])
            result.append({k:s[k] for k in ('id','chapter','title','source','parent','asset_ids')} | {'score':round(score,4),'preview':s['text'][:900],'url':self.source_url(s['chapter'])})
        return result

    def get_section(self, sid: str) -> dict:
        if sid not in self.sections:raise ValueError('Unknown or unreleased section')
        s=self.sections[sid];self.assert_fresh(s['chapter'])
        return dict(s,url=self.source_url(s['chapter']),content_sha256=self.fingerprints[s['chapter']][1]['content.md'])

    def descendants(self,sid):
        if sid not in self.sections:raise ValueError('Unknown section')
        out={sid}
        for child in self.sections[sid]['children']:out.update(self.descendants(child))
        return out

    def list_questions(self, chapter=None, section_id=None, include_descendants=True, offset=0, limit=10):
        allowed=self.descendants(section_id) if section_id and include_descendants else {section_id} if section_id else None
        if section_id:self.assert_fresh(self.sections[section_id]['chapter'])
        rows=[q for q in self.questions.values() if (chapter is None or q['chapter']==chapter) and (allowed is None or allowed.intersection(q['ref_sections']))]
        for n in {q['chapter'] for q in rows}:self.assert_fresh(n)
        return {'total':len(rows),'offset':max(0,offset),'questions':[{k:q[k] for k in ('id','label','chapter','type','ref_sections','has_figure','asset_ids')} for q in rows[max(0,offset):max(0,offset)+max(1,min(limit,50))]]}

    def get_question(self,qid):
        if qid not in self.questions:
            matches=[q for q in self.questions.values() if q['label'].lower()==qid.lower()]
            if len(matches)!=1:raise ValueError('Unknown or ambiguous question')
            q=matches[0]
        else:q=self.questions[qid]
        self.assert_fresh(q['chapter'])
        return dict(q,url=self.source_url(q['chapter'],'questions.md'),unavailable_sections=[s for s in q['ref_sections'] if s not in self.sections])

    def asset(self,aid):
        if aid not in self.assets:raise ValueError('Unknown or unreleased asset')
        a=self.assets[aid];self.assert_fresh(a['chapter'])
        path=safe_path(self.fingerprints[a['chapter']][0],'assets/'+a['file'])
        return a,path

