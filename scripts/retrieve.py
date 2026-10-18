#!/usr/bin/env python3
"""Retrieve one whole exact owner; --closure returns every complete route target."""
import argparse, json, sys
from source_store import SourceStore
p=argparse.ArgumentParser();p.add_argument('owner');p.add_argument('--root',default='.');p.add_argument('--closure',action='store_true');a=p.parse_args()
s=SourceStore(a.root)
names=[a.owner]
if a.closure:
    entries=json.loads(s.read('complete_sources/ACCESS_INDEX.json'))['entries']
    entry=next((e for e in entries if a.owner in [e['label'],e['owner'],e['path']]),None)
    if not entry:raise SystemExit('No complete route for this exact label/owner')
    names=entry['full_owner_routes']
for name in dict.fromkeys(names):
    raw=s.read(name)
    sys.stderr.write(json.dumps({'owner':name,'sha256':s.manifest['logical_modules'][name]['sha256'],'role':s.manifest['logical_modules'][name]['role']})+'\n')
    sys.stdout.buffer.write(raw)
    if len(names)>1:sys.stdout.buffer.write(b'\n')
