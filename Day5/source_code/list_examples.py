start = int(input('Podaj start: '))
end = int(input('Podaj stop: '))

my_list = list(range(start, end))

index = int(input('Podaj indeks: '))

print(my_list[index])

value = int(input('Podaj poszukiwana wartosc: '))
found = False

for element in my_list:
    if element == value:
        print('Znaleziono:', value)
        found = True
        break

if not found:
    print('Nie zaleziono', value)