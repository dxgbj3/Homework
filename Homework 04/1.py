import re
print("Please create a password, it must be at least 8 characters long and contain at least one uppercase letter, lowercase letter and numbers.")

def check_password():
    while True:
        password = input("Enter your password: ")

        if len(password) < 8:
            print("your password must be at least 8 characters long.")
            continue
        if not re.search(r'\d', password):
            print("your password must contain at least one number character.")
            continue
        if not re.search(r'[A-Z]', password) or not re.search(r'[a-z]', password):
            print("your password must contain at least one lower and one upper case letter.")
            continue
        else:
            print("your password is done.")
            return True

check_password()
