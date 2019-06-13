magic = 'abra1cadabra'
vowels_counter = 0
consonants_counter = 0
vowels = 'a'
consonants = 'brcd'

for char in magic:
    if char in vowels:
        vowels_counter += 1
    elif char in consonants:
        consonants_counter += 1
    else:
        continue
    print('char', char)

print('Ilosc samoglosek', vowels_counter)
print('Ilosc spolglosek', consonants_counter)