import re
import json

def validateJSONSchema(obj):

    #check if object was passed
    if not bool(obj):
        return generateResponse("Input File is Empty")
    

    # print(type(text.get("FReDTemplateFormatVersion")))
    if not type(obj.get("FReDTemplateFormatVersion")) == str:
        return generateResponse("Template Version has to be a String")
    

    for value in obj.get("Resources"):
        if not type(value.get("Name")) == str:
            return generateResponse("Name of Resource has to be a String")
        
        if value.get("Type") == "FReD":
            if not type(value.get("Properties")) == dict:
                return generateResponse("'Propeties' attribute of Resource should be an Object or is not found")
            

            if not type(value.get("Properties").get("Nodes")) == dict:
                return generateResponse("'Nodes' attribute of Propeties should be an Object or is not found")
            

            if not type(value.get("Properties").get("Nodes").get("NodeNames")) == list:
                return generateResponse("'NodeNames' attribute of Nodes should be an Object or is not found")
            
            
                

            for nodeName in value.get("Properties").get("Nodes").get("NodeNames"):
                if not type(nodeName) == str:
                    return generateResponse("NodeNames must be string")
                if len(list(filter(lambda node: node == nodeName, value.get("Properties").get("Nodes").get("NodeNames")))) > 1:
                    return generateResponse("NodeNames can not appear more then once in the Nodes List")
            

            if not type(value.get("Properties").get("Clients")) == list:
                return generateResponse("'Clients' attribute of Properties should be an Object or is not found")
            

            for clientValue in value.get("Properties").get("Clients"):
                if not type(clientValue.get("Name")) == str:
                    return generateResponse("Client name should be a string")

            if not type(value.get("Properties").get("KeyGroups")) == list:
                return generateResponse("'KeyGroups' attribute of Properties should be an Object or is not found")

            for keyGroupValue in value.get("Properties").get("KeyGroups"):
                if not type(keyGroupValue.get("Name")) == str:
                    return generateResponse("KeyGroup 'Name' should be a string or is not found")
                
                if not re.compile("^[a-zA-Z0-9]+$").match(keyGroupValue.get("Name")):
                    return generateResponse("Keygroup 'Name' does not match ^[a-zA-Z0-9]+$")
                
                if len(list(filter(lambda keygroup: keygroup.get("Name") == keyGroupValue.get("Name"), value.get("Properties").get("KeyGroups")))) > 1:
                    return generateResponse("KeyGroup names can only be given once")
                
                if not type(keyGroupValue.get("Mutable")) == bool:
                    return generateResponse("KeyGroup attribute 'Mutable' should be a boolean or is not found")
                
                if not type(keyGroupValue.get("Replicas")) == list:
                    return generateResponse("KeyGroup attribute 'Replicas' should be a object or is not found")
                

                for repValue in keyGroupValue.get("Replicas"):
                    if not type(repValue.get("Name")) == str:
                        return generateResponse("KeyGroup replica 'Name' should be a string or is not found")
                    
                    if not repValue.get("Name") in value.get("Properties").get("Nodes").get("NodeNames"):
                        return generateResponse("KeyGroup replica Name should be in the nodes list")
                    
                    if len(list(filter(lambda rep: rep.get("Name") == repValue.get("Name"), keyGroupValue.get("Replicas")))) > 1:
                        return generateResponse("KeyGroup replica can only appear once in the list")
                    
                    if not type(repValue.get("Expiry")) == int:
                        return generateResponse("KeyGroup replica attribute 'Expiry' should be a integer or is not found")
                    

                if not type(keyGroupValue.get("Triggers")) == list:
                    return generateResponse("KeyGroup attribute 'Triggers' should be a list or is not found")
                

                for triValue in keyGroupValue.get("Triggers"):
                    if not type(triValue.get("Name")) == str:
                        return generateResponse("KeyGroup trigger 'Name' should be a string or is not found")

                    if not type(triValue.get("ReceiverAddress")) == int:
                        return generateResponse("KeyGroup trigger attribute expiry should be a integer")

    return generateResponse("Schema contraints fulfilled", True)



def generateResponse(message, valid = False):
    params = {
        'valid': valid,
        'message': message
    }

    return (params)