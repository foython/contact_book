def contact_view(contacts):
    if contacts:
        sorted_contacts = sorted(contacts, key=lambda x: x['name'])
        print('Showing contact by name in ascending order\n')
        
        for item in sorted_contacts:    #printing from file sorted by name        
            print(f'Name : {item['name']}')
            print(f'Number : {item['number']}')
            print(f'Email : {item['email']}')
            print(f'Address : {item['address']}\n')
            
    else:
        print('\nNo contact to show')
    