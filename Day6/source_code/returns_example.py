def add_numbers(*args):
    return sum(args)


def add(a, b):
    return a + b


numbers = [1, 2, 3, 4]
a = 2
b = 10

result = add_numbers(*numbers)
print(result)
result_simple = add(a, b)
print(result_simple)


def is_greater_than_zero(value):
    return value > 0

f = add_numbers
print(f)
print(f(*numbers))
