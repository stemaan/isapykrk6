# wypisz liczby od 1 do 100 (wlacznie)
# jesli podzielna przez 3 to napisz Fizz
# jesli podzilena przez 5 to napisz Buzz
# jesli podzielna przez 3 i przez 5 to napisz FizzBuzz

# licznik
i = 1

# petla
# dopoki liczby mniejsze rowne 100:
while i <= 100:
    # jesli licznik podzielna przez 15
    if i % 15 == 0:
        #napisz FizzBuzz
        print("FizzBuzz")
    # jesli licznik podzielna przez 3
    elif i % 3 == 0:
        # napisz Fizz
        print("Fizz")
    # jesli licznik podzielna przez 5
    elif i % 5 == 0:
        # napisz Buzz
        print("Buzz")
    # w innym przypadku
    else:
        # wypisz wartosc licznika
        print(i)
    # update licznika
    i += 1
