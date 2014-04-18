import unittest
import sys, pygame

from lib.vec2d import Vec2d
from lib.geometry.util import generate_convex_hull, generate_random_polygon
from renderer import Renderer
from lib.pathfinding.astar.util import polygons_intersect
from lib.pathfinding.astar.astarplanner import AStarPlanner

class Test(unittest.TestCase):
    def setUp(self):
        pass

    def test_zvisual(self):
        obstacle1 = generate_random_polygon(100, 50, 200, 200, 10)
        obstacle2 = generate_random_polygon(100, 201, 200, 300, 10)
        obstacle3 = generate_random_polygon(100, 301, 200, 500, 10)
        obstacle4 = generate_random_polygon(300, 201, 500, 300, 10)
        obstacle5 = generate_random_polygon(700, 401, 800, 600, 10)
        obstacle6 = generate_random_polygon(500, 401, 600, 600, 10)
        # obstacle6 = Polygon([Vec2d(517, -574), Vec2d(575, -538), Vec2d(589, -512), Vec2d(596, -498), Vec2d(578, -447), Vec2d(528, -402), Vec2d(500, -529), Vec2d(517, -574)])
        obstacles = [obstacle1, obstacle2, obstacle3, obstacle4, obstacle5, obstacle6]
        # obstacles = [obstacle6]

        planner = AStarPlanner()
        for obstacle in obstacles:
            planner.add_polygon(obstacle)

        path = planner.find_path(0, 0, 800, 600)

        renderer = Renderer(800, 600)
        renderer.clear()

        planner.draw_neighbors(renderer, (15, 200, 200))

        for obstacle in obstacles:
            renderer.draw(obstacle)

        renderer.draw_lines(path, (255, 0, 0))
        renderer.flip()

        clock = pygame.time.Clock()

        while True:

            for event in pygame.event.get():
                if event.type == pygame.QUIT: sys.exit()

            keys = pygame.key.get_pressed()
            if keys[pygame.K_ESCAPE]:
                sys.exit()

            clock.tick(30)

if __name__ == '__main__':
    unittest.main()
