import pygame

from lib.ecs.component.component import Component
from ant.ecs.component.shape_component import ShapeComponent
from ant.ecs.component.movement_component import MovementComponent

class RenderComponent(Component):
    component_id = 'RenderComponent'

    def __init__(self, entity):
        self.entity = entity

    def draw(self, screen, color=(0, 0, 0)):
        raise NotImplementedError()

class ShapeRenderComponent(RenderComponent):
    component_id = 'RenderComponent'

    def __init__(self, entity):
        super(ShapeRenderComponent, self).__init__(entity)
        self.font = pygame.font.Font(None, 15)

    def draw(self, screen):
        color=(0, 115, 115)
        shape_component = self.entity[ShapeComponent]
        polygon = shape_component.get_polygon()
        points = polygon.get_points()

        for point in points:
            pygame.draw.circle(screen, color, (point.x, point.y), 3, 3)

            text = self.font.render('[{}, {}]'.format(point.x, point.y), 1, (155, 155, 10))
            screen.blit(text, text.get_rect(centerx=point.x + 30, centery=point.y))

        for i in range(len(points)):
            point_a = points[(i + 1) % len(points)]
            point_b = points[i]
            pygame.draw.line(screen, color, point_a, point_b)

class SimpleRenderComponent(RenderComponent):
    component_id = 'RenderComponent'

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
