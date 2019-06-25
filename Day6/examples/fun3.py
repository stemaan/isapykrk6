# mozemy miec kilka argumentow wymaganych oraz kilka domyslnych
# argumenty domyslne musza byc po wymaganych
def wypisz_dane(imie, nazwisko, kurs="Python", ilosc_dni=15):
    print(imie, nazwisko, kurs, ilosc_dni)

# argumenty wymagane (in. pozycyjne) musza byc podane
wypisz_dane("Arek", "G")

# tutaj podajemy wszystkie wartosci argumentow
wypisz_dane("jan", "kowalski", "Java", 80)

# kolejnosc argumentow mozna zmieniac, ale trzeba uzyc nazw zmiennych
wypisz_dane("gosia", "nowak", ilosc_dni=30, kurs="JavaScript")
wypisz_dane(kurs="Java", imie="gosia", ilosc_dni=23, nazwisko="kowal")