#!/usr/bin/env python3
"""Export deterministic non-canon read models; never writes source owners."""
import hashlib,json,sys
from pathlib import Path
from source_store import SourceStore

def project(root):
 s=SourceStore(root);m=s.manifest
 read=lambda n:json.loads(s.read(n))
 state=read('state/Post_Chris_Restart.json');cur=state['current_reconciliation_20261018'];branch=state['branch_id']
 access=read('complete_sources/ACCESS_INDEX.json')['entries']
 out={k:[] for k in ['Characters','Episodes','Abilities and Equipment','Consequences','Author Decisions','Research Evidence','Source Owners']}
 char=[]
 for e in access:
  if e['category']!='characters' or ' Source' in e['label']:continue
  label=e['label'];status='Source catalog only; current life, membership and location require scoped state owner'
  note='Complete source routes: '+json.dumps(e['full_owner_routes'],ensure_ascii=False)
  if label in cur['current_positions']:
   note+='\nLast confirmed position: '+cur['current_positions'][label]
   status='Last confirmed E20 / current scoped author configuration; acceptance separate'
  if label=='Briar':status='Independent; first meeting pending; no prior shared history'
  if label=='Kaze':status='E20 inside BELLY in Zaun; Noxus solo planned, not traveled'
  char.append({'Character':label,'Continuity Status':status,'Current Branch':branch,'Authority Source':e['owner'],'Evidence Level':'Derived exact-owner route; no new life-status/event adjudication','Notes':note})
 for label in ['Zid','Rick','Morty','Baldur','Kratos']:
  owner='state/Post_Chris_Restart.json' if label=='Zid' else 'research/GOW_Baldur_Kratos_Fidelity_20261018.md' if label in ['Baldur','Kratos'] else 'ACTIVE_AUTHOR_UPDATE_20261017_BRIAR_KAZE_RICK_MORTY.txt'
  status='Continuing Sin; preserve retained reinstatement' if label=='Zid' else 'Selected prospective; no arrival/encounter/outcome awarded' if label in ['Baldur','Kratos'] else 'Independent nonmember; location not inferred'
  char.append({'Character':label,'Continuity Status':status,'Current Branch':branch,'Authority Source':owner,'Evidence Level':'Author configuration / full owner required','Notes':'Do not import historical placements, grants or superseded membership.'})
 out['Characters']=char
 for n,title in [(19,'Narrow Mercy'),(20,'The Express Service')]:
  owner=f'state/episodes/Season_3_Episode_{n}_Checkpoint_Current.json';raw=s.read(f'state/evidence/S3_Reset_Episode_{n}_20261018.txt')
  out['Episodes'].append({'Episode':f'S3 Episode {n}: {title}','Branch':branch,'Delivery Status':'Delivered; acceptance not inferred; scoped later author overrides apply','Manuscript SHA256':hashlib.sha256(raw).hexdigest(),'Checkpoint Source':owner})
 out['Episodes'].append({'Episode':'S3 Episode 21','Branch':branch,'Delivery Status':'Next unwritten; NO PLAY','Checkpoint Source':'state/Post_Chris_Restart.json'})

 mechanics=[
 ('Black Marrow','Kaze','Current earned','canon/characters/kaze_current.md; canon/characters/kaze_future_progression.md','Single living formed weapon; Cleave and World-Cutting Slash require Black Marrow delivery. Full prerequisites remain.'),
 ('Right EMS / Black Fire','Kaze','Retained','canon/characters/kaze_current.md','No matching left EMS or Susanoo granted. Copying does not copy biology, artifacts or private knowledge.'),
 ('BLACKLIGHT','Kaze','Retained','canon/characters/kaze_current.md','Distinct from removed electrical package. No extra formed weapon or unsupported elasticity.'),
 ('Nightmare','Kaze','Retained scoped package','canon/characters/kaze_current.md','No other removed League demon packages; full target-specific rules remain.'),
 ('Shrine / Sukuna functions','Kaze','Retained','canon/characters/kaze_future_progression.md','Cleave and World-Cutting Slash sword-only; no automatic crossover curse bypass.'),
 ('Darkin / CASA / Warwick senses and recovery','Kaze','Retained','canon/characters/kaze_current.md','Qualitative recovery is not retroactive repair or gear regeneration.'),
 ('BLACKCURRENT','Kaze','Removed','canon/characters/kaze_current.md','All electrical derivatives removed.'),
 ('Rinnegan / Swap','Kaze','Removed','canon/characters/kaze_current.md','All dependent functions removed. No inherited ten-meter swap from old research.'),
 ('Beast','Daniel','Only approved transformation','character_sources/Daniel_Character_Source.txt','Base/Beast only; no retired form-specific powers.'),
 ('A Pluck of Many','Daniel','Approved limited fighting hair duplicates','canon/characters/daniel.md','Small temporary weaker destructible group; no full powers, duplicate real inventory or independent Beast; exact caps unchosen.'),
 ('Cloud Step / Rock Solid / Counterflow / Immobilize','Daniel','Approved under complete owner','canon/characters/daniel.md; canon/characters/daniel_repertoire.yaml','Five foundations organize 95 detailed techniques. No unselected numerical caps or magical exit invented.'),
 ('Spear / chain blade / shurikens','Daniel','Retained','character_sources/Daniel_Character_Source.txt','Real reach, grip, tension and geometry; no invented chain length or extra weapons.'),
 ('Frosted amber-filled bottle','Daniel','Unbreakable replenishing bottle','canon/characters/daniel.md','No bottle respawn or unlimited flood throughput; no switch-based cure.'),
 ('UNSHAKEN','Arthur','Current earned','character_sources/Arthur_Character_Source.txt','Two ten-round revolvers; real ammunition, charge and geometry.'),
 ('HIGH NOON / THE COUNT core','Arthur','Current earned','character_sources/Arthur_Character_Source.txt','Two configurations of one primary core sharing heat/damage/feedstock; not separate carried guns.'),
 ('THE COUNT','Arthur','Current earned','character_sources/Arthur_Character_Source.txt','Artillery penetrator; actual authorization, supported recoil path, charge, feedstock and cycling.'),
 ('Hypercharge','Arthur','Retained mode; use history must be evidenced','character_sources/Arthur_Character_Source.txt','Sustains priming without raising apex or granting infinite feedstock; no invented completed-shot tally.'),
 ('THE CRITIC','Chris','Current earned','canon/characters/chris_catfish_billy_future.md','Real core, modes, ammunition and exterior custody. Not Arthur Count power; repaired sight remains repaired.'),
 ('CHOW MAIN / HAMMER TIME / BONER','Chris','Retained','character_sources/Chris_Character_Source.txt','Use actual weapon positions, reserve ammunition and current exterior state.'),
 ('Dead Eye','Chris','Earned','character_sources/Chris_Character_Source.txt','Reload only from actual compatible reserves; does not create rounds.'),
 ('Subaru / X-wing','Chris','Single current vehicle','state/Post_Chris_Restart.json','E20 deployed/empty recall twice; fuel used, not reset by recall. No R2 location or fuel total invented.'),
 ('Teemo mask / rifle consciousness','Chris','One consciousness','canon/characters/chris_catfish_billy_current.md','No duplicated assistant, gun control or unauthorized communication channel.'),
 ('BELLY / CLEAR MEAT','Billy','Current retained','character_sources/Chris_Billy_BELLY_Source.txt','Billy controls intake, custody and egress; sight/sound permeability only; no involuntary prisoner effect leakage.'),
 ('Chris / Billy exterior switch','Chris and Billy','One exterior only','character_sources/Chris_Billy_BELLY_Source.txt','Same location; no duplicate bodies, teleportation, invulnerability or automatic healing.'),
 ('Bayou','Billy','Current source-governed','canon/characters/chris_catfish_billy_current.md','Exterior overlay ends on switch to Chris; no crushing/telefrag closure.'),
 ('Immortality / consciousness','Billy','Retained','character_sources/Billy_Character_Source.txt','Billy cannot die or lose consciousness; do not copy ontology to other Sins.'),
 ('TWANG / Dead Note','Billy','Retained source-governed','canon/characters/chris_catfish_billy_current.md','Actual banjo interception; Dead Note requires observation of specific energy execution, not universal depowering.'),
 ('Rick biomechanical Billy evolution','Billy','Selected future; not earned','state/Post_Chris_Restart.json','No future body size/anatomy or tongue imported into current state.')]
 for label,owner,available,path,limits in mechanics:
  out['Abilities and Equipment'].append({'System or Item':label,'Owner':owner,'Availability':available,'Mechanics Owner':path,'Limitations':limits})
 cp=read(cur['checkpoint_owner'])
 for i,event in enumerate(cp['actor_knowledge_and_consequences'],1):
  # Superseded Briar contact is kept only in exact source evidence, never projected as active state.
  if 'Briar' in event:continue
  out['Consequences'].append({'Event':f'E20 consequence {i:02d}','Episode Evidence':cur['checkpoint_owner']+f'#/actor_knowledge_and_consequences/{i-1}','Affected Actors':'See exact event and scoped actor knowledge','World Effect':event,'Acceptance Status':'Delivered provisional; limited author overrides take precedence'})
 for key,val in cur['current_resources'].items():
  out['Consequences'].append({'Event':'E20 resource: '+key,'Episode Evidence':'state/Post_Chris_Restart.json#/current_reconciliation_20261018/current_resources/'+key,'Affected Actors':'As specified in source','World Effect':json.dumps(val,ensure_ascii=False) if not isinstance(val,str) else val,'Acceptance Status':'Derived current reconciliation; no new transfer or gain'})
 authorities=['authority/Character_Removal_20261018.json','authority/Resolution_Register.json','state/work/Briar_First_Meeting_Author_Override_20261018.json','state/work/Kaze_Solo_Romance_20261018.json','state/work/Female_Roster_Restoration_20261018.json','canon/relationships/Kaze_Adult_Romance_20261018.md','canon/presentation/Season3_Approved_Portrayal_Patch_20261018.md']
 labels=['Removed identities exclusion','Authority and conflict resolution','Briar first-meeting override','Kaze solo / ensemble presentation hold','Female living-return scope and exceptions','Adult romance and agency','Recovery, repairs, Inside Job and TPP portrayal']
 for owner,label in zip(authorities,labels):
  out['Author Decisions'].append({'Decision':label,'Effective Date':'2026-10-18','Authority Path':owner,'Scope':'Read complete scoped owner. No story advancement; source hierarchy retained.','Supersedes':'Only same-responsibility conflicts within explicit scope; no blanket history or source deletion'})
 research=[(n,v) for n,v in m['logical_modules'].items() if (n.startswith(('research/','research_sources/','reference/research/')) and v['role'] not in ('historical_evidence','historical_archive'))]
 for n,v in research:
  out['Research Evidence'].append({'Source':n,'Actor or Topic':Path(n).stem.replace('_',' '),'Source Type':'Preserved source-owner evidence; coverage varies by owner','Verified Coverage':'Exact module bytes verified SHA256 '+v['sha256']+'. Read full owner for original primary/secondary/scene coverage; no fresh web verification claimed.','Open Gaps':'No new audiovisual certification. Owner-local unknowns remain. Legacy portability/loadout/crossover rules remain open for Kratos; removed swap wording in GOW research is subordinate to current Kaze removals.' if 'GOW_Baldur' in n else 'Read owner-local evidence limits; indexed does not mean every claim is verified.'})
 for n,v in m['logical_modules'].items():
  out['Source Owners'].append({'Logical Owner':n,'Physical Source':v['physical_source'],'Role':v['role'],'SHA256':v['sha256'],'Byte Offset':v['byte_offset'],'Byte Length':v['byte_length'],'Release':m['release']})
 overlay_path=Path(root)/'continuity/REFERENCE_OVERLAY.json'
 if overlay_path.exists():
  overlay=json.loads(overlay_path.read_text(encoding='utf-8'))
  keys={'Characters':'Character','Episodes':'Episode','Consequences':'Event','Author Decisions':'Decision'}
  out['Episodes']=[r for r in out['Episodes'] if r['Episode']!='S3 Episode 21']
  for table,records in overlay.items():
   if table not in keys:raise ValueError('Unexpected overlay table: '+table)
   key=keys[table]; merged={r[key]:r for r in out[table]}
   if len({r[key] for r in records})!=len(records):raise ValueError('Duplicate overlay keys: '+table)
   for record in records:merged[record[key]]=record
   out[table]=list(merged.values())
 return out
if __name__=='__main__':
 root=Path(sys.argv[1] if len(sys.argv)>1 else '.');out=project(root)
 print(json.dumps(out,ensure_ascii=False,indent=2))
