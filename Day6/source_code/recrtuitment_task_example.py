# the bad
# def foo(value, my_list=[]):
#     my_list.append(value)
#     print(my_list)

# good
def foo(value, my_list=None):
    if my_list is None:
        my_list = []
    my_list.append(value)
    print(my_list)


foo(1)
foo(2, [3, 4])
foo(5, [])
foo(8, [1])
foo(10)
