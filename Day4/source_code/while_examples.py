# TODO: pobierz od uzytkownika dowolna calkowita liczbe
# TODO: nie trzeba sprawdzac czy string zawiera liczbe

value = int(input('Podaj liczbe: '))

counter = 0
iteration_no = 0

while counter < value:
    iteration_no += 1
    print('Python', iteration_no)
    if iteration_no == 100:
        break