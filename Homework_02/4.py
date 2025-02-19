num = int(input("Enter any number: "))
a = 1
while num > 0:
    digit = num % 10
    a *= digit
    num //= 10
print("Production of these numbers:", a)
