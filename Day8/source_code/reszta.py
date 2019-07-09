# do debugowania
from math import floor

monety =        [5, 2, 1, 0.5, 0.2, 0.1]
monety_reszta = [0, 0, 0,   0,   0,   0]

banknot = 20
zakup = 8.30
reszta =  round(banknot - zakup, 2)
print(reszta)

# print(reszta)
indeks_mon_reszta = 0

for moneta in monety:
    if reszta >= moneta:
        ilosc =  reszta // moneta

        wartosc = ilosc * moneta
        reszta = round(reszta - wartosc, 2)
        print("Moneta {} ilość {}".format(moneta, ilosc))
        print("reszta: {}".format(reszta))
        monety_reszta[indeks_mon_reszta] = ilosc

    indeks_mon_reszta += 1

print("Reszta do wydania:")

for (moneta, ilosc) in zip(monety, monety_reszta):
    if ilosc > 0:
        print("Moneta {:>3} - {} szt.".format(moneta, int(ilosc)))
