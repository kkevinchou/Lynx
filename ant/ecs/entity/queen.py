from lib.ecs.entity.entity import Entity
from ant.ecs.component.movement_component import MovementComponent
from ant.ecs.component.reproduction_component import ReproductionComponent
from lib.vec2d import Vec2d

class Queen(Entity):
    def __init__(self):
        super(Queen, self).__init__()
        self.position = Vec2d(0, 0)

    def initialize_entity(self):
        reproduction_component = ReproductionComponent()
        movement_component = MovementComponent()

        self.add_component(reproduction_component)
        self.add_component(movement_component)
