full_name = 'jan kowalski'

# NAMESPACE
def print_name(name):
    ful_name = name.capitalize()
    # print(name_capitalized)
    print(full_name)
    print(locals())
    print(globals())


print(full_name)
# ERROR!
# print(name_capitalized)
print_name('adam')
print(locals())
