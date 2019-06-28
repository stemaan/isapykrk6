from pprint import pprint

phone_book = {
    'Kowalski': 'Jan',
    'Nowak': 'Anna',
    'Lalak': 'Przemyslaw'
}

pprint(phone_book)

# wyluskanie wartosci klucza
last_name = phone_book['Kowalski']
print(last_name)

# dodanie nowego klucza do slownika
phone_book['Pythonowy'] = 'Python'

# iterowanie po slowniku (tylko klucze!)
for key in phone_book:
    # print(element)
    print(phone_book[key])

# iterowanie po slowniku (klucze i warosci)
for key, value in phone_book.items():
    print(key, value)

print(type(phone_book.items()))

print(phone_book)
phone_book['Lalak'] = 'Przemysław Adam'
print(phone_book)

phone_book_copy = phone_book.copy()
phone_book_copy['Nowak'] = 'Adam'
phone_book['Wick'] = 'John'

phone_book.update(phone_book_copy)
print(phone_book)

phone_book.update(Balboa='Rocky')
pprint(phone_book)

# usuwanie klucza ze slownika
popped_value = phone_book.pop('Lalak')
print(popped_value)

del phone_book['Nowak']

# phone_book['Creed']

print(phone_book.get('Wick'))
print(phone_book.get('Creed', 'Unkown'))

# tworzymy pusty slownik
# some_dict = {}  # dict()

# list_comp = [x for x in range(10)]

# dict comprehension
some_dict = {x: x ** 2 for x in range(10)}
pprint(some_dict)

# DON'T DO THIS!
# for key in some_dict:
#     if key % 2:
#         del some_dict[key]
# pprint(some_dict)


def foo(*args, **kwargs):
    print(locals())


foo(1, 2)
foo(1, 5, some='value')
foo(argument=123)


