from pathlib import Path
import json, importlib.util, argparse, shutil, tempfile
from content import MODULES

HERE=Path(__file__).resolve().parent
parser=argparse.ArgumentParser()
parser.add_argument('--renderer',required=True,help='Path to visualize/scripts/render.py')
parser.add_argument('--out',default='.',help='Output folder (default: current directory)')
parser.add_argument('--inline-dir',default=None)
args=parser.parse_args()
out=Path(args.out).resolve();out.mkdir(parents=True,exist_ok=True)
inline=Path(args.inline_dir or out).resolve();inline.mkdir(parents=True,exist_ok=True)
ids={'simple-tenses':'mt_Of-WsrRQ8B','standard-verb-forms':'mt_ay0qkGj0jg'}
for m in MODULES:
    if m['id'] in ids:m['node']=ids[m['id']]
    for bank in ['questions','transfer']:
        for i,q in enumerate(m[bank]):
            q['id']=f"{m['id']}-{bank}-{i+1}"
            assert q['options'].count(q['answer'])==1
            assert len(q['options'])==len(set(q['options']))
    assert {q['tag'] for q in m['questions']} <= {q['tag'] for q in m['transfer']}
    assert len(m['questions'])==12
blob=json.dumps(MODULES,ensure_ascii=False,separators=(',',':')).replace('</','<\\/')
fragment=(HERE/'template.html').read_text().replace('__LESSONS_JSON__',blob).replace('__ENGINE_JS__',(HERE/'engine.js').read_text())
assert len(fragment.encode())<1000000
(out/'grammar-adventures.html').write_text(fragment)
(inline/'grammar-adventures.html').write_text(fragment)
(out/'lessons.json').write_text(json.dumps(MODULES,ensure_ascii=False,indent=2)+'\n')
spec=importlib.util.spec_from_file_location('viz_renderer',Path(args.renderer));r=importlib.util.module_from_spec(spec);spec.loader.exec_module(r)
r.export_html(out/'grammar-adventures.html',out/'game.html',title='Second Path · Grammar Adventures',force=True)
for index,m in enumerate(MODULES):
    start="let state=E.clean(window.openai?.widgetState?.privateContent,data);"
    direct=fragment.replace(start,start+f"\n  if(state.module!=={index}){{state.module={index};state.mode='learn';state.lesson=0;state.variant=0;}}")
    with tempfile.TemporaryDirectory() as temp:
        source=Path(temp)/'lesson.html';source.write_text(direct)
        r.export_html(source,out/(m['id']+'.html'),title='Second Path · '+m['en'],force=True)
for name in ['content.py','engine.js','template.html','build.py','verify.cjs']:
    if (HERE/name).exists() and (HERE/name).resolve()!=(out/name).resolve():shutil.copy2(HERE/name,out/name)
for m in MODULES:
    rows=['# '+m['en'],'',f"Reference ages: **{m['age']}** · Map node: `{m['node']}`.",'',f"[Play this module](https://hedybi.github.io/second-path-for-kids/skills/grammar-adventures/{m['id']}.html). This address opens **{m['name']}** directly. You can also download `{m['id']}.html` and open it in a browser.",'','## Teaching focus','',m['boundary'],'','## Interactive lessons','']
    for l in m['lessons']:
        rows.extend(['### '+l['title'],'',l['clue'],''])
        for v in l['variants']:rows.extend([f"- **{v['sentence']}** — {v['zh']} {v['rule']}"])
        rows.append('')
    rows.extend(['## Practice','',f"12 core questions and {len(m['transfer'])} transfer questions. Hints and retries are recorded separately from first-attempt independent answers. Use `lessons.json` for the complete question bank."])
    (out/(m['id']+'.md')).write_text('\n'.join(rows)+'\n')
print(json.dumps({'modules':len(MODULES),'lessons':sum(len(m['lessons']) for m in MODULES),'coreQuestions':sum(len(m['questions']) for m in MODULES),'transferQuestions':sum(len(m['transfer']) for m in MODULES),'inline':str(inline/'grammar-adventures.html'),'output':str(out)},ensure_ascii=False))
