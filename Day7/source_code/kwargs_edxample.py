def foo(*args, **kwargs):
    print(locals())


foo(1, 2)
foo(1, 5, some='value')
foo(argument=123)


def bar(x, *args, argument1=1, argument2='abc', **kwargs):
    print(locals())


bar(1)
bar(1, 2)
bar(10, argument2=123)
bar(x=99, y=100)
bar(99, y=100, argument2='asdasd', another_one='nasjdn 123123')
