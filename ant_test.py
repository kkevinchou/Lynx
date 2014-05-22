# import unittest

# from ant.test import *

# if __name__ == '__main__':
#     unittest.main()

import unittest
import sys, pygame

from lib.vec2d import Vec2d
from lib.geometry.util import generate_random_polygon, create_polygons
from renderer import Renderer
from lib.pathfinding.astar.astarplanner import AStarPlanner
from lib.geometry.polygon import Polygon
from ant.ecs.entity.queen import Queen
from ant.ecs.system.movement_system import MovemenSystem

queen = Queen()
dude = Polygon([Vec2d(1, 1), Vec2d(1, 0), Vec2d(0, 0), Vec2d(0, 1)])

obstacle1 = generate_random_polygon(100, 50, 200, 200, 10)
obstacle2 = generate_random_polygon(100, 201, 200, 300, 10)
obstacle3 = generate_random_polygon(100, 301, 200, 500, 10)
obstacle4 = generate_random_polygon(300, 201, 500, 300, 10)
obstacle5 = generate_random_polygon(700, 401, 800, 600, 10)
obstacle6 = generate_random_polygon(500, 401, 600, 600, 10)
obstacles = [obstacle1, obstacle2, obstacle3, obstacle4, obstacle5, obstacle6]

planner = AStarPlanner()
planner.add_polygons(obstacles)
planner.init()

renderer = Renderer(800, 600)

movement_system = MovementSystem()
movement_system.register(queen)

# planner.draw_neighbors(renderer, (15, 200, 200))

clock = pygame.time.Clock()
quit = False
while True:
    movement_system.update(1 / float(30))

    if pygame.mouse.get_pressed()[0]:
        mouse_pos = pygame.mouse.get_pos()
        movement_system.set_target(queen, mouse_pos)
    elif pygame.mouse.get_pressed()[2]:
        break

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit = True

    keys = pygame.key.get_pressed()
    if keys[pygame.K_ESCAPE]:
        quit = True

    if quit:
        sys.exit()

    renderer.clear()

    for obstacle in obstacles:
        renderer.draw(obstacle)

    # renderer.draw_lines(path, (255, 0, 0))

    renderer.draw_circle(Vec2d(int(queen.position[0]), int(queen.position[1])))
    renderer.flip()

    clock.tick(30)
