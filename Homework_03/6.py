age = int(input('Age: '))
milage = int(input('Milage: '))
if age < 3 and milage < 30000:
    print('In best conditions')
elif age < 10 and milage < 100000:
    print('In good conditions')
else:
    print('In bad conditions, need diagnostics')