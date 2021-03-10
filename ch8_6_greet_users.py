#passing a list to a function
def greet_users(names):
    """Print greeting to each user in the list"""
    for n in names:
        msg = f"Hello,{n} !"  
        print(msg)

usernames = ['hannah','ty','margot']
greet_users(usernames)