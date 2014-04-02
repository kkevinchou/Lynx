import random
import unittest
from lib.geometry.util import generate_convex_hull
from lib.vec2d import Vec2d

class Test(unittest.TestCase):
    def setUp(self):
        pass

    def test_convex_hull(self):
        points = [Vec2d(-1, 0), Vec2d(0, 1), Vec2d(-0.5, 0.5),Vec2d(0, 0), Vec2d(-1, 1)]
        self.assertEqual(generate_convex_hull(points), [Vec2d(0, 0), Vec2d(0, 1), Vec2d(-1, 1), Vec2d(-1, 0)])

    def test_random_hull(self):
        x_offset = 50
        y_offset = 50

        x_max = 100
        y_max = 100

        num_points = 1000
        for i in range(num_points):
            x = random.randint(x_offset, x_offset + x_max)
            y = random.randint(y_offset, y_offset + y_max)

if __name__ == '__main__':
    unittest.main()
