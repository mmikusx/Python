class Point:
    """Klasa reprezentująca punkty na płaszczyźnie."""

    def __init__(self, x, y):  # konstuktor
        self.x = x
        self.y = y

    def __str__(self):         # zwraca string "(x, y)"
        result = f'({self.x}, {self.y})'

        return result

    def __repr__(self):        # zwraca string "Point(x, y)"
        result = f'Point({self.x}, {self.y})'

        return result

    def __eq__(self, other):   # obsługa point1 == point2
        if self.x == other.x and self.y == other.y:
            return True

        return False

    def __ne__(self, other):        # obsługa point1 != point2
        return not self == other

    # Punkty jako wektory 2D.
    def __add__(self, other):  # v1 + v2
        return Point(self.x + other.x, self.y + other.y)

    def __sub__(self, other):  # v1 - v2
        return Point(self.x - other.x, self.y - other.y)

    def __mul__(self, other):  # v1 * v2, iloczyn skalarny, zwraca liczbę
        return self.x * other.x + self.y * other.y

    def cross(self, other):         # v1 x v2, iloczyn wektorowy 2D, zwraca liczbę
        return self.x * other.y - self.y * other.x

    def length(self):          # długość wektora
        podPierwiastkiem = pow(self.x, 2) + pow(self.y, 2)
        return pow(podPierwiastkiem, 0.5)

    def __hash__(self):
        return hash((self.x, self.y))   # bazujemy na tuple, immutable points

# Kod testujący moduł.

import unittest

class TestPoint(unittest.TestCase):
    def setUp(self): pass

    def test_str(self):
        self.assertEqual(str(Point(1, 2)), '(1, 2)')
        self.assertEqual(str(Point(13, 31)), '(13, 31)')
        self.assertEqual(str(Point(1000, 0)), '(1000, 0)')
        self.assertEqual(str(Point(0, 1000)), '(0, 1000)')

    def test_repr(self):
        self.assertEqual(repr(Point(1, 2)), 'Point(1, 2)')
        self.assertEqual(repr(Point(13, 31)), 'Point(13, 31)')
        self.assertEqual(repr(Point(1000, 0)), 'Point(1000, 0)')
        self.assertEqual(repr(Point(0 ,1000)), 'Point(0, 1000)')

    def test_eq(self):
        self.assertEqual(Point(1, 2), Point(1, 2))
        self.assertEqual(Point(13, 31), Point(13, 31))
        self.assertEqual(Point(1000, 0), Point(1000, 0))

    def test_ne(self):
        self.assertNotEqual(Point(1, 2), Point(2, 1))
        self.assertNotEqual(Point(13, 31), Point(31, 13))
        self.assertNotEqual(Point(1000, 0), Point(0 ,1000))

    def test_add(self):
        self.assertEqual(Point(1, 2) + Point(1, 2), Point(2, 4))
        self.assertEqual(Point(13, 31) + Point(31, 13), Point(44, 44))
        self.assertEqual(Point(1000, 0) + Point(0, 1000), Point(1000, 1000))

    def test_sub(self):
        self.assertEqual(Point(1, 2) - Point(1, 2), Point(0, 0))
        self.assertEqual(Point(13, 31) - Point(13, 31), Point(0, 0))
        self.assertEqual(Point(1000, 0) - Point(543, 0), Point(457, 0))

    def test_mul(self):
        self.assertEqual(Point(1, 2) * Point(1, 2), 5)
        self.assertEqual(Point(13, 31) * Point(2, 3), 119)
        self.assertEqual(Point(1000, 0) * Point(1, 2), 1000)

    def test_cross(self):
        self.assertEqual(Point(1, 2).cross(Point(1, 2)), 0)
        self.assertEqual(Point(1, 2).cross(Point(13, 31)), 5)
        self.assertEqual(Point(13, 31).cross(Point(1000, 0)), -31000)

    def test_leng(self):
        self.assertEqual(Point(0, 4).length(), 4)
        self.assertEqual(Point(1, 1).length(), 1.4142135623730951)

    def test_hash(self):
        self.assertEqual(hash(Point(1, 1)), 8389048192121911274)
        self.assertEqual(hash(Point(1, 2)), -3550055125485641917)

    def tearDown(self): pass

if __name__ == "__main__":
    unittest.main()     # wszystkie testy