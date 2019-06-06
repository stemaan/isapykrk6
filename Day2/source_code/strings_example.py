text = 'ala ma kota'

print(text.capitalize())

text_uppercased = text.upper()

print(text)
print(text_uppercased)

length = len(text)
message = 'Dlugosc tekstu to:'
print(message, length)
# TODO: wyswietl na ekranie tekst:
# TODO: 'pierwszy znak tekstu to: {znak}'

message = 'Pierwszy znak tekstu to:'
print(message, text[0])

# TODO: wyswietl na ekranie tekst:
# TODO: 'Ostatni znak tekstu to: {znak}'
message = 'Ostatni znak tekstu to:'
print(message, text[length-1])
