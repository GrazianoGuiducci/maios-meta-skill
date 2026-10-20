"""Assemble language-aware resource entries and render the English primary README."""
import json
from pathlib import Path
from render_readmes import render

ROOT=Path(__file__).resolve().parents[1]

def main():
    path=ROOT/'catalog.json'
    catalog=json.loads(path.read_text(encoding='utf-8'))
    resources={r['id']:r for r in catalog['resources']}
    for entry in sorted((ROOT/'skills').glob('*/catalog-entry.json')):
        item=json.loads(entry.read_text(encoding='utf-8'))
        assert item['id']==entry.parent.name
        resources[item['id']]=item
    ordered=sorted(resources.values(),key=lambda x:x['review_id'])
    assert {x['review_id'] for x in ordered}=={f'{x:02}' for x in range(25)}
    assert all(x['instruction_language']=='en' and set(x['languages'])=={'en','it'} for x in ordered)
    catalog.update(primary_language='en',available_languages=['en','it'],resources=ordered)
    path.write_text(json.dumps(catalog,ensure_ascii=False,indent=2)+'\n',encoding='utf-8',newline='\n')
    render(ROOT,ordered)
    print(json.dumps({'resources':len(ordered),'primary_language':'en'}))

if __name__=='__main__':main()
