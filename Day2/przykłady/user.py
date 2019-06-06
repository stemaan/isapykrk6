imie = input("Podaj imie: ")

# w pythonie 3.6 można tak jak ponizej, ale tylko w 3.6 i kolejnych wersjach
print(f"Witaj {imie}!")

# nazwisko powinno byc z duzej
imie = imie.capitalize()
print("Witaj {}".format(imie))

# szukamy pierwszego wystapienia znaku
x = imie.find('A')
print(x)

# ------------------------
imie2 = 'anna'

# wszystko wydrukuje sie tak samo
print(f"Hello {imie2}")
print("Hello {}".format(imie2))
print("Hello " + imie2)





