from save_contact import save
from validation import validate_name, validate_number, validate_email, validate_address

def add_contact(contacts):
    name = validate_name()    
    number = validate_number(contacts)
    email = validate_email(contacts)
    address = validate_address()
    
    
    contact = {
        'name' : name,
        'number' : number,
        'email' : email,
        'address' : address
    }
    
    contacts.append(contact) 
    
    response = save(contacts)
    
    if response == 1:
        print('Contact saved successfully')
    
    
    