import unittest
from lib.vec2d import Vec2d
import sys, pygame
from lib.pathfinding.astar.polygon import Polygon
from lib.pathfinding.astar.util import (
    colinear,
    shares_point,
    intersect_polygon,
    line_intersect
)

class Test(unittest.TestCase):
    def setUp(self):
        pass

    def test_basic_polygon_intersect(self):
        poly = Polygon()
        poly.add_point(0, 0)
        poly.add_point(0, 1)
        poly.add_point(1, 1)
        poly.add_point(1, 0)

        line = [Vec2d(-0.5, -0.5), Vec2d(0.5, 0.5)]
        self.assertTrue(intersect_polygon(line, poly))

        line = [Vec2d(1, -1), Vec2d(1, 0)]
        self.assertFalse(intersect_polygon(line, poly))

    def test_basic_line_intersect(self):
        line_a = [Vec2d(1, 0), Vec2d(1, 1)]
        line_b = [Vec2d(1, 1), Vec2d(0, 1)]

        self.assertFalse(line_intersect(line_a, line_b))

    def test_border_non_intersect(self):
        polygon = Polygon()
        polygon.add_point(0, 0)
        polygon.add_point(0, 1)
        polygon.add_point(1, 1)
        polygon.add_point(1, 0)

        line1 = [Vec2d(0, 0), Vec2d(1, 0)]

        self.assertFalse(intersect_polygon(line1, polygon))

    def test_shares_point(self):
        line_a = [Vec2d(1, 0), Vec2d(1, 1)]
        line_b = [Vec2d(1, 1), Vec2d(0, 1)]
        line_c = [Vec2d(0, 1), Vec2d(0, 0)]

        self.assertTrue(shares_point(line_a, line_b))
        self.assertFalse(shares_point(line_a, line_c))

    def test_colinear(self):
        self.assertFalse(colinear([Vec2d(0, 0), Vec2d(1, 0)], [Vec2d(0, 0), Vec2d(0, 1)]))
        self.assertFalse(colinear([Vec2d(0, 0), Vec2d(1, 0)], [Vec2d(0, 0), Vec2d(0, -1)]))
        self.assertTrue(colinear([Vec2d(0, 0), Vec2d(1, 0)], [Vec2d(0, 0), Vec2d(-1, 0)]))
        self.assertTrue(colinear([Vec2d(0, 0), Vec2d(1, 0)], [Vec2d(0, 0), Vec2d(1, 0)]))

    def ztest_visual(self):
        pygame.init()
        size = width, height = 320, 240
        screen = pygame.display.set_mode(size, 0, 32)
        clock = pygame.time.Clock()

        black = (0, 0, 0)
        white = (255, 255, 255)
        green = (0, 255, 0)
        red = (255, 0, 0)
        bleh = (155, 10, 110)

        poly = Polygon()
        poly.add_point(50, 0)
        poly.add_point(50, 50)
        poly.add_point(0, 50)
        poly.add_point(0, 0)

        poly2 = Polygon()
        poly2.add_point(50, 0)
        poly2.add_point(50, 50)
        poly2.add_point(0, 50)
        poly2.add_point(0, 0)

        c_poly = poly.compute_c_polygon(poly2)
        print c_poly

        screen.fill(white)

        for point in poly.get_points():
            print point
            draw_color = black
            pygame.draw.circle(screen, draw_color, (point.x + 200, height - point.y - 100), 3, 3)
            print (point.x + 200, height - point.y - 200)

        for point in c_poly.get_points():
            print point
            draw_color = green
            pygame.draw.circle(screen, draw_color, (point.x + 200, height - point.y - 100), 3, 3)
            print (point.x + 200, 200 + height - point.y)

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT: sys.exit()

            keys = pygame.key.get_pressed()
            if keys[pygame.K_ESCAPE]:
                sys.exit()

            # num_hull_points = len(hull_points)
            # for i in range(num_hull_points):
            #     point_a = (hull_points[(i + 1) % num_hull_points].x, -hull_points[(i + 1) % num_hull_points].y)
            #     point_b = (hull_points[i].x, -hull_points[i].y)

            #     pygame.draw.line(screen, red, point_a, point_b)
            #     pygame.display.flip()

            pygame.display.flip()
            pygame.display.update()
            clock.tick(30)

if __name__ == '__main__':
    unittest.main()
