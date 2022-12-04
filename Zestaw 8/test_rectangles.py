from rectangles import Rectangle
from points import Point
import pytest

def test_center():
    assert Rectangle(0, 0, 4, 4).center == Point(2, 2)
    assert Rectangle(1, 1, 4, 4).center == Point(2.5, 2.5)

def test_from_points():
    assert str(Rectangle.from_points((Point(0, 0), Point(3, 3)))) == '[(0, 0), (3, 3)]'
    assert str(Rectangle.from_points((Point(1, 3), Point(3, 5)))) == '[(1, 3), (3, 5)]'

def test_number_coordinates():
    rectangle = Rectangle(0, 0, 3, 5)
    rectangle2 = Rectangle(1, 3, 5, 5)

    assert rectangle.top == 5
    assert rectangle.right == 3
    assert rectangle.bottom == 0
    assert rectangle.left == 0
    assert rectangle.width == 3
    assert rectangle.height == 5

    assert rectangle2.top == 5
    assert rectangle2.right == 5
    assert rectangle2.bottom == 3
    assert rectangle2.left == 1
    assert rectangle2.width == 4
    assert rectangle2.height == 2

def test_attributes_points():
    rectangle = Rectangle.from_points((Point(1, 1), Point(4, 5)))
    rectangle2 = Rectangle.from_points((Point(2, 3), Point(6, 6)))

    assert rectangle.topleft == Point(1, 5)
    assert rectangle.topright == Point(4, 5)
    assert rectangle.bottomleft == Point(1, 1)
    assert rectangle.bottomright == Point(4, 1)

    assert rectangle2.topleft == Point(2, 6)
    assert rectangle2.topright == Point(6, 6)
    assert rectangle2.bottomleft == Point(2, 3)
    assert rectangle2.bottomright == Point(6, 3)

if __name__ == "__main__":
    pytest.main()