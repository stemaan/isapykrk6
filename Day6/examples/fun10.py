# jesli mamy typ referencyjny w argumencie domyslnym
# to tworzmy go w ten sposob
# uzywamy slowo None aby okreslic, ze zmienna jest na
# poczatku pusta, nastepnie wew. funkcji sprawdzamy czy jest None
# jesli tak to wtedy tworzymy nowa liste i przypisujemy
# do zmiennej
def dodaj_imie(imie, imiona=None):
    if imiona is None:
        imiona = []
    imiona.append(imie)
    return imiona

print(dodaj_imie("ola"))
print(dodaj_imie("ala"))

# zobacz na pythontutor.com jak to dziala w porownaniu
# do poprzedniej wersji

