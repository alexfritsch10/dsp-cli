import sys
import json
import requests

def main():

    args = sys.argv[1:]
    input = {}
    apiPath = "/"

    if len(args) == 0:
        print("If you want to deploy an infrastructure on FReD please enter: mercury deploy {IaC JSON File Path} \nAn Example for the JSON File is provided on our Website")
        sys.exit()
    if not args[0] == "deploy" and not args[0] == "process" and not args[0] == "get":
        print("The command is unknown")
        sys.exit()

    if args[0] == "deploy":
        if not len(args) == 2:
            print("If you want to deploy an infrastructure on FReD please enter: mercury deploy {IaC JSON File Path} \nAn Example for the JSON File is provided on our Website")
            sys.exit()
        try:
            with open(args[1]) as data:
                input = json.load(data)
        except json.decoder.JSONDecodeError as jex:
            print("JSON is not formatted Correctly")
            print(jex)

    if args[0] == "process":
        if len(args) < 4 or len(args) > 5:
            print("If you want to process data on FReD please enter: mercury process {keygroup name} {key of the data} {value of the data} {optional : function handler name}")
            sys.exit()
        input = {
            "keygroup": args[1],
            "key": args[2],
            "value": args[3],
        }
        if len(args) == 5:
            input["handler"] = args[4]
        apiPath = "/data"

    if args[0] == "get":
        if not len(args) == 3:
            print("If you want to read a data item from a Keygroup please enter: mercury get {keygroup name} {data key}")
            sys.exit()
        apiPath = "/data/" + args[1] + "/" + args[2]

    url = "http://127.0.0.1:8081" + apiPath
    try:    
        if args[0] == "get":
            res = requests.get(url)
        else: 
            res = requests.post(url, json = input)
        response = json.loads(res.text)
        print('- - - - - - - - - -')
        if response.get("Status") == '200':
            print(response.get("Message"))
        else:
            print('Schema is not valid or could not be processed')
            print(response.get("Message"))
        print('- - - - - - - - - -')

    except requests.exceptions.HTTPError as err:
        print(err)

if __name__ == '__main__':
    main()