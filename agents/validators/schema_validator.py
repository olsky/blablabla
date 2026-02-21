import json
import yaml
import glob
import sys
from jsonschema import validate, ValidationError

def load_schema(schema_path):
    with open(schema_path, 'r') as f:
        return json.load(f)

def validate_files(schema_path, glob_pattern):
    schema = load_schema(schema_path)
    files = glob.glob(glob_pattern)
    errors = 0
    
    for f in files:
        with open(f, 'r') as fp:
            try:
                data = yaml.safe_load(fp)
                validate(instance=data, schema=schema)
                print(f"✅ {f} passed schema validation.")
            except ValidationError as e:
                print(f"❌ {f} failed schema validation: {e.message}")
                errors += 1
            except yaml.YAMLError as e:
                print(f"❌ {f} is not valid YAML: {e}")
                errors += 1
                
    return errors

if __name__ == '__main__':
    total_errors = 0
    total_errors += validate_files('schemas/epic.schema.json', 'project/epics/*.yaml')
    total_errors += validate_files('schemas/story.schema.json', 'project/stories/*.yaml')
    total_errors += validate_files('schemas/override.schema.json', 'project/overrides/*.yaml')
    # Review files are nested inside EP directories
    total_errors += validate_files('schemas/review.schema.json', 'project/reviews/**/*.yaml')
    
    if total_errors > 0:
        print(f"Validation failed with {total_errors} errors.")
        sys.exit(1)
    else:
        print("All schema validations passed.")
        sys.exit(0)
