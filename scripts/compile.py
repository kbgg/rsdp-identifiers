import glob
import json
import os

def main():
    if not os.path.exists('build/'):
        os.makedirs('build/')

    identifiers = {}    
    identifier_files = glob.glob('identifiers/*.json')

    for identifier_file in identifier_files:
        if identifier_file == 'identifiers/template.json':
            continue

        with open(identifier_file, 'r') as f:
            data = json.load(f)
            identifiers[data['id']] = data

    with open('build/identifiers.json', 'w') as f:
        f.write(json.dumps(identifiers, indent=4, sort_keys=True))

if __name__ == '__main__':
    main()