from lib.vec2d import Vec2d
import lib

class Node(object):
    def __init__(self, x_or_pair, y = None):
        if y is None:
            self.x = x_or_pair[0]
            self.y = x_or_pair[1]
        else:
            self.x = x_or_pair
            self.y = y
            
        self.neighbors = []

    def point(self):
        return Vec2d(self.x, self.y)

    def __eq__(self, other):
        if isinstance(other, Node):
            return self.x == other.x and self.y == other.y

        return False

    def __repr__(self):
        return '<{} ({}, {})>'.format(hex(id(self)), self.x, self.y)
