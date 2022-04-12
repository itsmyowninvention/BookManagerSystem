import json
class User:
    def __init__(self,id, password, name, identity):
        
        self.id = id # 用户ID
        
        self.password = password # 密码
        
        self.name = name # 用户名
        
        self.identity = identity # 身份
        
logged_in_user : User = None # 登录用户信息


def isLogged() -> bool: # 检查登录状态
    global logged_in_user
    return logged_in_user != None

def load():
    result = {}
    with open('./data/user.json') as file:
        users = json.load(file)
    for user in users:
        result[user['id']] = User(
                id = user['id'],
                password = user['password'],
                name = user['name'],
                identity = user['identity'])
    return result
    
def dump(users):
    result = []
    for user in users.values():
        result.append(
            {
                'id':user.id,
                'password':user.password,
                'name':user.name,
                'identity':user.identity
            }
        )
    with open('./data/user.json', 'w') as file:
        json.dump(result, file)

def login(id,password) -> User:
    users = load() # 用户列表
    
    global logged_in_user # 登录用户
    
    if isLogged(): # 用户已登录
        return None
    if(id not in users):
        return None
    
    if users[id].password == password:
        logged_in_user = users[id]
    
    return logged_in_user
    
def logout() -> bool:
    if not isLogged(): # 未登录
        return False
    logged_in_user = None
    return True

def selectUser(id) -> User:
    users = load()
    return users[id]


def changePassword(password) -> bool:
    if not isLogged(): # 未登录
        return False
    global logged_in_user
    logged_in_user.password = password
    users = load()
    users[logged_in_user.id].password = password
    dump(users)
    

                
    
    
    
        
        