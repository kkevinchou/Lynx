from lib.vec2d import Vec2d
from lib.geometry.util import generate_convex_hull

class Polygon(object):
    def __init__(self, points=None):
        if points is None:
            points = []

        self.points = points

    def get_points(self):
        return self.points

    def add_point(self, x, y):
        self.points.append(Vec2d(x, y))

    def add_points(self, points):
        self.points.extend(points)

    def get_edges(self):
        num_points = len(self.points)
        return [[self.points[i], self.points[(i + 1) % num_points]] for i in range(num_points)]

    def compute_c_polygon(self, agent):
        agent_points = agent.get_points()

        all_points = []
        for point in self.points:
            for agent_point in agent_points:
                all_points.append(point - agent_point)

        c_polygon_points = generate_convex_hull(all_points)
        return Polygon(c_polygon_points)

