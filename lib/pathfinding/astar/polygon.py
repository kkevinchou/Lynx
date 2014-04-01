from lib.vec2d import Vec2d

class Polygon(object):
    def __init__(self):
        self.points = []

    def get_points(self):
        return self.points

    def add_point(self, x, y):
        self.points.append(Vec2d(x, y))

    def get_edges(self):
        num_points = len(self.points)
        return [[self.points[i], self.points[(i + 1) % num_points]] for i in range(num_points)]
