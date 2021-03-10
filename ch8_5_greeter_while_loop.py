#using a function in a while loop
def get_formatted_name(first_name,last_name):
    """Return a neatly formatted full name"""
    full_name = f"{first_name} {last_name}"
    return full_name.title()

while True:
    print("Pl enter your name")
    print("(Enter 'q' to quit)")
    f_name = input("First Name :")
    if f_name == 'q':
        break
    l_name = input("Last Name :")
    if l_name == 'q':
        break
    formatted_name = get_formatted_name(f_name,l_name)
    print(f"\nHello, {formatted_name}")
