from ant.ecs.entity.ant_base import AntBase
from lib.vec2d import Vec2d
from lib.ecs.system_manager import SystemManager
from ant.ecs.message_types import MESSAGE_TYPE

from ant.ecs.component.render import SpriteRenderComponent
from ant.ecs.component.movement_component import MovementComponent
from ant.ecs.component.reproduction_component import ReproductionComponent
from ant.ecs.component.defined_shape_component import DefinedShapeComponent

class Queen(AntBase):
    system_manager = SystemManager.get_instance()

    def __init__(self):
        super(Queen, self).__init__(
            [
                ReproductionComponent(),
                MovementComponent(),
                SpriteRenderComponent(self, 'mite.png'),
            ]
        )

        self.position = Vec2d(0, 0)

        Queen.system_manager.send_message({
            'message_type': MESSAGE_TYPE.CREATE_ENTITY,
            'entity_type': 'queen',
            'entity': self
        })
