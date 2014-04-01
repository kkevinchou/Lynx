import unittest
from lib.geometry.util import generate_convex_hull

class Test(unittest.TestCase):
	def setUp(self):
		pass

	def test_convex_hull(self):
		self.assertEqual(generate_convex_hull([]), [])

if __name__ == '__main__':
	unittest.main()