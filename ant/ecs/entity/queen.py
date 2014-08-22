from ant.ecs.entity.ant_base import AntBase
from lib.vec2d import Vec2d
from lib.ecs.system_manager import SystemManager
from ant.ecs.message_types import MESSAGE_TYPE

from ant.ecs.component.render import SpriteRenderComponent
from ant.ecs.component.movement_component import MovementComponent
from ant.ecs.component.reproduction_component import ReproductionComponent
from ant.ecs.component.shape import DefinedShapeComponent

class Queen(AntBase):
    system_manager = SystemManager.get_instance()

    def __init__(self):
        super(Queen, self).__init__(
            [
                ReproductionComponent(),
                MovementComponent(speed=150),
                SpriteRenderComponent(self, 'mite.png', 64, 64),
            ]
        )

        self.position = Vec2d(0, 0)

        Queen.system_manager.send_message({
            'message_type': MESSAGE_TYPE.CREATE_ENTITY,
            'entity_type': 'queen',
            'entity': self
        })
