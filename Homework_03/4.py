a = int(input('Rating: '))
b = int(input('Rating: '))
c = int(input('Rating: '))

if min(a, b, c) <= 2:
    print('Unsatisfactory')
elif a+b+c >= 12:
    print('Great')