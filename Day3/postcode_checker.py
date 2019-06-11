post_code = input('Podaj kod pocztowy: ')

post_code_splitted = post_code.split('-')

if post_code_splitted[0].isdigit() and post_code_splitted[1].isdigit():
    print('Kod pocztowy jest poprawny')
else:
    print('Kod pocztowy jest niepoprawny')

if post_code[:2].isdigit() and post_code[3:].isdigit():
    print('Kod pocztowy jest poprawny')
else:
    print('Kod pocztowy jest niepoprawny')