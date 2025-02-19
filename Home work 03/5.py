a = int(input('Rating: '))
b = int(input('Rating: '))
c = int(input('Rating: '))
d = int(input('Rating: '))

if min(a, b, c, d) <= 2:
    print('Not allowed for an exam')
elif a+b+c+d >= 16:
    print('Admitted to the exam with honors.')
else:
    print('Fine to go on the exam')