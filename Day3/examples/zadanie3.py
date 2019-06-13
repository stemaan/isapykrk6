#  sprawdź czy jest wygrana w kółko i krzyżyk
#   input: string 9 znaków x, o, n
#   znaki oznaczają pozycje wierszami od gornego

# sprawdzamy czy długość inputu = 9

gra = "xonoxoxox"

# sprawdzimy czy wygrane po przekątnych
if gra[0] == gra[4] == gra[8] or gra[2] == gra[4] == gra[6]:
    if gra[4] != "n":
        print("Wygrał {}".format(gra[4]))
elif gra[0] == gra[1] == gra[2]:
    if gra[0]!="n":
        print("Wygrał {}".format(gra[0]))
elif gra[3] == gra[4] == gra[5]:
    if gra[3]!="n":
        print("Wygrał {}".format(gra[0]))
elif gra[6] == gra[7] == gra[8]:
    if gra[6]!="n":
        print("Wygrał {}".format(gra[0]))

