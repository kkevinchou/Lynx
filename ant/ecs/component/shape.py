from lib.ecs.component.component import Component
from lib.geometry.util import generate_random_polygon, generate_convex_hull, copy_points_list
from lib.geometry.polygon import Polygon

# TODO: This should be a lib class
class ShapeComponent(Component):
    component_id = 'ShapeComponent'

    def __init__(self, entity, x_max, y_max, max_points):
        self.polygon = generate_random_polygon(x_max, y_max, max_points)
        self.entity = entity

    def get_points(self):
        return [self.entity.position + point for point in self.polygon.get_points()]

    #TODO : this method should be in Polygon.  Have this method create a new polygon
    # that has been offsetted by the entity's position
    def compute_c_polygon(self, agent):
        agent_points = copy_points_list(agent.get_points())

        all_points = []
        for point in self.get_points():
            for agent_point in agent_points:
                all_points.append(point - agent_point)

        c_polygon_points = generate_convex_hull(all_points)
        return Polygon(c_polygon_points)

# TODO: This should be a lib class
class DefinedShapeComponent(Component):
    component_id = ShapeComponent.component_id

    def __init__(self, entity):
        self.entity = entity
        self.polygon = Polygon.rectangular_polygon(64, 64)
        self.points = [self.entity.position + point for point in self.polygon.get_points()]

    def get_points(self):
        return [self.entity.position + point for point in self.polygon.get_points()]
