# W pliku rectangles.py zdefiniować klasę Rectangle wraz z potrzebnymi metodami. Prostokąt jest określony przez
# podanie dwóch wierzchołków, lewego dolnego i prawego górnego. Napisać kod testujący moduł rectangles.

from points import Point
import unittest


class Rectangle:
    """Klasa reprezentująca prostokąt na płaszczyźnie."""

    def __init__(self, x1, y1, x2, y2):
        self.pt1 = Point(x1, y1)
        self.pt2 = Point(x2, y2)

    def __str__(self):  # "[(x1, y1), (x2, y2)]"
        result = f'[{Point.__str__(self.pt1)}, {Point.__str__(self.pt2)}]'

        return result

    def __repr__(self):  # "Rectangle(x1, y1, x2, y2)"
        result = f'Rectangle({self.pt1.x}, {self.pt1.y}, {self.pt2.x}, {self.pt2.y})'

        return result

    def __eq__(self, other):  # obsługa rect1 == rect2
        if self.pt1.x == other.pt1.x and self.pt1.y == other.pt1.y and self.pt2.x == other.pt2.x and self.pt2.y == other.pt2.y:
            return True

        return False

    def __ne__(self, other):  # obsługa rect1 != rect2
        return not self == other

    def center(self):  # zwraca środek prostokąta
        delta_x = self.pt2.x - self.pt1.x
        center_x = delta_x / 2
        delta_y = self.pt2.y - self.pt1.y
        center_y = delta_y / 2

        return Point(center_x + self.pt1.x, center_y + self.pt1.y)

    def area(self):  # pole powierzchni
        width = self.pt2.x - self.pt1.x
        height = self.pt2.y - self.pt1.y

        return abs(width * height)

    def move(self, x, y):  # przesunięcie o (x, y)
        newRectangle = self
        newRectangle.pt1.x += x
        newRectangle.pt2.x += x
        newRectangle.pt1.y += y
        newRectangle.pt2.y += y

        return newRectangle


# Kod testujący moduł.

class TestRectangle(unittest.TestCase):
    def SetUp(self): pass

    def test_str(self):
        self.assertEqual(str(Rectangle(1, 2, 3, 4)), '[(1, 2), (3, 4)]')
        self.assertEqual(str(Rectangle(13, 31, 31, 13)), '[(13, 31), (31, 13)]')
        self.assertEqual(str(Rectangle(1000, 0, 0, 1000)), '[(1000, 0), (0, 1000)]')
        self.assertEqual(str(Rectangle(0, 1000, 1000, 0)), '[(0, 1000), (1000, 0)]')

    def test_repr(self):
        self.assertEqual(repr(Rectangle(1, 2, 3, 4)), 'Rectangle(1, 2, 3, 4)')
        self.assertEqual(repr(Rectangle(13, 31, 31, 13)), 'Rectangle(13, 31, 31, 13)')
        self.assertEqual(repr(Rectangle(1000, 0, 0, 1000)), 'Rectangle(1000, 0, 0, 1000)')
        self.assertEqual(repr(Rectangle(0, 1000, 1000, 0)), 'Rectangle(0, 1000, 1000, 0)')

    def test_eq(self):
        self.assertEqual(Rectangle(1, 2, 3, 4), Rectangle(1, 2, 3, 4))
        self.assertEqual(Rectangle(13, 31, 31, 13), Rectangle(13, 31, 31, 13))
        self.assertEqual(Rectangle(1000, 0, 0, 1000), Rectangle(1000, 0, 0, 1000))

    def test_ne(self):
        self.assertNotEqual(Rectangle(1, 2, 3, 4), Rectangle(13, 31, 31, 13))
        self.assertNotEqual(Rectangle(13, 31, 31, 13), Rectangle(1000, 0, 0, 1000))
        self.assertNotEqual(Rectangle(1000, 0, 0, 1000), Rectangle(0, 1000, 1000, 0))

    def test_center(self):
        self.assertEqual(Rectangle(1000, 0, 0, 1000).center(), Point(500, 500))
        self.assertEqual(Rectangle(0, 1000, 1000, 0).center(), Point(500, 500))
        self.assertEqual(Rectangle(1, 5, 5, 1).center(), Point(3, 3))

    def test_area(self):
        self.assertEqual(Rectangle(1, 2, 3, 4).area(), 4)
        self.assertEqual(Rectangle(0, 10, 10, 0).area(), 100)
        self.assertEqual(Rectangle(0, 20, 15, 0).area(), 300)

    def test_move(self):
        self.assertEqual(Rectangle(1, 2, 3, 4).move(2, 2), Rectangle(3, 4, 5, 6))
        self.assertEqual(Rectangle(13, 31, 31, 13).move(-10, -10), Rectangle(3, 21, 21, 3))
        self.assertEqual(Rectangle(1000, 0, 0, 1000).move(-999, -999), Rectangle(1, -999, -999, 1))

    def tearDown(self): pass


if __name__ == "__main__":
    unittest.main()  # wszystkie testy
