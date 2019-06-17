import string

letters_counter = 0
numbers_counter = 0

text = ';akdjfnwpur9h230[9rjqoifnb  GH240[39    P4NTPIU34T34890[J'

for element in text:
    if element in string.ascii_letters:
        letters_counter += 1
    elif element in string.digits:
        numbers_counter += 1

print(letters_counter)
print(numbers_counter)