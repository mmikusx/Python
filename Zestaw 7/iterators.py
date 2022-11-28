# Stworzyć następujące iteratory nieskończone:
# (a) zwracający 0, 1, 0, 1, 0, 1, ...,
# (b) zwracający przypadkowo jedną wartość z ("N", "E", "S", "W") [błądzenie przypadkowe na sieci kwadratowej 2D],
# (c) zwracający 0, 1, 2, 3, 4, 5, 6, 0, 1, 2, 3, 4, 5, 6, ... [numery dni tygodnia].

import itertools
import random

a = itertools.cycle('01')

b = (random.choice(('N', 'E', 'S', 'W')) for _ in iter(int, 1))

c = itertools.cycle('0123456')

result_a = ''
result_b = ''
result_c = ''
for i in range(25):
    result_a += f'{(next(a))}, '
    result_b += f'{next(b)}, '
    result_c += f'{next(c)}, '

print('a)', result_a)
print('b)', result_b)
print('c)', result_c)