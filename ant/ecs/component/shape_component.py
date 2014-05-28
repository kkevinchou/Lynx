from lib.ecs.component.component import Component
from lib.geometry.polygon import Polygon
from lib.geometry.util import generate_random_polygon

class ShapeComponent(Component):
    component_id = 'ShapeComponent'

    def __init__(self, x_min, y_min, x_max, y_max, max_points, entity):
        self.polygon = generate_random_polygon(x_min, y_min, x_max, y_max, max_points)
        self.entity = entity