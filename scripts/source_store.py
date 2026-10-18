"""Read-only access to exact manifest-addressed S7NS source bytes."""
import hashlib
from pathlib import Path
import yaml

class SourceStore:
    def __init__(self, root):
        self.root = Path(root).resolve()
        self.manifest = yaml.safe_load((self.root / 'MANIFEST.yaml').read_text(encoding='utf-8'))
    def path(self, name):
        path = (self.root / name).resolve()
        if not path.is_relative_to(self.root):
            raise ValueError(f'Unsafe source path: {name}')
        return path
    def read(self, name):
        item = self.manifest['logical_modules'][name]
        raw = self.path(item['physical_source']).read_bytes()
        start, length = item['byte_offset'], item['byte_length']
        if not isinstance(start, int) or not isinstance(length, int) or start < 0 or length < 0 or start + length > len(raw):
            raise ValueError(f'Invalid byte range: {name}')
        result = raw[start:start + length]
        if hashlib.sha256(result).hexdigest() != item['sha256']:
            raise ValueError(f'Logical source hash mismatch: {name}')
        return result
