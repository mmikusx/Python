# Na liście L mamy liczby jedno-, dwu- i trzycyfrowe dodatnie. Chcemy zbudować napis z trzycyfrowych bloków,
# gdzie liczby jedno- i dwucyfrowe będą miały blok dopełniony zerami, np. 007, 024. Wskazówka: str.zfill().
import random

L = random.sample(range(1, 9), 3)
L += random.sample(range(10, 99), 3)
L += random.sample(range(100, 999), 3)

napis = ''

for element in L:
    if element != L[-1]:
        napis += str(element).zfill(3) + ", "
    else:
        napis += str(element).zfill(3)

print(napis)