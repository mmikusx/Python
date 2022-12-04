from points import Point
import unittest


class Rectangle:
    """Klasa reprezentująca prostokąt na płaszczyźnie."""

    def __init__(self, x1, y1, x2, y2):
        if x1 >= x2 or y1 >= y2:
            raise ValueError("x2 and y2 must be greater than x1 and y1")
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

    @property
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

    def intersection(self, other): # czesc wspolna prostokatow
        if isinstance(other, Rectangle):
            x1 = max(self.pt1.x, other.pt1.x)
            y1 = max(self.pt1.y, other.pt1.y)
            x2 = min(self.pt2.x, other.pt2.x)
            y2 = min(self.pt2.y, other.pt2.y)

            if x1 >= x2 or y1 >= y2:
                raise ValueError("x2 and y2 must be greater than x1 and y1")

            return Rectangle(x1, y1, x2, y2)
        else:
            raise ValueError("Other must be rectangle object")

    def cover(self, other): # prostokat nakrywajacy oba
        if isinstance(other, Rectangle):
            min_pt1_x = min(self.pt1.x, other.pt1.x)
            min_pt1_y = min(self.pt1.y, other.pt1.y)
            max_pt2_x = max(self.pt2.x, other.pt2.x)
            max_pt2_y = max(self.pt2.y, other.pt2.y)

            return Rectangle(min_pt1_x, min_pt1_y, max_pt2_x, max_pt2_y)
        else:
            raise ValueError("Other must be rectangle object")

    def make4(self): # zwraca krotke czterech mniejszych
        centerPoint = self.center()

        # (x1, y2) ----------- (center_x, y2) ----------- (x2, y2)
        # |                         |                            |
        # |                         |                            |
        # (x1, center_y) -- (center_x, center_y) -- (x2, center_y)
        # |                         |                            |
        # |                         |                            |
        # (x1, y1) ----------- (center_x, y1) ----------- (x2, y1)

        return (
            Rectangle(self.pt1.x, self.pt1.y, centerPoint.x, centerPoint.y),
            Rectangle(centerPoint.x, self.pt1.y, self.pt2.x, centerPoint.y),
            Rectangle(centerPoint.x, centerPoint.y, self.pt2.x, self.pt2.y),
            Rectangle(self.pt1.x, centerPoint.y, centerPoint.x, self.pt2.y)
        )

    @classmethod
    def from_points(cls, points):
        if isinstance(points, (list, tuple)):
            if len(points) != 2:
                raise ValueError("Arguments must be 2 lists/tuples")
            point1 = points[0]
            point2 = points[1]

        if not isinstance(point1, Point) or not isinstance(point2, Point):
            raise ValueError("Arguments must be points!")

        return cls(point1.x, point1.y, point2.x, point2.y)

    @property
    def top(self):
        return self.pt2.y

    @property
    def right(self):
        return self.pt2.x

    @property
    def bottom(self):
        return self.pt1.y

    @property
    def left(self):
        return self.pt1.x

    @property
    def width(self):
        return self.pt2.x - self.pt1.x

    @property
    def height(self):
        return self.pt2.y - self.pt1.y

    @property
    def topleft(self):
        return Point(self.pt1.x, self.pt2.y)

    @property
    def topright(self):
        return Point(self.pt2.x, self.pt2.y)

    @property
    def bottomleft(self):
        return Point(self.pt1.x, self.pt1.y)

    @property
    def bottomright(self):
        return Point(self.pt2.x, self.pt1.y)