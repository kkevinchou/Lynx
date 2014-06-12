from lib.vec2d import Vec2d
from lib.geometry.util import generate_convex_hull

class Polygon(object):
    def __init__(self, points=None):
        if points is None:
            points = []

        self.points = points

        if len(self.points) != len(set(self.points)):
            raise Exception('Points in Polygon must be distinct')

    def copy_points_list(self, points):
        return [point.copy() for point in points]

    def get_points(self):
        return self.copy_points_list(self.points)
        # return self.points

    def add_point(self, x, y):
        new_point = Vec2d(x, y)

        if new_point in self.points:
            raise Exception('Points in Polygon must be distinct')

        self.points.append(new_point)

    def add_points(self, points):
        self.points.extend(self.copy_points_list(points))

        if len(self.points) != len(set(self.points)):
            raise Exception('Points in Polygon must be distinct')

    def get_edges(self):
        num_points = len(self.points)
        return [[self.points[i].copy(), self.points[(i + 1) % num_points].copy()] for i in range(num_points)]

    def compute_c_polygon(self, agent):
        agent_points = self.copy_points_list(agent.get_points())

        all_points = []
        for point in self.points:
            for agent_point in agent_points:
                all_points.append(point - agent_point)

        c_polygon_points = generate_convex_hull(all_points)
        return Polygon(c_polygon_points)

    @staticmethod
    def rectangular_polygon(width, height):
        points = [
            Vec2d(0, 0),
            Vec2d(0, height),
            Vec2d(width, height),
            Vec2d(width, 0)
        ]
        return Polygon(points)
