"""Fail-closed release validation; no server startup or network required."""
from __future__ import annotations
import argparse, json, re, sys
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from dcom_mcp.store import read_md, parse_sections, parse_questions, digest, safe_path

def validate_chapter(directory: Path) -> dict:
    errors=[]
    try:
        c,cb=read_md(directory/'content.md');q,qb=read_md(directory/'questions.md');card,_=read_md(directory/'data_card.md')
        manifest=json.loads((directory/'assets/manifest.json').read_text(encoding='utf-8'))
        n=c['chapter'];sections=parse_sections(cb,n);questions=parse_questions(qb,n)
        ids={s['id'] for s in sections};assets={a['id']:a for a in manifest['assets']}
        external={r['id'] for r in card.get('external_section_refs',[])}
        external_assets=set(card.get('external_asset_refs',[]))
        if len(assets)!=len(manifest['assets']):errors.append('Duplicate asset IDs')
        if len({q['id'] for q in questions})!=len(questions):errors.append('Duplicate question IDs')
        if card.get('open_issues'):errors.append('Unresolved data card issues')
        if c.get('status')!='complete' or q.get('status')!='complete':errors.append('Extraction is not complete')
        review=card.get('review',{})
        if not review.get('source_order_checked') or not review.get('reviewed_at'):errors.append('Source review receipt missing')
        if review.get('figures')!=sum(a['type']=='illustration' for a in assets.values()):errors.append('Figure review count differs')
        if review.get('questions')!=len(questions):errors.append('Question review count differs')
        if card.get('content_stats',{}).get('words')!=len(cb.split()):errors.append('Stale word count')
        if card.get('question_stats',{}).get('total')!=len(questions):errors.append('Stale question count')
        for s in sections:
            if not s['source']:errors.append(f'{s["id"]}: missing source')
            for aid in s['asset_ids']:
                if aid not in assets:errors.append(f'{s["id"]}: unknown asset {aid}')
        definitions=re.findall(r'\[ASSET ([\w-]+)\]',cb+'\n'+qb)
        for aid,a in assets.items():
            if definitions.count(aid)!=1:errors.append(f'{aid}: expected one definition')
            if a.get('needs_review') or a.get('review',{}).get('visual_semantics')!='reviewed':errors.append(f'{aid}: review incomplete')
            if a.get('section_id') not in ids and a.get('section_id') not in {q['id'] for q in questions}:errors.append(f'{aid}: invalid section')
            for key in ('description','structure','use_when','sources','text_in_image'):
                if not a.get(key):errors.append(f'{aid}: missing {key}')
            if re.search(r'No reliable|labels are present|see the attached image|Refer to the attached image',a.get('structure',''),re.I):errors.append(f'{aid}: placeholder structure')
            path=safe_path(directory,'assets/'+a['file'])
            if digest(path)!=a['sha256']:errors.append(f'{aid}: stale image hash')
            try:
                from PIL import Image
                with Image.open(path) as im:
                    if im.size!=(a['width'],a['height']):errors.append(f'{aid}: wrong dimensions')
                    im.verify()
            except ImportError:errors.append('Pillow required for release validation')
        for question in questions:
            label=question['label'];refs=set(question['ref_sections'])
            if not refs or not refs.issubset(ids|external):errors.append(f'{label}: invalid section mapping')
            aids=set(question['asset_ids'])
            if question['has_figure']!=bool(aids) or not aids.issubset(set(assets)|external_assets):errors.append(f'{label}: invalid figure metadata')
            rendered=set(re.findall(r'\[ASSET(?:_REF)? ([\w-]+)\]',question['text']))
            if aids!=rendered:errors.append(f'{label}: asset references differ')
            if len(question['text'].split())<3:errors.append(f'{label}: empty question')
        for name in ('content.md','questions.md','data_card.md'):
            raw=(directory/name).read_bytes()
            if b'\r' in raw or raw.startswith(b'\xef\xbb\xbf'):errors.append(f'{name}: encoding is not UTF-8/LF')
            if '\ufffd' in raw.decode('utf-8'):errors.append(f'{name}: replacement characters')
    except (OSError,ValueError,KeyError,TypeError) as e:errors.append(str(e))
    return {'chapter':directory.name,'ready':not errors,'errors':errors,'error_count':len(errors)}

def main():
    p=argparse.ArgumentParser();p.add_argument('directory',type=Path,nargs='?');args=p.parse_args()
    root=Path(__file__).resolve().parents[1]
    targets=[args.directory] if args.directory else sorted((root/'Data_Communications').glob('Chapter_*'))
    results=[validate_chapter(d) for d in targets]
    release=json.loads((root/'course/release.json').read_text(encoding='utf-8'))
    if args.directory is None:
        from dcom_mcp.store import Store
        store=Store(root)
        for n,msg in store.rejected.items():results.append({'chapter':n,'ready':False,'error_count':1,'errors':[msg]})
        served=set(store.cards)
        if served!={int(r['chapter']) for r in release['chapters'] if r.get('status')=='ready'}:results.append({'chapter':'release','ready':False,'errors':['Release set mismatch']})
    print(json.dumps(results,ensure_ascii=False,indent=2))
    return 0 if all(r['ready'] for r in results) else 1

if __name__=='__main__':raise SystemExit(main())
