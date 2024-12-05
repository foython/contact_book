def search(contacts):
    if contacts:
        user_input = input('Enter contacts any of four info to search ').strip() #taking input and removing extra white space
        
        if user_input.isnumeric(): #Checking if the input is number
            user_input = int(user_input)              
       
        for item in contacts:       #looping to find if user input in file
            if user_input in item.values():
                print('Contact matched\n')
                print(f'Name : {item['name']}')
                print(f'Number : {item['number']}')
                print(f'Email : {item['email']}')
                print(f'Address : {item['address']}')
                print('\n')
                break
        else:
            print('\nNo such contact')
    else:
        print('\nList empty, No contact to search')    