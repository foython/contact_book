from save_contact import save

def remove(contacts):
            user_input = input('Enter contacts any of four info to remove ').strip()
            
            if not user_input:
                print('The contact info cannot be empty, try again')
                
            else:
                if user_input.isnumeric():
                    user_input = int(user_input)                            
                    
                if contacts:
                    for item in contacts:
                        if user_input in item.values():
                            contacts.remove(item) 
                            save(contacts)
                            print(f'Contact {item} removed successfully')            
                            break
                    else:
                        print('Item not found.')  