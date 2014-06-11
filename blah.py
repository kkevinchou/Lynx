# import unittest

# from ant.test import *

# if __name__ == '__main__':
#     unittest.main()

import unittest
import sys, pygame

from lib.vec2d import Vec2d
from lib.geometry.util import generate_random_polygon, create_polygons
from lib.pathfinding.astar.astarplanner import AStarPlanner
from lib.geometry.polygon import Polygon
from lib.ecs.system_manager import SystemManager

from ant.ecs.entity.queen import Queen
from ant.ecs.entity.obstacle import Obstacle
from ant.ecs.system.movement_system import MovementSystem
from ant.ecs.system.render_system import RenderSystem
from ant.ecs.component.movement_component import MovementComponent
from ant.ecs.message_types import MESSAGE_TYPE

def set_up_systems():
    system_manager = SystemManager.get_instance()

    movement_system = MovementSystem(AStarPlanner())
    render_system = RenderSystem(800, 600)

    system_manager.init(
        [
            movement_system,
            render_system,
        ]
    )

    return system_manager

def run():
    system_manager = set_up_systems()

    obstacle1 = Obstacle(100, 50, 200, 200, 10)
    obstacle2 = Obstacle(100, 201, 200, 300, 10)
    obstacle3 = Obstacle(100, 301, 200, 500, 10)
    obstacle4 = Obstacle(300, 201, 500, 300, 10)
    obstacle5 = Obstacle(700, 401, 800, 600, 10)
    obstacle6 = Obstacle(500, 401, 600, 600, 10)

    system_manager.send_message({'message_type': MESSAGE_TYPE.INIT_MOVEMENT_PLANNER})

    queen = Queen()

    clock = pygame.time.Clock()
    quit = False

    while True:
        system_manager.update(1 / float(30))

        if pygame.mouse.get_pressed()[0]:
            mouse_pos = pygame.mouse.get_pos()
            system_manager.send_message({
                'message_type': MESSAGE_TYPE.MOVE_ENTITY,
                'entity': queen,
                'goal': mouse_pos,
            })
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

        clock.tick(30)

if __name__ == '__main__':
    run()
