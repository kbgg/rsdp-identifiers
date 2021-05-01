import glob
import json
import jsonschema
from jsonschema import validate


def validate_json(identifier_file, schema):
    data = json.load(open(identifier_file, 'r'))

    try:
        validate(instance=data, schema=schema)
    except jsonschema.exceptions.ValidationError as err:
        return False, err

    if identifier_file.split('/')[-1].split('.')[0] != data['id']:
        return False, 'Filename does not match ID'

    return True, None

def main():
    schema = json.load(open('scripts/schema.json', 'r'))

    identifiers = {}    
    identifier_files = glob.glob('identifiers/*.json')

    for identifier_file in identifier_files:
        if identifier_file == 'identifiers/template.json':
            continue
        valid, message = validate_json(identifier_file, schema)

        if not valid:
            raise Exception(message)

    print('Valid!')

if __name__ == '__main__':
    main()