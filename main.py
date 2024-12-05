from add_contact import add_contact
from read_file import read
from view_contact import contact_view
from search_cont import search
from remove_cont import remove


contacts = read() #loading data from file

if not contacts:
    contacts = []

while True:
    print('\nWelcome to Contact Management System')
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Remove Contact")
    print("0. Exit")
    option = input("Select an option:  ") # taking user input 
    option = option.strip()    # removing extra white space   
    
    if option == '0':
        print('Thanks for using Contact Management System')
        break
    
    elif option == '1':
        add_contact(contacts)

    elif option == '2':
       contact_view(contacts)
    
    elif option == '3':
        search(contacts)
    
    elif option == '4':
        remove(contacts)
    
    else:
        print('Wrong input, try again')