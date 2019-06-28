# # TODO: zlicz wystąpienia każdego znaku wystepującego w tekscie
# # TODO: jedna linia = jeden znak/slowo
#
# # TODO: otworz plik w trybie do odczytu
# # TODO: przeczytaj plik, linia po linii
# # TODO: ? algorytm ? jak zliczyc wystapienia danego slowa/znaku w tekscie?
# # TODO: jezeli klucz istnieje w slowniku - zwieksz liczbe wystapien o 1
# # TODO: w przeciwnym przypadku dany ciag znaku pojawia sie po raz pierwszy
#
# counter = {}
#
#
# with open('random_words.txt', 'r') as random_words_file:
#     for line in random_words_file:
#         word = line.strip()
#         if word in counter:
#             counter[word] += 1
#         else:
#             counter[word] = 1
#
# for key in counter:
#     print(key.strip(), counter[key])


from collections import Counter

with open('random_words.txt', 'r') as random_words_file:
    lines = [line.strip() for line in random_words_file]
    print(Counter(lines))
