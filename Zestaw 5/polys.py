def equal_poly_len(poly1, poly2):
    if len(poly1) != len(poly2):
        while len(poly1) > len(poly2):
            poly2.insert(0, 0)

        while len(poly1) < len(poly2):
            poly1.insert(0, 0)

def add_poly(poly1, poly2):        # poly1(x) + poly2(x)
    suma = [0 for _ in range(max(len(poly1), len(poly2)))]

    equal_poly_len(poly1, poly2)

    for i in range(len(poly1) - 1, -1, -1):
        suma[i] += poly1[i]

    for j in range(len(poly2) -1, -1, -1):
        suma[j] += poly2[j]

    return suma

def sub_poly(poly1, poly2):        # poly1(x) - poly2(x)
    suma = [0 for _ in range(max(len(poly1), len(poly2)))]

    equal_poly_len(poly1, poly2)

    for i in range(len(poly1)):
        suma[i] += poly1[i]

    for j in range(len(poly2)):
        suma[j] -= poly2[j]

    return suma

def mul_poly(poly1, poly2):        # poly1(x) * poly2(x)
    suma = [0 for _ in range(len(poly1) + len(poly2) - 1)]

    for i in range(len(poly1)):
        for j in range(len(poly2)):
            suma[i + j] += poly1[i] * poly2[j]

    return suma

def is_zero(poly):                 # bool, [0], [0,0], itp.
    for i in range(len(poly)):
        if poly[i] != 0:
            return False
    return True


def eq_poly(poly1, poly2):        # bool, porównywanie poly1(x) == poly2(x) rowne czy nie rowne
    for i in range(max(len(poly1), len(poly2))):

        equal_poly_len(poly1, poly2)

        if poly1[i] != poly2[i]:
            return False

    return True

def eval_poly(poly, x0):           # poly(x0), algorytm Hornera wartosc wielomianu dla danego x
    result = poly[0]

    for i in range(1, len(poly)):
        result = result * x0 + poly[i]

    return result


def pow_poly(poly, n):             # poly(x) ** n
    result = poly
    if n == 0:
        return [1]
    else:
        for i in range(n-1):
            result = mul_poly(result, poly)

    return result

def combine_poly(poly1, poly2):  # poly1(poly2(x)), trudne! wielomian od wielomianu, zlozenie wielomianow, pod x
    # ustawiamy caly drugi wielomian
    poly22 = []
    result = [0]

    loopHelp = len(poly1)
    for i,j in zip(range(loopHelp), range(loopHelp - 1, -1, -1)):
        if j == 0:
            poly22.append(poly1[i])
        else:
            for element in list(pow_poly(poly2, j)):
                poly22.append(element * poly1[i])

        equal_poly_len(result, poly22)

        result = add_poly(result, poly22)
        poly22.clear()
    return result


def diff_poly(poly):               # pochodna wielomianu
    result = []
    loopHelp = len(poly)
    for i, j in zip(range(loopHelp), range(loopHelp - 1, -1, -1)):
        if j == 0:
            break
        result.append(poly[i] * j)

    return result

p1 = [-3, 0, 1, 2]
p2 = [1, 0, -3, 11]
p3 = add_poly(p1, p2)
p4 = sub_poly(p1, p2)
p5 = mul_poly(p1, p2)
p6 = [0, 2, 1]
p7 = [2, 1]
print(p3, p4, p5, is_zero(p6), eq_poly(p6, p7), eval_poly(p2, 2), diff_poly([7, 0, 3, -1, 3]))

# # 3x^2 + 2x - 1 = 3 * (2x - 1)^2 + 2 (2x - 1) - 1 = 3 * (4x^2 - 4x + 1) + 4x - 2 - 1 = 12x^2 - 12x + 3 +4x - 2 - 1 = 12x^2 - 8x
# # x = 2x - 1
#
pp = [3, 2, -1]
po = [2, -1]
print(combine_poly(pp, po))