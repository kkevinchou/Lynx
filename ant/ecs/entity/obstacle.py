from ant.ecs.entity.ant_base import AntBase
from ant.ecs.component.shape import ShapeComponent
from ant.ecs.component.render import ShapeRenderComponent
from lib.vec2d import Vec2d
from lib.ecs.system_manager import SystemManager
from ant.ecs.message_types import MESSAGE_TYPE
from ant.ecs.entity_types import ENTITY_TYPE

class Obstacle(AntBase):
    system_manager = SystemManager.get_instance()

    def __init__(self, position, x_range, y_range, max_points):
        self.position = position.copy()
        super(Obstacle, self).__init__(
            [
                ShapeComponent(self, x_range, y_range, max_points),
                ShapeRenderComponent(self),
            ]
        )

        Obstacle.system_manager.send_message({
            'message_type': MESSAGE_TYPE.CREATE_ENTITY,
            'entity_type': ENTITY_TYPE.OBSTACLE,
            'entity': self
        })
