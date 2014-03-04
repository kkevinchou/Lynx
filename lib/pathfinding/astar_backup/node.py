import numpy

class Node(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.neighbors = []

    def point(self):
        return numpy.array([self.x, self.y])

    def __eq__(self, other):
        if isinstance(other, Node):
            return self.x == other.x and self.y == other.y

        return False

    def __repr__(self):
        return '<{} ({}, {})>'.format(hex(id(self)), self.x, self.y)
