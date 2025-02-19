a = input("Enter a number: ")
b = input("Enter a number: ")

if len(a) == 3 and len(b) == 3 and a.isdigit() and b.isdigit():
    result = ''.join([a[i] + b[i] for i in range(3)])
    print("United number:", result)
else:
    print("Enter a valid number")