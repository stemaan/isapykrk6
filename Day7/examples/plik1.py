# otwieram swoj plik
plik = open('c:\\day6\\moj_plik.txt')

# czytamy jedną linijkę z pliku
linijka = plik.readline()

print(linijka)

# pamietamy o zamykaniu pliku
plik.close()