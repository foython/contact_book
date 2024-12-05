import json

def read():
    try:
        with open('contact.json', 'r+') as fp:          
            if fp:
                data = json.load(fp)
                if data:
                   return data                        
                   
    except FileNotFoundError:
        print('file dosnt exist')
       
        
    except json.JSONDecodeError:
        print('No data in file')
        
    
        