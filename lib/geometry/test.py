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

        points = []
        num_points = 20
        for i in range(num_points):
            x = random.randint(0, x_max) + x_offset
            y = -1 * random.randint(0, y_max) + -1 * y_offset
            points.append(Vec2d(x, y))

        points = [Vec2d(105, -150), Vec2d(113, -134), Vec2d(84, -111), Vec2d(143, -137), Vec2d(136, -97), Vec2d(138, -60)]
        hull_points = generate_convex_hull(points)
        print hull_points

        import sys, pygame
        pygame.init()

        size = width, height = 320, 240
        black = (0, 0, 0)
        white = (255, 255, 255)
        green = (0, 255, 0)
        red = (255, 0, 0)

        screen = pygame.display.set_mode(size, 0, 32)
        clock = pygame.time.Clock()

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT: sys.exit()

            screen.fill(white)
            for point in points:
                draw_color = black
                if point in hull_points:
                    draw_color = red

                pygame.draw.circle(screen, draw_color, (point.x, -point.y), 2, 2)

            pygame.draw.circle(screen, green, (hull_points[0].x, -hull_points[0].y), 2, 2)
            num_hull_points = len(hull_points)
            for i in range(num_hull_points):
                point_a = (hull_points[(i + 1) % num_hull_points].x, -hull_points[(i + 1) % num_hull_points].y)
                point_b = (hull_points[i].x, -hull_points[i].y)

                pygame.draw.line(screen, red, point_a, point_b)

            pygame.display.flip()
            pygame.display.update()
            clock.tick(30)

if __name__ == '__main__':
    unittest.main()
