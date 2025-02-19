number = input("Enter a number: ")

if number.isdigit():
    number_list = list(number)
    number_list.reverse()
    reversed_number = ''.join(number_list)
    print("Reversed number:", reversed_number)
else:
    print(":(")
