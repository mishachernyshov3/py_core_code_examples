# Створити класи точки та координатної площини. Перевизначити магічні методи.

class Point2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f'Point2D({self.x}, {self.y})'

    def __str__(self):
        return f'Point2D with x={self.x}, y={self.y}'

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y


class CoordinatesPlane2D:
    def __init__(self):
        self.points = {}

    def __getitem__(self, coordinates):
        x, y = coordinates
        if (x, y) not in self.points:
            self.points[(x, y)] = Point2D(x, y)
        return self.points[(x, y)]

    def __setitem__(self, coordinates_tuple, point):
        x, y = coordinates_tuple
        if point.x != x or point.y != y:
            raise ValueError('Wrong coordinates')
        self.points[(x, y)] = point


point_3_5 = Point2D(3, 5)
print(repr(point_3_5))
print(str(point_3_5))
print(eval(repr(Point2D(3, 5))))

coord_plane = CoordinatesPlane2D()
a = Point2D(3, 4)
b = Point2D(3, 4)
print(a == b)
print(a is b)
