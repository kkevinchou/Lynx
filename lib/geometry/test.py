import unittest
from lib.geometry.util import generate_convex_hull
from lib.vec2d import Vec2d

class Test(unittest.TestCase):
	def setUp(self):
		pass

	def test_convex_hull(self):
		points = [Vec2d(-0.5, 0.5), Vec2d(0, 0), Vec2d(0, 1), Vec2d(-1, 1), Vec2d(-1, 0)]
		self.assertEqual(generate_convex_hull(points), [])

if __name__ == '__main__':
	unittest.main()