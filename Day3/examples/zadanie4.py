# oblicz czy podany rok jest przestępny
# podzielny przez 4, nie podzielny przez 100 ale podzielny przez 400

rok = int(input("Podaj rok: "))

if rok % 400 == 0:
    print("Jest przestępny")
elif rok % 4 == 0 and rok % 100 != 0:
    print("Jest przestępny")
else:
    print("Nie jest przestępny")



