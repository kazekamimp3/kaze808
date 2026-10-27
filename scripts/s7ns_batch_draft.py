#!/usr/bin/env python3
"""Safe S7NS E82-E100 batch draft generator. Never edits official continuity."""
import argparse,datetime as dt,json,os,re,subprocess,time,urllib.error,urllib.request
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
HANDOFF=ROOT/"continuity/author/S7NS_SPACE_ARC_E82_E100_AI_STUDIO_HANDOFF_20261027.md"
READINESS=ROOT/"continuity/work/S7NS_SPACE_ARC_E82_READINESS_20261026.md"
CURRENT=ROOT/"continuity/CURRENT.json"; LEDGER=ROOT/"continuity/DELIVERY_LEDGER.json"
REFRESH=ROOT/"continuity/work/S7NS_EPISODE_RECORD_REFRESH_20261026.json"
RUN_ID=re.sub(r"[^A-Za-z0-9_-]","",os.getenv("GITHUB_RUN_ID","manual"))
OUT=ROOT/"continuity/drafts"/f"ai_studio_run_{RUN_ID}"
CANDIDATES={
"Kaze":["complete_sources/characters/Kaze_Character_Source_COMPLETE.txt","character_sources/Kaze_Character_Source.txt","canon/characters/kaze_current.md"],
"Chris":["complete_sources/characters/Chris_Character_Source_COMPLETE.txt","character_sources/Chris_Character_Source.txt","canon/characters/Chris_Food_Stash_20261019.md"],
"Daniel":["complete_sources/characters/Daniel_Character_Source_COMPLETE.txt","character_sources/Daniel_Character_Source.txt","canon/characters/daniel.md"],
"Billy":["complete_sources/characters/Billy_Character_Source_COMPLETE.txt","character_sources/Billy_Character_Source.txt","canon/characters/chris_catfish_billy_current.md"],
"Wade/Deadpool":["complete_sources/characters/Deadpool_Character_Source_COMPLETE.txt","character_sources/season3/Deadpool_Character_Source.txt","canon/presentation/Deadpool_Primary_Narration_After_E32_20261019.md"],
"Arthur":["complete_sources/characters/Arthur_Character_Source_COMPLETE.txt","character_sources/Arthur_Character_Source.txt"],
"Matt Murdock":["complete_sources/characters/Matt_Murdock_Character_Source_COMPLETE.txt","character_sources/Matt_Murdock_Character_Source.txt"],
"Dana/Mana":["canon/characters/Dana_Mana_Restored_Current_Access_20261019.md","authority/Dana_Mana_Reinstated_20261019.json"],
"BELLY":["complete_sources/topics/Chris_Billy_BELLY_Source_COMPLETE.txt","character_sources/Chris_Billy_BELLY_Source.txt","canon/household/BELLY_ATHF_Dysfunction_After_E34_20261019.md"],
"Combat":["complete_sources/topics/Shared_Combat_and_Power_Rules_Source_COMPLETE.txt","topic_sources/Shared_Combat_and_Power_Rules_Source.txt"],
"Factions":["complete_sources/topics/Factions_and_Retaliation_Source_COMPLETE.txt","topic_sources/Factions_and_Retaliation_Source.txt"],
"Travel":["complete_sources/topics/Runeterra_World_and_Travel_Source_COMPLETE.txt","topic_sources/Runeterra_World_and_Travel_Source.txt"],
"Narration":["complete_sources/topics/Narration_and_Episode_Presentation_Source_COMPLETE.txt","topic_sources/Narration_and_Episode_Presentation_Source.txt"]}
MAP={
82:["Kaze","Chris","Billy","Wade/Deadpool","Dana/Mana","Narration","Combat","BELLY"],83:["Kaze","Chris","Daniel","Billy","Arthur","Narration","Combat","Factions"],84:["Billy","Kaze","Chris","Daniel","Wade/Deadpool","Narration","Combat"],85:["Kaze","Chris","Daniel","Billy","Wade/Deadpool","Factions","Narration"],86:["Kaze","Chris","Daniel","Billy","Wade/Deadpool","BELLY","Combat"],87:["Kaze","Arthur","Chris","Daniel","Combat","Factions"],88:["Kaze","Chris","Arthur","Factions","Narration"],89:["Kaze","Chris","Billy","Arthur","BELLY","Combat"],90:["Kaze","Arthur","Chris","Combat","Factions"],91:["Kaze","Chris","Wade/Deadpool","Factions","Narration"],92:["Kaze","Billy","Chris","Wade/Deadpool","Factions","Combat"],93:["Kaze","Arthur","Factions","Combat"],94:["Kaze","Chris","Daniel","Billy","Combat","Factions"],95:["Kaze","Arthur","Chris","Billy","Factions","Combat"],96:["Kaze","Arthur","Combat","Factions"],97:["Kaze","Chris","Daniel","Billy","Combat"],98:["Kaze","Chris","Daniel","Billy","Combat","BELLY"],99:["Kaze","Daniel","Billy","Combat","BELLY","Travel"],100:["Kaze","Billy","Wade/Deadpool","Factions","Travel","BELLY"]}
def read(p,required=False):
 if not p.is_file():
  if required: raise RuntimeError("Required source missing: "+str(p.relative_to(ROOT)))
  return ""
 return p.read_text(encoding="utf-8")
