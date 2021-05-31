import json

def get_stored_username():
    """Get stored username if available"""
    filename="username.json"
    try:
        with open(filename) as f:
            username=json.load(f)
    except FileNotFoundError:
        return None
    else:
        return username

def store_username():
    """Store new user"""
    filename="username.json"
    username=input("Enter your username")
    with open(filename,'w') as f:
        json.dump(username,f)
    return username

def greet_user():
    """Greet the user"""
    username=get_stored_username()
    if username:
        print(f"Welcome back {username} !")
    else:
        username=store_username()
        print(f"Username : {username} stored !")      
    
greet_user()