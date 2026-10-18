#!/usr/bin/env python3
"""Read-only byte/routing validation; never adjudicates or promotes canon."""
import hashlib, json, sys
from pathlib import Path
from source_store import SourceStore

def validate(root):
    store = SourceStore(root)
    m = store.manifest
    errors = []
    checked = 0
    for item in m['physical_sources']:
        try:
            raw = store.path(item['path']).read_bytes()
            if hashlib.sha256(raw).hexdigest() != item['sha256']:
                errors.append('HASH MISMATCH ' + item['path'])
            if len(raw) != item['byte_length']:
                errors.append('SIZE MISMATCH ' + item['path'])
            checked += 1
        except (OSError, ValueError) as exc:
            errors.append(str(exc))
    logical = 0
    for name in m['logical_modules']:
        try:
            store.read(name)
            logical += 1
        except (OSError, ValueError, KeyError) as exc:
            errors.append(str(exc))
    if m['physical_bundle_count'] != len(m['physical_sources']):
        errors.append('Declared physical count mismatch')
    if m['logical_module_count'] != len(m['logical_modules']):
        errors.append('Declared logical count mismatch')
    routes = 0
    try:
        index = json.loads(store.read('routing/MASTER_SOURCE_INDEX.json'))
        missing = set(m['logical_modules']) - set(index['source_modules'])
        if missing:
            errors.append('Missing master index modules: ' + repr(sorted(missing)))
        access = json.loads(store.read('complete_sources/ACCESS_INDEX.json'))
        for entry in access['entries']:
            for owner in entry['full_owner_routes']:
                if owner not in m['logical_modules']:
                    errors.append('Missing complete owner: ' + owner)
            routes += 1
        state = json.loads(store.read('state/Post_Chris_Restart.json'))
        current = state['current_reconciliation_20261018']
        for key in ['checkpoint_owner','manuscript_owner']:
            store.read(current[key])
        override = json.loads(store.read('state/work/Briar_First_Meeting_Author_Override_20261018.json'))
        if override['current_relationship']['met'] is not False:
            errors.append('Baseline first-meeting pin changed; requires explicit author review')
        exclusion = json.loads(store.read('authority/Character_Removal_20261018.json'))
        if exclusion.get('status') != 'ACTIVE_EXPLICIT_AUTHOR_REMOVAL':
            errors.append('Exclusion authority inactive')
    except (OSError, ValueError, KeyError) as exc:
        errors.append(str(exc))
    return {'release':m['release'], 'manifest_sha256':hashlib.sha256(store.path('MANIFEST.yaml').read_bytes()).hexdigest(),
        'checked_physical_files':checked, 'checked_logical_modules':logical, 'complete_routes':routes,
        'errors':errors, 'result':'FAIL' if errors else 'PASS',
        'scope':'Byte integrity and route existence only. No semantic acceptance, new event, Project installation or remote synchronization implied.'}

if __name__ == '__main__':
    try:
        result = validate(Path(sys.argv[1]) if len(sys.argv)>1 else Path('.'))
    except Exception as exc:
        result = {'result':'FAIL','errors':[str(exc)]}
    print(json.dumps(result, indent=2))
    sys.exit(result['result'] != 'PASS')