def section(text,start,end):
 m=re.search(r"(?ms)^"+re.escape(start)+r".*?(?=^"+re.escape(end)+r"|\Z)",text)
 return m.group(0).strip() if m else ""
def card_for(text,n):
 m=re.search(rf"(?ms)^### E{n}\s+—\s+(.+?)\s*\n(.*?)(?=^### E\d+\s+—|^## \d+\.|\Z)",text)
 if not m: raise RuntimeError(f"No approved card for E{n}.")
 return m.group(1).strip(),m.group(2).strip()
def state():
 c=json.loads(read(CURRENT,True)); l=json.loads(read(LEDGER,True)); r=json.loads(read(REFRESH)) if REFRESH.exists() else {}
 return json.dumps({"CURRENT":{"last_delivered_episode":c.get("last_delivered_episode"),"next_episode":c.get("next_episode")},"DELIVERY_LEDGER":{"current_delivered_episode":l.get("current_delivered_episode"),"next_episode":l.get("next_episode")},"unresolved_gaps":r.get("unchanged_gaps",[]),"rule":"Read-only. E82-E100 are future proposals, not the official cursor."},ensure_ascii=False,indent=2)
def owners(n):
 out=[]; missing=[]
 for label in MAP[n]:
  p=next((ROOT/x for x in CANDIDATES[label] if (ROOT/x).is_file()),None)
  if p: out.append("\n\n===== "+label+": "+str(p.relative_to(ROOT))+" =====\n"+p.read_text(encoding="utf-8"))
  else: missing.append(label)
 return "\n".join(out),missing
def remote_paths():
 result=set()
 try:
  refs=subprocess.check_output(["git","for-each-ref","--format=%(refname)","refs/remotes/origin"],cwd=ROOT,text=True).splitlines()
  for ref in refs:
   try: result.update(subprocess.check_output(["git","ls-tree","-r","--name-only",ref],cwd=ROOT,text=True,timeout=30).splitlines())
   except Exception: pass
 except Exception: pass
 return result
