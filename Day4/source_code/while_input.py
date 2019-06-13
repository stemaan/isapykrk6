user_input = input('Podaj liczbe calkowita: ')

while not user_input.isdigit():
    print('podales niepoprawne dane wejsciowe')
    user_input = input('Podaj liczbe calkowita: ')

input_as_int = int(user_input)
if input_as_int % 2:
    print(input_as_int, 'jest nieparzyste')
else:
    print(input_as_int, 'jest parzyste')
