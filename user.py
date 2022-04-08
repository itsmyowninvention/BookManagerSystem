import json
class user:
    def __init__(self,id, password, name, identity):
        
        self.id = id # 用户ID
        
        self.password = password # 密码
        
        self.name = name # 用户名
        
        self.identity = identity # 身份
        
logged_in_user = None # 登录用户信息

def login(self,id,password):
    with open('user.json') as user_file:
        user_json = json.load(user_file)
    global logged_in_user # 登录用户
    user_dict = None # 
    for user in user_json:
        if(user['id'] == id):
            
    

    
    
        
        