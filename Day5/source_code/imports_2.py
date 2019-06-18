from string import ascii_letters, digits

# it is possible to rename import using following syntax
# from string import ascii_letters as imported_ascii

letters_counter = 0
numbers_counter = 0
# ascii_letters = 'jansdkjnaskjdn'

text = ';akdjfnwpur9h230[9rjqoifnb  GH240[39    P4NTPIU34T34890[J'

for element in text:
    if element in ascii_letters:
        letters_counter += 1
    elif element in digits:
        numbers_counter += 1

print(letters_counter)
print(numbers_counter)