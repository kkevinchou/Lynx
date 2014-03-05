from astarplanner import AStarPlanner
from polygon import Polygon
from lib.vec2d import Vec2d
from lib.pathfinding.astar.node import Node

from util import (
    intersect_polygon,
    line_intersect,
    create_line_segment,
    shares_point,
    colinear,
)

def basic_intersection_test():
    poly = Polygon()
    poly.add_point(0, 0)
    poly.add_point(0, 1)
    poly.add_point(-1, 1)
    poly.add_point(-1, 0)

    line = [Vec2d(0.5, -0.5), Vec2d(-0.5, 0.5)]
    assert(intersect_polygon(line, poly) == True)

    line = [Vec2d(1, -1), Vec2d(1, 0)]
    assert(intersect_polygon(line, poly) == False)

def line_intersection_test():
    a = Vec2d(1, 0)
    b = Vec2d(1, 1)
    c = Vec2d(0, 1)
    d = Vec2d(0, 0)

    line_a = [a, b]
    line_b = [b, c]
    line_c = [c, d]
    line_d = [d, a]

    assert(line_intersect(line_a, line_b) == True)

def border_non_intersect_test():
    polygon = Polygon()
    polygon.add_point(0, 0)
    polygon.add_point(0, 1)
    polygon.add_point(-1, 1)
    polygon.add_point(-1, 0)

    line1 = [Vec2d(0, 0), Vec2d(-1, 0)]
    line2 = [Vec2d(0, 1), Vec2d(0, 0)]

    assert(intersect_polygon(line1, polygon) == False)

def shares_point_test():
    a = Vec2d(1, 0)
    b = Vec2d(1, 1)
    c = Vec2d(0, 1)
    d = Vec2d(0, 0)

    line_a = [a, b]
    line_b = [b, c]
    line_c = [c, d]

    assert(shares_point(line_a, line_b) == True)
    assert(shares_point(line_a, line_c) == False)

def colinear_test():
    base = Vec2d(0, 0)
    assert(colinear([base, Vec2d(1, 0)], [base, Vec2d(0, 1)]) == False)
    assert(colinear([base, Vec2d(1, 0)], [base, Vec2d(0, -1)]) == False)
    assert(colinear([base, Vec2d(1, 0)], [base, Vec2d(-1, 0)]) == True)
    assert(colinear([base, Vec2d(1, 0)], [base, Vec2d(1, 0)]) == True)

def basic_path_test():
    poly1 = Polygon()
    poly1.add_point(0, 0)
    poly1.add_point(0, 1)
    poly1.add_point(-1, 1)
    poly1.add_point(-1, 0)

    # poly2 = Polygon()
    # poly2.add_point(101, 0)
    # poly2.add_point(101, 1)
    # poly2.add_point(100, 1)
    # poly2.add_point(100, 0)

    astarplanner = AStarPlanner()
    astarplanner.add_polygon(poly1)
    # astarplanner.add_polygon(poly2)

    print astarplanner.find_path(-1, -1, 1000, 1000)

if __name__ == '__main__':
    tests = [
        basic_intersection_test,
        line_intersection_test,
        border_non_intersect_test,
        basic_path_test,
        shares_point_test,
        colinear_test,
    ]

    for test in tests:
        test()

# poly2 = Polygon()
# poly2.add_point(100, 0)
# poly2.add_point(100, 1)
# poly2.add_point(101, 1)
# poly2.add_point(101, 0)

# planner.add_polygon(poly1)
# planner.add_polygon(poly2)

# planner.find_path(0, 0, 1, 1)

# b = [numpy.array([0, 0]), numpy.array([1, 1])]

# c = numpy.array([0, 1])
# d = numpy.array([1, 0])

# print numpy.array_equal(c, d)
# b = [numpy.array([0, 0]), numpy.array([1, 1])]
# print _compute_t_value(a, b)
