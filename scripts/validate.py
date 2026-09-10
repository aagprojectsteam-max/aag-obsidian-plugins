from pathlib import Path
import json,re
root=Path(__file__).resolve().parents[1];data=json.loads((root/'catalog.json').read_text());plugins=data['plugins'];assert len(plugins)==3
assert len({p['id'] for p in plugins})==len(plugins)
for p in plugins:
 assert re.fullmatch(r'aagprojectsteam-max/aag-obsidian-(designtweaker|smartpaste|sidenotes)',p['repository'])
 assert re.fullmatch(r'\d+\.\d+\.\d+',p['version'])
 assert p['minAppVersion']=='1.13.7'
 assert 'https://github.com/'+p['repository']+'/releases/tag/'+p['version'] in (root/'README.md').read_text()
print('CATALOG=PASS; ENTRIES=3')
