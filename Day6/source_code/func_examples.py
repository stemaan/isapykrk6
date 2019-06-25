def do_something(x, y, z=12, w='Ola'):
    print(x, y, z, w)
    print(locals())


# wywolania
do_something(1, 33)
do_something(1, 33, 65)
do_something(1, 33, w='65')


# ponizszy zapis jest bledny!
# do_something(x=64, 1, 33)

# *args przechowuje dowolna ilosc argumentow pozycyjnych
def foo(x, y, *args, some_text='asc', something='asd'):
    print(locals())


foo(1, 11)
foo(45, 99, some_text='ansdkjanskjdnas')
foo(87, 12, 43, 345, 'asd', 'ala ma kota', None, some_text='1223')
