from ant.ecs.entity.ant_base import AntBase
from ant.ecs.component.movement_component import MovementComponent
from ant.ecs.component.shape_component import ShapeComponent
from ant.ecs.component.shape_render_component import ShapeRenderComponent
from lib.vec2d import Vec2d
from lib.ecs.system_manager import SystemManager
from ant.ecs.message_types import MESSAGE_TYPE
from ant.ecs.entity_types import ENTITY_TYPE

class Obstacle(AntBase):
    system_manager = SystemManager.get_instance()

    def __init__(self, x_min, y_min, x_max, y_max, max_points):
        self.position = Vec2d(0, 0)
        super(Obstacle, self).__init__(
            [
                ShapeComponent(x_min, y_min, x_max, y_max, max_points, self),
                ShapeRenderComponent(self),
            ]
        )

        Obstacle.system_manager.send_message({
            'message_type': MESSAGE_TYPE.CREATE_ENTITY,
            'entity_type': ENTITY_TYPE.OBSTACLE,
            'entity': self
        })
