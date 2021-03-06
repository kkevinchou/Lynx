import pygame

from lib.ecs.component.component import Component
from ant.ecs.component.shape import ShapeComponent
from ant.ecs.component.movement_component import MovementComponent
from lib.resource_manager import ResourceManager
from lib.geometry.polygon import Polygon
from lib.vec2d import Vec2d

from ant.settings import SPRITES_FOLDER

class RenderComponent(Component):
    component_id = 'RenderComponent'

    def draw(self, screen, color=(0, 0, 0)):
        raise NotImplementedError()

class SpriteRenderComponent(RenderComponent):
    component_id = 'RenderComponent'
    resource_manager = ResourceManager.get_instance()

    def __init__(self, entity, sprite_file, width, height):
        self.entity = entity
        self.width, self.height = width, height
        self.sprite = SpriteRenderComponent.resource_manager.get_sprite(sprite_file)

    def draw(self, screen):
        screen.blit(self.sprite, self.entity.position - Vec2d(int(self.width) / 2, int(self.height) / 2))

class ShapeRenderComponent(RenderComponent):
    component_id = RenderComponent.component_id

    def __init__(self, shape_component):
        self.shape_component = shape_component
        self.font = pygame.font.Font(None, 15)
        self.agent_prototype = Polygon.rectangular_polygon(64, 64)

    def draw_edges(self, screen, points, color=(155, 155, 10)):
        for point in points:
            pygame.draw.circle(screen, color, (point.x, point.y), 3, 3)

            text = self.font.render('[{}, {}]'.format(point.x, point.y), 1, (37, 4, 52))
            # screen.blit(text, text.get_rect(centerx=point.x + 30, centery=point.y))

        for i in range(len(points)):
            point_a = points[(i + 1) % len(points)]
            point_b = points[i]
            pygame.draw.line(screen, color, point_a, point_b)

    def draw_c_polygon(self, screen):
        c_polygon_points = self.shape_component.compute_c_polygon(self.agent_prototype).get_points()
        self.draw_edges(screen, c_polygon_points, (98, 200, 156))

    def draw(self, screen):
        color=(0, 115, 115)

        self.draw_edges(screen, self.shape_component.get_points())
        self.draw_c_polygon(screen)

class SimpleRenderComponent(RenderComponent):
    component_id = RenderComponent.component_id

    def __init__(self, entity):
        super(SimpleRenderComponent, self).__init__(entity)

    def draw_lines(self, screen, points, color=(0, 0, 0)):
        for i in range(len(points) - 1):
            point_a = points[(i + 1) % len(points)]
            point_b = points[i]
            pygame.draw.line(screen, color, point_a, point_b)

    def draw(self, screen):
        color=(65, 15, 25)
        pygame.draw.circle(screen, color, (int(self.entity.position[0]), int(self.entity.position[1])), 3, 3)

        movement_component = self.entity.get(MovementComponent)
        if movement_component is not None and movement_component.path is not None:
            self.draw_lines(screen, movement_component.path, (255, 0, 0))
