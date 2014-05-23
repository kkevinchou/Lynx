from lib.ecs.entity.entity import Entity
from ant.ecs.component.movement_component import MovementComponent
from ant.ecs.component.reproduction_component import ReproductionComponent
from lib.vec2d import Vec2d

class Queen(Entity):
    def __init__(self):
    	components = [
        	ReproductionComponent(),
        	MovementComponent()
    	]

        super(Queen, self).__init__(components)
        self.position = Vec2d(0, 0)
