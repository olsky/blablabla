#!/usr/bin/env python3
"""Validate Session 3 EPICs against schema."""

import yaml
import json
from pathlib import Path
from jsonschema import Draft202012Validator

schema_path = Path('schemas/epic.schema.json')
with open(schema_path) as f:
    schema = json.load(f)

validator = Draft202012Validator(schema)

epic_ids = ['EP-0910', 'EP-0911', 'EP-0912', 'EP-0913', 'EP-0914']
passed = []
failed = []

for epic_id in epic_ids:
    epic_path = Path(f'project/epics/{epic_id}.yaml')
    
    try:
        with open(epic_path) as f:
            data = yaml.safe_load(f)
        
        validator.validate(data)
        passed.append(epic_id)
        print(f'✓ {epic_id}: PASS')
        
    except Exception as e:
        failed.append((epic_id, str(e)[:100]))
        print(f'✗ {epic_id}: FAIL - {str(e)[:100]}')

print(f'\n{"="*70}')
print(f'VALIDATION RESULTS: {len(passed)}/{len(epic_ids)} PASSED')
print(f'{"="*70}')

if failed:
    print('\nFailed EPICs:')
    for epic_id, error in failed:
        print(f'  - {epic_id}: {error}')
else:
    print('\n✓ All 5 Session 3 EPICs validated successfully!')
