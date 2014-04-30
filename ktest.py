import unittest
import sys, pygame

from lib.vec2d import Vec2d
from lib.geometry.util import generate_random_polygon
from renderer import Renderer
from lib.pathfinding.astar.astarplanner import AStarPlanner
from lib.pathfinding.astar.polygon import Polygon

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
path = planner.find_path(0, 0, 800, 600)

position = Vec2d(0, 0)
path_index = 0
speed = 5

# planner.draw_neighbors(renderer, (15, 200, 200))

clock = pygame.time.Clock()

while True:
    if pygame.mouse.get_pressed()[0]:
        path_index = 0
        mouse_pos = pygame.mouse.get_pos()
        path = planner.find_path(int(position.x), int(position.y), mouse_pos[0], mouse_pos[1])
    elif pygame.mouse.get_pressed()[2]:
        break

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_ESCAPE]:
        sys.exit()

    renderer.clear()

    for obstacle in obstacles:
        renderer.draw(obstacle)

    renderer.draw_lines(path, (255, 0, 0))

    if path_index < len(path):
        target_node = path[path_index]
        if target_node.get_distance(position) < speed:
            position = target_node
            path_index += 1
        else:
            direction = target_node - position
            direction = direction.normalized()
            position = position + (direction * speed)

    renderer.draw_circle(Vec2d(int(position.x), int(position.y)))
    renderer.flip()

    clock.tick(30)
