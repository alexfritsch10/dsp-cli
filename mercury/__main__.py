import sys
import json
import requests

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
        res = requests.post('http://127.0.0.1:80', json = input)
        response = json.loads(res.text)
        print('- - - - - - - - - -')
        if response.get("Status") == '200':
            print('Schema fulfills all contraints was successfully process by the Backend.')
        else:
            print('Schema is not valid or could not be processed')
            print(response.get("Message"))
        print('- - - - - - - - - -')
            
    except json.decoder.JSONDecodeError as jex:
        print('JSON is not formatted Correctly')
        print(jex)


if __name__ == '__main__':
    main()