while True:
    meters = input("Meters: ")
    try:
        meters = int(float(meters))
        print('Dm:', meters / 0.1)
        print('Cm:', meters / 0.01)
        print('Mm:', meters / 0.001)
        print('Miles: ', meters / 1609.34)
        break
    except ValueError:
        meters = float(meters)
        print('Dm:', meters / 0.1)
        print('Cm:', meters / 0.01)
        print('Mm:', meters / 0.001)
        print('Miles: ', meters / 1609.34)
        break

# meters = int(input('Meters: '))
# print('Dm:', meters / 0.1)
# print('Cm:', meters / 0.01)
# print('Mm:', meters / 0.001)
# print('Miles: ', meters / 1609.34)