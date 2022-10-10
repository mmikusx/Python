# Na liście L znajdują się liczby całkowite dodatnie. Stworzyć napis będący ciągiem cyfr kolejnych liczb z listy L.

import random

L = random.sample(range(100), 12)

napis = ''

for element in L:
    lista = list(str(element))
    for elementy in lista:
        napis += elementy

print("Lista L z liczbami calkowitymi:", L)
print("Napis bedacy ciagiem liczb z listy L: " + napis)
