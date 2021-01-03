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
                return generateResponse("Propeties Attribute of Resource should be an Object")
            

            if not type(value.get("Properties").get("Nodes")) == dict:
                return generateResponse("Nodes Attribute of Propeties should be an Object")
            

            if not type(value.get("Properties").get("Nodes").get("NodeNames")) == list:
                return generateResponse("NodeNames Attribute of Nodes should be an Object")
            
            
                

            for nodeName in value.get("Properties").get("Nodes").get("NodeNames"):
                if not type(nodeName) == str:
                    return generateResponse("NodeNames must be string")
                if len(list(filter(lambda node: node == nodeName, value.get("Properties").get("Nodes").get("NodeNames")))) > 1:
                    return generateResponse("NodeNames can not appear more then once in the Nodes List")
            

            if not type(value.get("Properties").get("Clients")) == list:
                return generateResponse("Clients Attribute of Properties should be an Object")
            

            for clientValue in value.get("Properties").get("Clients"):
                if not type(clientValue.get("Name")) == str:
                    return generateResponse("Client name should be a string")

            if not type(value.get("Properties").get("KeyGroups")) == list:
                return generateResponse("KeyGroups Attribute of Properties should be an Object")

            for keyGroupValue in value.get("Properties").get("KeyGroups"):
                if not type(keyGroupValue.get("Name")) == str:
                    return generateResponse("KeyGroup name should be a string")
                
                if not re.compile("^[a-zA-Z0-9]+$").match(keyGroupValue.get("Name")):
                    return generateResponse("Keygroup name does not match ^[a-zA-Z0-9]+$")
                
                if len(list(filter(lambda keygroup: keygroup.get("Name") == keyGroupValue.get("Name"), value.get("Properties").get("KeyGroups")))) > 1:
                    return generateResponse("KeyGroup names can only be given once")
                
                if not type(keyGroupValue.get("Mutable")) == bool:
                    return generateResponse("KeyGroup attribute mutable should be a boolean")
                
                if not type(keyGroupValue.get("Expiry")) == int:
                    return generateResponse("KeyGroup attribute expiry should be a integer")
                
                if not type(keyGroupValue.get("Replicas")) == list:
                    return generateResponse("KeyGroup attribute Replicas should be a object")
                

                for repValue in keyGroupValue.get("Replicas"):
                    if not type(repValue.get("Name")) == str:
                        return generateResponse("KeyGroup Replica name should be a string")
                    
                    if not repValue.get("Name") in value.get("Properties").get("Nodes").get("NodeNames"):
                        return generateResponse("KeyGroup Replica name should be in the Nodes List")
                    
                    if len(list(filter(lambda rep: rep.get("Name") == repValue.get("Name"), keyGroupValue.get("Replicas")))) > 1:
                        return generateResponse("KeyGroup Replica can only appear once in the list")
                    
                    if not type(repValue.get("Expiry")) == int:
                        return generateResponse("KeyGroup Replica attribute expiry should be a integer")
                    

                if not type(keyGroupValue.get("Triggers")) == list:
                    return generateResponse("KeyGroup attribute Replicas should be a object")
                

                for triValue in keyGroupValue.get("Triggers"):
                    if not type(triValue.get("Name")) == str:
                        return generateResponse("KeyGroup Replica name should be a string")

                    if not type(triValue.get("ReceiverAddress")) == int:
                        return generateResponse("KeyGroup Trigger attribute expiry should be a integer")

    return generateResponse("Schema contraints fulfilled", True)



def generateResponse(message, valid = False):
    params = {
        'valid': valid,
        'message': message
    }

    return (params)