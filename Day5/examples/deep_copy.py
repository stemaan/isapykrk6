# co jeśli mamy listę w liście i ją skopiujemy
# copy() , list() oraz [:] są kopiami płytkimi
# zakupy
import copy

nabial = ["mleko", "jajka", "ser"]
chemia = ["domestos", "plyn do naczyn"]

zakupy_styczen = [nabial, chemia]
print(zakupy_styczen)

zakupy_luty = copy.deepcopy(zakupy_styczen)
print(zakupy_luty)

zakupy_styczen.append("gabka")
print(zakupy_styczen)
print(zakupy_luty)