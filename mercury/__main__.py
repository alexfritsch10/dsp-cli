import sys
import json

import validateJSONSchema

def main():
    print('in main')
    args = sys.argv[1:]
    print('count of args: {}'.format(len(args)))

    if len(args) == 0:
        print('If you want to deploy an infrastructure on FReD please enter: mercury deploy {IaC JSON File Path} \nAn Example for the JSON File is provided on our Website')
        sys.exit()
    if not len(args) == 2:
        print('not enough arguments passed')
        sys.exit()
    if not args[0] == 'deploy':
        print('action {} not found'.format(args[0]))
        sys.exit()
        
    with open(args[1]) as data:
        input = json.load(data)

    print(input)

    print(validateJSONSchema(input))


    for arg in args:
        print('passed argument: {}'.format(arg))

if __name__ == '__main__':
    main()