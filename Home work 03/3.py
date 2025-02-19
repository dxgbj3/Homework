age = int(input('Age: '))
price = 100.0
print('Before discount:',price)
if age < 18:
    price = price - price * 0.1
elif 18 < age < 60:
    price = price - price * 0.05
else:
    price = price - price * 0.15
print('After discount:', price)