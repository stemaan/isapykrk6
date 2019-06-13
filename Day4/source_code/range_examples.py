# # przyklad nr 1, gdzie podana jest tylko wartosc koncowa
# for element in range(10):
#     print(element)
#
# # przyklad nr 2, podana wartosc poczatkowa i koncowa
# for element in range(15, 46):
#     print(element)
#
# #przyklad nr 3, wartosc poczatkowa, koncowa i krok
# for element in range(1, 101, 7):
#     print(element)
#
# TODO: raymond hettinger pythonic code!
# for element in range(1, 11):
#     if not element % 2:
#         print(element)
#

# TODO: pobierz od uzytkownika dwie wartosci
# TODO: poczatek ciagu liczbowego i koniec
# TODO: wyswietl wszystkie liczby z tego zakresu
start_value = int(input('Podaj wartosc poczatkowa: '))
stop_value = int(input('Podaj wartosc koncowa: '))

series = range(start_value, stop_value)
result = sum(series)
print(result)
# alternative, non pythonic!
total = 0
for value in series:
    total += value
print(result == total)