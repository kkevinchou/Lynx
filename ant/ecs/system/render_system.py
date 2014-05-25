import pygame

from lib.ecs.system.system import System
from lib.vec2d import Vec2d
from ant.ecs.component.movement_component import MovementComponent
from ant.ecs.message_types import MESSAGE_TYPE
from ant.renderer import Renderer

class RenderSystem(System):
    def __init__(self, width, height):
        pygame.init()
        pygame.font.init()

        self.width, self.height = width, height
        size = width, height
        screen = pygame.display.set_mode(size, 0, 32)
        self.screen = screen
        self.font = pygame.font.Font(None, 20)

        self.entities = []

        message_handlers = {
            MESSAGE_TYPE.CREATE_ENTITY: self.handle_create_entity,
        }

        super(RenderSystem, self).__init__(message_handlers)

    def clear(self, color=(255, 255, 255)):
        self.screen.fill(color)

    def draw(self, polygon, color=(0, 0, 0)):
        points = polygon.get_points()

        for point in points:
            pygame.draw.circle(self.screen, color, (point.x, point.y), 3, 3)

            text = self.font.render('[{}, {}]'.format(point.x, point.y), 1, (10, 155, 10))
            self.screen.blit(text, text.get_rect(centerx=point.x + 30, centery=point.y))

        for i in range(len(points)):
            point_a = points[(i + 1) % len(points)]
            point_b = points[i]
            pygame.draw.line(self.screen, color, point_a, point_b)

    def draw_lines(self, points, color=(0, 0, 0)):
        for i in range(len(points) - 1):
            point_a = points[(i + 1) % len(points)]
            point_b = points[i]
            pygame.draw.line(self.screen, color, point_a, point_b)

    def draw_circle(self, position, color=(15, 15, 200)):
        pygame.draw.circle(self.screen, color, (position.x, position.y), 3, 3)

    def flip(self):
        pygame.display.flip()

    def handle_create_entity(self, message):
        self.entities.append(message['entity'])

    def update(self, delta):
        self.handle_messages()

        self.clear()

        # for obstacle in obstacles:
        #     renderer.draw(obstacle)

        for entity in self.entities:
            movement_component = entity.get_component(MovementComponent)
            if movement_component is not None and movement_component.path is not None:
                self.draw_lines(movement_component.path, (255, 0, 0))

            self.draw_circle(Vec2d(int(entity.position[0]), int(entity.position[1])))
        self.flip()
