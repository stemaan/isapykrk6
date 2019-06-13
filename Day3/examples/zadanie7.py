# zamiana temperatury
#     wejscie: "35C" "100F"
#     wyjście "Temperatura w {typ} to {xxx} stopni"
#     C = (F - 32) * (5/9)
#     F = C * (9 / 5) + 32

temp = str(input()).upper()
print(temp)

# sprawdzamy ostatni znak
# jesli C
if temp.endswith("C"):
    # obliczamy F
    cel = temp[0:-1]
    cel = int(cel)
    fahr = cel * (9 /5) + 32

    print("Temperatura w Fahrenheit to {} stopni".format(fahr))
#jesli F
elif temp.endswith("F"):
    #obliczmy C
    fahr = int(temp[0:-1])
    cel = (fahr - 32) * 5/9

    # wypisujemy
    print("Temperatura w Celsjusz to {} stopni".format(cel))
