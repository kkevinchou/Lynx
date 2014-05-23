from lib.ecs.entity.entity import Entity
from lib.vec2d import Vec2d

from ant.ecs.component.movement_component import MovementComponent
from ant.ecs.component.reproduction_component import ReproductionComponent

from ant.ecs.system.movement_system import MovementSystem
from ant.ecs.system.render_system import RenderSystem

class Queen(Entity):
    def __init__(self):
        components = [
            ReproductionComponent(),
            MovementComponent()
        ]

        systems = [
            MovementSystem.get_instance(),
            RenderSystem.get_instance()
        ]

        super(Queen, self).__init__(components, systems)

        self.position = Vec2d(0, 0)
