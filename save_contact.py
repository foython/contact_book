import json

def save(contacts):
    try:       
        with open('contact.json', 'w') as fp:
            json.dump(contacts, fp, indent=4)
            return 1 

    except Exception as e:
        print(f"An error occurred: {e}")
 