import json


with open('Lojas.json', 'rb')as f:
    USERS = json.load(f)
    USERS = USERS.pop('Lojas')  
    

print(USERS)
