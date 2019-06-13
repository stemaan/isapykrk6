# sprawdź czy liczba jest podzielna przez 3 , 5, 7
# przyjmij dane
dane = str(input("Podaj liczbe: "))

# sprawdzamy czy zawiera tylko cyfry
if dane.isdigit() and int(dane) != 0:
#if dane.isdigit():
    liczba = int(dane)

    # sprawdzamy czy podzielna przez 3
    if liczba % 3 == 0:
        # napisz ze podzielna
        print("Liczba {} jest podzielna przez 3".format(liczba))
    #sprawdzamy czy jest podzielna przez 5
    if liczba % 5 == 0:
        # napisz ze jest podzielna
        print("Liczba {} jest podzielna przez 5".format(liczba))
    #sprawdzamy czy jest podzielna przez 7
    if liczba % 7 == 0:
        # napisz ze podzielna przez 7
        print("Liczba {} jest podzielna przez 7".format(liczba))


