a = int(input(': '))
b = int(input(': '))
days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

for i in range(a, b+1):
    print(days[i-1])