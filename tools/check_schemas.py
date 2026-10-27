"""Check that every JSON Schema in schemas/ is valid Draft 2020-12
and that its $id matches the URL where GitHub Pages publishes it."""
import json
import pathlib
import sys

from jsonschema import Draft202012Validator
from jsonschema.exceptions import SchemaError

BASE = "https://cpintl-org.github.io/"
problems = 0
files = sorted(pathlib.Path("schemas").rglob("*.schema.json"))
if not files:
    print("No schema files found in schemas/")
    sys.exit(1)
for f in files:
    schema = json.loads(f.read_text(encoding="utf-8"))
    try:
        Draft202012Validator.check_schema(schema)
    except SchemaError as e:
        print(f"{f}: invalid schema: {e.message[:120]}")
        problems += 1
        continue
    expected = BASE + f.as_posix()
    if schema.get("$id") != expected:
        print(f"{f}: $id is {schema.get('$id')} but expected {expected}")
        problems += 1
    else:
        print(f"{f}: OK")
print("PASS" if not problems else f"FAIL ({problems} problems)")
sys.exit(1 if problems else 0)
