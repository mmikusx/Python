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