def generate(prompt,model,key,max_tokens):
 body={"model":model,"input":prompt,"generation_config":{"max_output_tokens":max_tokens,"thinking_level":"high"},"store":False}
 req=urllib.request.Request("https://generativelanguage.googleapis.com/v1beta/interactions",data=json.dumps(body).encode(),headers={"Content-Type":"application/json","x-goog-api-key":key,"Api-Revision":"2026-05-20"},method="POST")
 try:
  with urllib.request.urlopen(req,timeout=900) as r: data=json.loads(r.read().decode())
 except urllib.error.HTTPError as e: raise RuntimeError(f"Gemini API HTTP {e.code}: {e.read().decode(errors='replace')[:1500]}") from e
 if data.get("status")!="completed": raise RuntimeError("Gemini interaction status: "+str(data.get("status")))
 chunks=[]
 for step in data.get("steps",[]):
  if step.get("type")=="model_output": chunks += [x.get("text","") for x in step.get("content",[]) if x.get("type")=="text"]
 result="\n".join(chunks).strip()
 if not result: raise RuntimeError("Gemini returned no manuscript text.")
 return result,data.get("usage",{})
def main():
 ap=argparse.ArgumentParser(); ap.add_argument("--start-episode",type=int,required=True); ap.add_argument("--count",type=int,required=True); ap.add_argument("--model",default="gemini-3.8-flash"); ap.add_argument("--max-output-tokens",type=int,default=24576); a=ap.parse_args()
 if not 82<=a.start_episode<=100: raise SystemExit("Safety stop: only E82-E100 are supported.")
 if not 1<=a.count<=5 or a.start_episode+a.count-1>100: raise SystemExit("Safety stop: batch must be 1-5 episodes within E82-E100.")
 key=os.getenv("GEMINI_API_KEY","").strip()
 if not key: raise SystemExit("Missing GEMINI_API_KEY Actions secret; see continuity/work/S7NS_BATCH_DRAFTING_GUIDE.md.")
 if OUT.exists(): raise SystemExit("Output folder already exists; refusing to overwrite.")
 handoff=read(HANDOFF,True); readiness=read(READINESS); curstate=state()
 intent=read(ROOT/"canon/presentation/S7NS_Authorial_Intent_Raw_Note_Fidelity_Active_Comedy_v1_1_20261020.md")
 doctrine=read(ROOT/"canon/presentation/Season3_Scene_Decision_Doctrine_20261010.md")
 plain=read(ROOT/"canon/presentation/S7NS_Plain_Language_Work_Communication_20261021.md")
 global_rules=section(handoff,"## 2. Global rules","## 3.")
 protected=section(handoff,"## 3. Protected opening scene","## 4.")
 existing=remote_paths(); OUT.mkdir(parents=True,exist_ok=False); records=[]
 for n in range(a.start_episode,a.start_episode+a.count):
  title,card=card_for(handoff,n)
  dup=[p for p in existing if re.search(rf"(?i)(?:^|/)(?:E{n:02,3}|Episode[_ -]?{n:02,3})\b",p) and any(x in p.lower() for x in ("draft","batch","ai_studio"))]
  if dup: raise SystemExit(f"Possible existing draft for E{n}; inspect before rerunning: "+", ".join(dup[:5]))
  owner_text,missing=owners(n)
  special=("\n\nPROTECTED E82 OPENING:\n"+protected+"\n\nE82 READINESS OWNER:\n"+readiness) if n==82 else ""
  prompt=f"""Write one complete, polished S7NS episode manuscript, not an outline or synopsis.
EPISODE: E{n} — {title}
STATUS: proposed draft only; no PLAY, official delivery, author acceptance, or fictional-time/cursor advance.

READ-ONLY OFFICIAL STATE:
{curstate}
E74-E80 source/delivery/title gaps remain unresolved. E80-E81 backups exist, but this does not reconcile the official cursor. Never change CURRENT.json, DELIVERY_LEDGER.json, checkpoints, or existing manuscripts. E82-E100 are future-development proposals, not the official next sequence.

AUTHORIAL INTENT:
{intent}

ONE SCENE DECISION DOCTRINE:
{doctrine}

PLAIN-LANGUAGE / FIDELITY RULES:
{plain}

GLOBAL RULES FROM APPROVED ARC HANDOFF:
{global_rules}

TARGET EPISODE CARD — preserve required outcomes:
{card}
{special}

AVAILABLE RELEVANT SOURCE OWNERS:
{owner_text}

Mapped owner groups unavailable: {", ".join(missing) if missing else "none"}.
Do not invent major canon, biography, powers, relationships, or fixes to fill missing sources. Keep unknowns unknown.

Write actual scenes with dialogue, physical staging, causal escalation, distinct voices, character-specific comedy, and legible action where appropriate. Preserve protected lines, locked outcomes, and ending state. Wade/Deadpool narrates ordinary main-story episodes within established knowledge; characters cannot hear him without permission. Track consequential ship damage/reserves, injuries, cargo, ammunition, artifacts/keys, BELLY residents, information, travel/time, and faction motives. No free repairs, fuel, healing, ammunition, authentication, or new powers. No generic filler, interchangeable enemy waves, forced joke quotas, arbitrary cameos, or exposition-only scenes. Preserve permitted profanity and absurdity; do not soften author intent. Aim for 2,500–4,000 words when the card supports it. Silently check all card requirements and repair misses. Return only the finished manuscript beginning “Episode {n}: {title}”.
"""
  print(f"Generating E{n} — {title}",flush=True); manuscript,usage=generate(prompt,a.model,key,a.max_output_tokens)
  if not manuscript.startswith(f"Episode {n}:"): manuscript=f"Episode {n}: {title}\n\n"+manuscript
  words=len(re.findall(r"\b[\w’'-]+\b",manuscript)); warnings=[]
  if words<1800: warnings.append(f"Short output ({words} words); review completeness.")
  if usage.get("total_output_tokens",0)>=int(a.max_output_tokens*.94): warnings.append("Output near token ceiling; check for truncation.")
  target=OUT/f"E{n:03d}_DRAFT.md"; target.write_text(manuscript.rstrip()+"\n",encoding="utf-8")
  records.append({"episode":n,"title":title,"path":str(target.relative_to(ROOT)),"words":words,"model":a.model,"usage":usage,"missing_owner_groups":missing,"warnings":warnings,"status":"PROPOSED_DRAFT_NOT_DELIVERED"})
  print(f"Saved E{n}: {words} words",flush=True); time.sleep(1)
 c=json.loads(read(CURRENT,True)); l=json.loads(read(LEDGER,True))
 report={"schema":"S7NS_AI_STUDIO_DRAFT_BATCH_REPORT_V1","created_utc":dt.datetime.now(dt.timezone.utc).isoformat(),"run_id":RUN_ID,"model":a.model,"batch":{"start_episode":a.start_episode,"count":a.count,"end_episode":a.start_episode+a.count-1},"status":"PROPOSED_DRAFTS_ONLY","official_cursor":{"CURRENT_last_delivered":c.get("last_delivered_episode"),"CURRENT_next":c.get("next_episode"),"LEDGER_last_delivered":l.get("current_delivered_episode"),"LEDGER_next":l.get("next_episode")},"continuity_warning":"E74-E80 source/delivery/title gaps remain unresolved. Official cursor files were not changed.","episodes":records}
 (OUT/"BATCH_REPORT.json").write_text(json.dumps(report,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
 lines=[f"# S7NS AI Studio Draft Batch — {RUN_ID}","","- Status: proposed drafts only; nothing delivered or accepted.","- Official cursor files were not changed.","- Continuity gate: CURRENT/ledger remain E73 / next E74 until E74-E80 are reconciled.","","## Drafts",""]
 for r in records:
  lines.append(f"- **E{r['episode']} — {r['title']}**: {r['path']} ({r['words']} words)")
  for gap in r["missing_owner_groups"]: lines.append(f"  - Mapped owner unavailable: {gap}")
  for warning in r["warnings"]: lines.append(f"  - Review warning: {warning}")
 lines += ["","Read each complete manuscript and repair it against current source owners before any delivery."]
 (OUT/"BATCH_REPORT.md").write_text("\n".join(lines)+"\n",encoding="utf-8")
 print("Batch complete: "+str(OUT.relative_to(ROOT)),flush=True)
if __name__=="__main__": main()
