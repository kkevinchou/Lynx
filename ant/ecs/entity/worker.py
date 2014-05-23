from lib.ecs.entity.entity import Entity
from ant.ecs.component.movement_component import MovementComponent
from ant.ecs.component.reproduction_component import ReproductionComponent
from lib.vec2d import Vec2d

class Worker(Entity):
    def __init__(self):
        super(Worker, self).__init__()
        self.position = Vec2d(0, 0)

    def initialize_entity(self):
    	return
