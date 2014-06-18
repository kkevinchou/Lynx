from lib.vec2d import Vec2d
from lib.geometry.util import generate_convex_hull, copy_points_list

class Polygon(object):
    def __init__(self, points=None):
        if points is None:
            points = []

        self.points = points

        if len(self.points) != len(set(self.points)):
            raise Exception('Points in Polygon must be distinct')

    def get_points(self):
        return copy_points_list(self.points)

    def add_point(self, x, y):
        new_point = Vec2d(x, y)

        if new_point in self.points:
            raise Exception('Points in Polygon must be distinct')

        self.points.append(new_point)

    def add_points(self, points):
        self.points.extend(copy_points_list(points))

        if len(self.points) != len(set(self.points)):
            raise Exception('Points in Polygon must be distinct')

    def contains_point(self, point):
        num_points = len(self.points)

        for i in range(num_points):
            current_point = self.points[i]
            next_point = self.points[(i + 1) % num_points]
            polygon_vec = next_point - current_point
            point_vec = point - current_point

            print polygon_vec.cross(point_vec)

            if polygon_vec.cross(point_vec) >= 0:
                return False

        return True

    def get_edges(self):
        num_points = len(self.points)
        return [[self.points[i].copy(), self.points[(i + 1) % num_points].copy()] for i in range(num_points)]

    @staticmethod
    def rectangular_polygon(width, height):
        points = [
            Vec2d(0, 0),
            Vec2d(0, height),
            Vec2d(width, height),
            Vec2d(width, 0)
        ]
        return Polygon(points)
