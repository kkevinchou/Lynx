from lib.ecs.component.component import Component
from lib.geometry.polygon import Polygon

class ShapeComponent(Component):
    component_id = 'ShapeComponent'

    def __init__(self, entity, width, height):
    	Polygon([Vec2d(width, height), Vec2d(0, height), Vec2d(0, 0), Vec2d(width, 0)])
  		self.entity = entity