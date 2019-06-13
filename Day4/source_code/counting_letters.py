magic = 'abracadabra'
counter = 0
char_to_count = 'a'

for char in magic:
    if char == char_to_count:
        counter += 1

print(f'Liczba wystapien znaku {char_to_count} wynosi: {counter}')
