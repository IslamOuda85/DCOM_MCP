from pathlib import Path
import json,shutil
import pytest
from dcom_mcp.store import Store,parse_sections,safe_path

ROOT=Path(__file__).resolve().parents[1]

def test_release_loads():
    s=Store(ROOT)
    assert not s.rejected
    assert 1 in s.cards
    assert len(s.questions)>=29

def test_section_practice_and_images():
    s=Store(ROOT)
    q=s.get_question('P1-6')
    assert q['has_figure'] and q['asset_ids']==['ch01_ill_007']
    assert q['ref_sections']==['ch01-1-2-2-ring-topology']
    assert any(q['label']=='P1-6' for q in s.list_questions(section_id='ch01-1-2-2')['questions'])
    a,p=s.asset('ch01_ill_007')
    assert p.exists() and a['type']=='illustration'

def test_search_and_hierarchy():
    s=Store(ROOT)
    results=s.search('mesh topology',chapter=1)
    assert results and results[0]['chapter']==1
    assert any('mesh-topology' in r['id'] for r in results)
    assert s.get_section('ch01-1-2-2-mesh-topology')['parent']=='ch01-1-2-2'
    assert s.search('zzqqxyunknown')==[]

def test_unreleased_chapter_rejected():
    s=Store(ROOT)
    with pytest.raises(ValueError):s.get_section('ch99-1')

def test_path_escape():
    with pytest.raises(ValueError):safe_path(ROOT,'../outside')

def test_changed_data_fails_closed(tmp_path):
    for name in ('course','Data_Communications'):shutil.copytree(ROOT/name,tmp_path/name)
    p=tmp_path/'Data_Communications/Chapter_01/content.md'
    p.write_text(p.read_text(encoding='utf-8')+'tampered',encoding='utf-8')
    s=Store(tmp_path)
    assert 1 in s.rejected and 1 not in s.cards

def test_changed_after_load_is_rejected(tmp_path):
    for name in ('course','Data_Communications'):shutil.copytree(ROOT/name,tmp_path/name)
    s=Store(tmp_path)
    p=tmp_path/'Data_Communications/Chapter_01/questions.md'
    p.write_text('changed',encoding='utf-8')
    with pytest.raises(ValueError):s.get_question('P1-6')

def test_examples_are_atomic():
    body='## Topic\n> id: ch01-test | src: book p.1 | kind: concept\n\n**Example 1.1**\nProblem\n\n**Solution**\nSteps\n'
    result=parse_sections(body,1)
    assert len(result)==1 and '**Solution**' in result[0]['text']

def test_cross_chapter_source_note():
    s=Store(ROOT);q=s.get_question('Q1-16')
    assert q['ref_sections']==['ch02-2-1-2']
    assert 'Source note' in q['text']

