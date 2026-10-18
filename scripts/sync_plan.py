#!/usr/bin/env python3
"""Exact-key diff for connected-tool sync. Emits operations; never sends credentials or writes canon."""
import argparse,json
from pathlib import Path
p=argparse.ArgumentParser();p.add_argument('desired');p.add_argument('readback');p.add_argument('--registry',default='integrations/registry.json');a=p.parse_args()
desired=json.loads(Path(a.desired).read_text());current=json.loads(Path(a.readback).read_text());reg=json.loads(Path(a.registry).read_text())
operations=[];errors=[]
for table in reg['airtable']['tables']:
 rows=current.get(table['name'],[]);primary=table['primary_field'];bykey={}
 for rec in rows:
  key=rec['cellValuesByFieldId'].get(primary)
  if key in bykey:errors.append('Duplicate key '+table['name']+': '+str(key))
  bykey[key]=rec
 fields={f['name']:f['id'] for f in table['fields']}
 for row in desired[table['name']]:
  mapped={fields[k]:v for k,v in row.items()};prev=bykey.get(mapped[primary])
  if prev:
   changes={k:v for k,v in mapped.items() if prev['cellValuesByFieldId'].get(k)!=v}
   if changes:operations.append({'operation':'update','table':table['id'],'id':prev['id'],'fields':changes})
  else:operations.append({'operation':'create','table':table['id'],'fields':mapped})
print(json.dumps({'errors':errors,'operation_count':len(operations),'operations':operations,'direction':'source_to_reference_only'},ensure_ascii=False,indent=2))
raise SystemExit(bool(errors))
