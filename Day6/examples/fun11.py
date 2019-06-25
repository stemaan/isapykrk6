# wow w koncu bedziemy miec pomoc do funkcji!
# doc string zaczynamy i konczymy trzema apostrofami lub
# cudzyslowami

def kwadrat(liczba):
    ''' Zwraca kwadrat podanej liczby'''
    return liczba**2

print(kwadrat())

def pole_prostokat(a, b):
    """
    Oblicza i zwraca pole prostokata

    (double, double) -> double
    :param a: bok a
    :param b: bok b
    :return: Pole prostokata
    """
    return a*b


