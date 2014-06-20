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

from ant import settings
from ant.ecs.entity.queen import Queen
from ant.ecs.entity.obstacle import Obstacle
from ant.ecs.system.movement_system import MovementSystem
from ant.ecs.system.render_system import RenderSystem
from ant.ecs.component.movement_component import MovementComponent
from ant.ecs.message_types import MESSAGE_TYPE
from lib.resource_manager import ResourceManager

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
    resource_manager = ResourceManager.get_instance()
    resource_manager.setup(settings.SPRITES_FOLDER)

    system_manager = set_up_systems()

    obstacle1 = Obstacle(Vec2d(250, 50), 100, 100, 10)
    obstacle2 = Obstacle(Vec2d(250, 250), 100, 100, 10)
    obstacle3 = Obstacle(Vec2d(250, 450), 100, 100, 10)
    obstacle3 = Obstacle(Vec2d(300, 50), 100, 100, 10)
    obstacle3 = Obstacle(Vec2d(300, 250), 100, 100, 10)
    obstacle3 = Obstacle(Vec2d(300, 450), 100, 100, 10)
    obstacle3 = Obstacle(Vec2d(400, 50), 100, 100, 10)
    obstacle3 = Obstacle(Vec2d(400, 250), 100, 100, 10)
    obstacle3 = Obstacle(Vec2d(400, 450), 100, 100, 10)

    system_manager.send_message({'message_type': MESSAGE_TYPE.INIT_MOVEMENT_PLANNER})

    queen = Queen()

    clock = pygame.time.Clock()
    quit = False

    while True:
        system_manager.update(1 / float(30))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit = True
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                system_manager.send_message({
                    'message_type': MESSAGE_TYPE.MOVE_ENTITY,
                    'entity': queen,
                    'goal': mouse_pos,
                })

        keys = pygame.key.get_pressed()
        if keys[pygame.K_ESCAPE]:
            quit = True

        if quit:
            sys.exit()

        clock.tick(30)

if __name__ == '__main__':
    run()
