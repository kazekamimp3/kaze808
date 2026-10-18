"""Mutation tests: verify corruption, missing owners, and unsafe paths fail."""
import shutil, tempfile
from pathlib import Path
from source_store import SourceStore
from validate import validate
root=Path(__file__).resolve().parents[1]
s=SourceStore(root)
assert validate(root)['result']=='PASS'
name='state/evidence/S3_Reset_Episode_20_20261018.txt'
raw=s.read(name)
assert __import__('hashlib').sha256(raw).hexdigest()=='12c91032405edf9c8aae912d55f52d66481d6e4ecdf151e02f8727ce27905d58'
with tempfile.TemporaryDirectory() as tmp:
    t=Path(tmp)
    for f in s.manifest['physical_sources']:
        shutil.copyfile(s.path(f['path']), t/f['path'])
    (t/'MANIFEST.yaml').write_bytes(s.path('MANIFEST.yaml').read_bytes())
    assert validate(t)['result']=='PASS'
    # Corrupt only temporary copies; production source bytes are never written.
    target=s.manifest['logical_modules'][name]['physical_source']
    (t/target).unlink();(t/target).write_bytes(b'corrupt')
    assert validate(t)['result']=='FAIL'
    (t/target).unlink()
    assert validate(t)['result']=='FAIL'
try:s.path('../escape')
except ValueError:pass
else:raise AssertionError('Traversal allowed')
print('PASS: baseline, E20 exact retrieval, corruption, missing source, path traversal')
