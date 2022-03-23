from user import User
from hmac import compare_digest

users = [
    User(1,"gokhan","asd")
]

username_mapping = {u.username : u for u in users}
userid_mapping = {u.id : u for u in users}

def authenticate(username,password):
    user = username_mapping.get(username,None)
    #if user and user.password == password:
    print(compare_digest(user.password , password))
    if user and user.password == password:
        return user

def identity(payload):
    user_id = payload["identity"]
    return userid_mapping.get(user_id,None)