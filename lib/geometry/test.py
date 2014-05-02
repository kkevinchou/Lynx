import random
import unittest
from lib.geometry.util import generate_convex_hull, generate_random_polygon
from lib.vec2d import Vec2d
import sys, pygame

class GeometryTest(unittest.TestCase):
    def setUp(self):
        pass

    def test_broken_hull_history1(self):
        points = [Vec2d(60, 130), Vec2d(65, 83), Vec2d(105, 74), Vec2d(141, 136), Vec2d(79, 123)]
        hull_points = generate_convex_hull(points)
        self.assertEqual(hull_points, [Vec2d(141, 136), Vec2d(105, 74), Vec2d(65, 83), Vec2d(60, 130)])

    def test_broken_hull_history2(self):
        points = [Vec2d(105, 150), Vec2d(113, 134), Vec2d(84, 111), Vec2d(143, 137), Vec2d(136, 97), Vec2d(138, 60)]
        hull_points = generate_convex_hull(points)
        self.assertEqual(hull_points, [Vec2d(105, 150), Vec2d(143, 137), Vec2d(138, 60), Vec2d(84, 111)])

    def test_broken_hull_history3(self):
        points = [Vec2d(579, 518), Vec2d(500, 512), Vec2d(528, 501), Vec2d(573, 477), Vec2d(510, 541), Vec2d(533, 565), Vec2d(542, 578), Vec2d(516, 437), Vec2d(575, 401), Vec2d(519, 470)]
        hull_points = generate_convex_hull(points)
        self.assertEqual(len(hull_points), 6)

    def test_convex_hull(self):
        points = [Vec2d(1, 0), Vec2d(0, 0), Vec2d(0.5, 0.5),Vec2d(0, 1), Vec2d(1, 1)]
        self.assertEqual(generate_convex_hull(points), [Vec2d(1, 1), Vec2d(1, 0), Vec2d(0, 0), Vec2d(0, 1)])

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

        x_min = 50
        y_min = 50
        x_max = 100
        y_max = 100

        polygon = generate_random_polygon(x_min, y_min, x_max, y_max, 10)
        points = polygon.get_points()

        screen.fill(white)

        for point in points:
            draw_color = black
            pygame.draw.circle(screen, draw_color, (point.x, point.y), 3, 3)

        hull_points = generate_convex_hull(points, screen)

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT: sys.exit()

            keys = pygame.key.get_pressed()
            if keys[pygame.K_ESCAPE]:
                sys.exit()

            num_hull_points = len(hull_points)
            for i in range(num_hull_points):
                point_a = hull_points[(i + 1) % num_hull_points]
                point_b = hull_points[i]

                pygame.draw.line(screen, red, point_a, point_b)
                pygame.display.flip()

            pygame.display.flip()
            pygame.display.update()
            clock.tick(30)

if __name__ == '__main__':
    unittest.main()
