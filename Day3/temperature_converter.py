data = input('Podaj wartość temperatury: ')

value = data[0:-1]
unit = data[-1]

if value.isdigit():
    value_converted = int(value)

    if unit.upper() == 'C':
        value_fahrenheit = value_converted * (9 / 5) + 32
        print(f'Wartość temperatury: {value_converted}C w Fahrenheitach wynosi: {value_fahrenheit}')
    elif unit.upper() == 'F':
        value_celsius = (value_converted - 32) * (5 / 9)
        print(f'Wartość temperatury: {value_converted}F w Celsjuszach wynosi: {value_celsius}')
    else:
        print('Podaj wartośćw w Celsjuszasch lub Fahrenheitach')
else:
    print('Podaj poprawną watość!')