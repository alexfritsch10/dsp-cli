import sys
import json

from .validateJSONSchema import validateJSONSchema

def main():
    
    args = sys.argv[1:]
    if len(args) == 0:
        print('If you want to deploy an infrastructure on FReD please enter: mercury deploy {IaC JSON File Path} \nAn Example for the JSON File is provided on our Website')
        sys.exit()
    if not len(args) == 2:
        print('Not enough arguments passed')
        sys.exit()
    if not args[0] == 'deploy':
        print('Action {} not found'.format(args[0]))
        sys.exit()

    try:    
        with open(args[1]) as data:
            input = json.load(data)
        res = validateJSONSchema(input)
        print('- - - - - - - - - -')
        if res.get("valid"):
            print('All schema contraints are fulfilled. Going to send the JSON file to our webserver for execution.')
            #sendDataToAPI(input)
        else:
            print('Not all object types of the schema are valid.')
            print(res.get("message"))
        print('- - - - - - - - - -')
            
    except json.decoder.JSONDecodeError as jex:
        print('JSON is not formatted Correctly')
        print(jex)


if __name__ == '__main__':
    main()