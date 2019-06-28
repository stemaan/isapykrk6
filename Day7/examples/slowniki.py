
slownik = { 'klucz':'wartosc', 0:'wartosc klucza zero' }

print(len(slownik))

print(slownik[0])
print(slownik)

print(slownik.items())

for klucz, wartosc in slownik.items():
    print("klucz: {}, warotsc: {}".format(klucz, wartosc))

for klucz in slownik.keys():
    print(klucz)

for wartosc in slownik.values():
    print(wartosc)

# tak dodajemy parę klucz:wartość do słownika
slownik.update({'telefon':'3434-3434-32'})
print(slownik)

# usuwamy klucz
klucz = 'klucz'
if klucz in slownik:
    slownik.pop(klucz)
print(slownik)