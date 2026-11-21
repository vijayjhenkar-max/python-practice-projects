import json

def load_contacts():
    try:
        with open("contacts.json", "r") as file:
            return json.load(file)
        
    except FileNotFoundError:
        return []
    
    except json.JSONDecodeError:
        print("Invalid JSON file. Starting with an empty contact list.")
        return []


def save_contacts(contacts):
    with open("contacts.json","w") as file:
        json.dump(contacts,file,indent= 4)