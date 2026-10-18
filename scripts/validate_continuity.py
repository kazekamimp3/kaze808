"""Validate operational evidence without granting acceptance or changing originals."""
import hashlib,json,sys
from pathlib import Path
root=Path(sys.argv[1] if len(sys.argv)>1 else '.').resolve()
ledger=json.loads((root/'continuity/DELIVERY_LEDGER.json').read_text())
def checked(path,expected):
 p=(root/path).resolve()
 assert p.is_relative_to(root),path
 assert hashlib.sha256(p.read_bytes()).hexdigest()==expected,path
 return p
previous=None
for e in ledger['episodes']:
 assert e['branch_id']==ledger['branch_id']
 checked(e['manuscript'],e['manuscript_sha256'])
 cp=json.loads(checked(e['checkpoint'],e['checkpoint_sha256']).read_text())
 assert cp['branch_id']==e['branch_id'] and cp['episode']==e['episode']
 assert cp['delivery_evidence']['sha256']==e['manuscript_sha256']
 assert e['author_acceptance']=='NOT_ASSERTED'
 if previous: assert e['predecessor_sha256']==previous
 previous=e['manuscript_sha256']
for o in ledger['author_overrides']:checked(o['path'],o['sha256'])
current=json.loads((root/'continuity/CURRENT.json').read_text())
assert current['branch_id']==ledger['branch_id']
assert current['KAZE_ROMANCE_ENABLED'] is False and current['Briar_stays'] is True
assert ledger['current_delivered_episode']==max(e['episode'] for e in ledger['episodes'] if e['delivery_status']=='DELIVERED_PROVISIONAL')
print(json.dumps({'result':'PASS','episode_pairs':len(ledger['episodes']),'last_delivered':ledger['current_delivered_episode'],'next':ledger['next_episode'],'acceptance_inferred':False}))
