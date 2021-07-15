import re

nombre1 = "Carmen López"
nombre2 = "Juan Diáz"
nombre3 = "Sandra Martín"

print(re.match("Sandra", nombre3))
print(re.match("Martín", nombre3))  # no lo encuentra porque busca al PRINCIPIO
print(re.search("Martín", nombre3))  # si lo encuentra porque busca en TODO


# sssssssssssssssssss
