username=input()
password=input()
if not bool(username.strip() and password.strip()):
    print("Username and password are empty!")
else:
    print("Username: {}\nPassword: {} ".format(username,password))