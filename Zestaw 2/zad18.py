# Znaleźć liczbę cyfr zero w dużej liczbie całkowitej. Wskazówka: zamienić liczbę na napis.

import random

cyfra = random.sample(range(10000000, 99999999), 3)
for element in cyfra:
    print("Liczba:", element)
    zera = 0
    for elements in list(str(element)):
        if elements == '0':
            zera += 1
    print("Ilosc zer w liczbie:", zera)