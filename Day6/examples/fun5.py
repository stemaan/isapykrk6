# ta zmienna imie jest w zakresie globalnym
imie = "ola"

# argument domyslny jest typem wartosciowym
def duza_litera(imie="ala"):
    # ta zmienna imie jest tylko w zakresie funkcji
    imie = imie.capitalize()
    return imie

print(duza_litera())
print(imie)


