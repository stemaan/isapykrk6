lista = [34, 56, 78, 98, 45,453,343,35462,2,245,45,245]

# pamietamy, ze funkcje musimy najpierw zdefinionwac
def czy_w_zakresie(liczba, zakres=range(1000)):
    if liczba in zakres:
        print(liczba, "yes")
    else:
        print(liczba, "no")

# a dopiero potem uzywac
for element in lista:
    czy_w_zakresie(element)

# i znowu uzywac - to jest re-uzywalnosc kodu :)
czy_w_zakresie(3476)


