print("Division of two no:")
while True:
    first_no=input("Enter first no:")
    if first_no=="q":
        break
    second_no=input("Enter second no:")
    if second_no=="q":
        break
    try:
        ans=int(first_no)/int(second_no)
    except ZeroDivisionError:
        print("Can't divide by Zero")
    else:
        print(ans)
