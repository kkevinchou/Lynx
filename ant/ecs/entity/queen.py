from lib.ecs.entity.entity import Entity
from ant.ecs.component.movement_component import MovementComponent
from ant.ecs.component.reproduce_component import ReproduceComponent
from lib.vec2d import Vec2d

class Queen(Entity):
    def __init__(self):
        self.position = Vec2D(0, 0)
        
    def initialize_entity(self):
        reproduce_component = ReproduceComponent()
        movement_component = MovementComponent()

        self.add_component(reproduce_component)
        self.add_component(movement_component)
