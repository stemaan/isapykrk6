start = int(input('Podaj start: '))
end = int(input('Podaj stop: '))

my_list = list(range(start, end))

value = int(input('Podaj poszukiwana wartosc: '))

for element in my_list:
    if element == value:
        print('Znaleziono:', value)
        break
else:
    print('Kiedy to sie wyswietli?')

