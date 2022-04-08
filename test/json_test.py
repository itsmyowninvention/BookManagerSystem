import json

with open('./data/user.json','r') as user_file:
    user_json = json.load(user_file)
    
print(user_json)

for user in user_json:
    print(user['id'])