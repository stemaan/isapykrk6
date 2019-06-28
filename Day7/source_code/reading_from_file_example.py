phone_book = {
    'Kowalski': 'Jan',
    'Nowak': 'Anna',
    'Lalak': 'Przemyslaw'
}

with open('phone_book_data.txt', 'r') as phone_book_file:
    for line in phone_book_file:
        print(line)
