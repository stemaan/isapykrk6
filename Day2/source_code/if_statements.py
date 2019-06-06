# %
user_input = input('Podaj liczbe calkowita: ')
# user_input = int(user_input)

if user_input.isdigit():
    input_as_int = int(user_input)
    if input_as_int % 2:
        print(input_as_int, 'jest nieparzyste')
    else:
        print(input_as_int, 'jest parzyste')
else:
    print('podales niepoprawne dane wejsciowe')
