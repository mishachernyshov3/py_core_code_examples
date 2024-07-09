# Знайти відстань між 2 точками: A(12, 32) i B(-6, 4).
import math
from collections import namedtuple


Point = namedtuple('Point', ['x', 'y'])


def get_distance(p1: Point, p2: Point) -> float:
    return math.sqrt((p1.x - p2.x) ** 2 + (p1.y - p2.y) ** 2)


print(get_distance(Point(12, 32), Point(-6, 4)))
