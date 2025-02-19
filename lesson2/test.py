user_name = input('Whats your name: ')
age = int(input('Whats your age: '))
if age <= 18:
    status = 'child'
else:
    status = 'adult'

form = f"""====================
Hi {user_name}! You are {age} years old!
You are {status}.
===================="""
print(form)
