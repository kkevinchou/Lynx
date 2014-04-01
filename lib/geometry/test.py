import unittest
from lib.geometry.util import generate_convex_hull
from lib.geometry.point import Point

class Test(unittest.TestCase):
	def setUp(self):
		pass

	def test_convex_hull(self):
		points = [Point(-0.5, 0.5), Point(0, 0), Point(0, 1), Point(-1, 1), Point(-1, 0)]
		self.assertEqual(generate_convex_hull(points), [])

if __name__ == '__main__':
	unittest.main()