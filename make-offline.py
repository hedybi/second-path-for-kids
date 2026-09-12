from pathlib import Path
import re

root = Path(__file__).parent
public = root / 'dist'
html = (root / 'templates/studio.html').read_text()
css = (public / 'studio.css').read_text()
modules = ['data/activities.js', 'data/cases-en.js', 'data/cases-extra.js', 'data/learning-map-data.js', 'content.js', 'reports.js', 'learning-map.js', 'studio.js']
parts = []
for name in modules:
    code = (public / name).read_text()
    code = re.sub(r'^import .*?;\s*$', '', code, flags=re.M)
    code = re.sub(r'\bexport (?=(?:const|function|class)\b)', '', code)
    parts.append(code)
script = '\n'.join(parts).replace('</script', '<\\/script')
html = html.replace('<link rel="stylesheet" href="/studio.css">', '<style>' + css + '</style>')
html = html.replace('<script type="module" src="/studio.js"></script>', '<script type="module">\n' + script + '\n</script>')
original = (public / 'data/learning-map-source.json').read_text().replace('</', '<\\/')
before, after = html.rsplit('</body>', 1)
html = before + '<script type="application/json" id="learningMapOriginal">' + original + '</script></body>' + after
assert '<script type="module" src=' not in html
assert '<link rel="stylesheet"' not in html
assert not re.search(r'^import ', script, re.M)
for out in [root / 'index.html', root / 'deliverables/一起长大.html', public / 'index.html', public / 'studio.html']:
    out.write_text(html)
    print(f'Standalone entry: {out.relative_to(root)} · {out.stat().st_size} bytes')
