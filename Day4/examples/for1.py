# x = range(5)
#
# for i in x:
#     print(i)

# for c in "Anna":
#     print(c)

# magic = "abracadabra"
# for i in range(len(magic)):
#     print(i, magic[i])

# i = 0
# for c in magic:
#     print(i, c.upper())
#     i += 1


name = "janina"
upper_name = ""

# i = 0
#
# for c in name:
#     if i % 2 ==0:
#         upper_name += c.upper()
#     else:
#         upper_name += c
#
#     i += 1
#
# print(upper_name)

for i in range(len(name)):
    if i % 2 == 0:
        upper_name += name[i].upper()
    else:
        upper_name += name[i]

print(upper_name)


