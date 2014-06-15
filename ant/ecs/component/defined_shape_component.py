from lib.ecs.component.component import Component
from lib.geometry.polygon import Polygon
from lib.geometry.util import generate_random_polygon

# TODO: This should be a lib class
class DefinedShapeComponent(Component):
    component_id = 'ShapeComponent'

    def __init__(self, entity):
        self.entity = entity
        self.polygon = Polygon.rectangular_polygon(64, 64)
        self.points = [self.entity.position + point for point in self.polygon.get_points()]

    def get_points(self):
        return self.points

    def get_polygon(self):
        return self.polygon
