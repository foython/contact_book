from read_file import read


def validate_name():
    while True:
        try:
            user_input = input('Enter Contact Name: ').strip()  # Remove extra whitespace
            
            if not user_input.replace(" ", "").isalpha():
                raise ValueError('The contact’s name must be a string and cannot be empty.')
            return user_input
        
        except ValueError as e:
            print(f"Error: {e}")          
            
            
            
def validate_number(contacts):
    while True:
        try:
            user_input = input('Enter Contact Number: ').strip()  
                      
            if not user_input.isnumeric():
                raise ValueError('The contact number must be an integer and cannot be empty.')  
                      
            elif len(user_input) < 5:
                raise ValueError('Number should have five digit')
            
            elif contacts:
                for contact in contacts: # looping for check if number in file
                    if contact['number'] == int(user_input):
                        raise ValueError('Number already saved')
                        
            return int(user_input)
        
        
        except ValueError as e:
            print(f"Error: {e}")
     
            

def validate_email(contacts):
    while True:
        try:
            email = input('Enter Contact Email: ').strip()
                        
            if '@' and '.' not in email:
                raise ValueError("The contact email must have '@', '.' and cannot be empty.")
                       
            elif contacts:
                for contact in contacts:
                    if contact['email'] == email:
                        raise ValueError('Email already exist, use another') 
                                            
            return email.lower()
        
        except ValueError as e:
            print(f"Error: {e}")
            
            

def validate_address():
    while True:
        try:
            address = input('Enter Contact Address: ').strip() 
                       
            if not address:
                raise ValueError('The contact address cannot be empty.')                         
            return address
        
        except ValueError as e:
            print(f"Error: {e}")