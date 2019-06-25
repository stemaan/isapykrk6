# importujemy nasz kod, ktory sami napisalismy!

# import fun7
from fun7 import odwroc

fraza = input("Podaj wyrażenie: ")

# tu wykorzystujemy nasza funkcje odwroc!
if fraza == odwroc(fraza):
    print("{} jest palindromem".format(fraza))
else:
    print("{} nie jest palindromem".format(fraza))

