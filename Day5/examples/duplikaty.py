# zwroc liste bez duplikatow

lista = [10, 20, 30, 20, 10, 50, 60, 40, 80, 50, 40]

lista_bez_duplikat = []

for element in lista:
    if element not in lista_bez_duplikat:
        lista_bez_duplikat.append(element)

print(lista_bez_duplikat)

