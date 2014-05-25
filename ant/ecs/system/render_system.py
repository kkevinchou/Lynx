from lib.ecs.system.system import System
from lib.vec2d import Vec2d
from ant.ecs.component.movement_component import MovementComponent
from ant.ecs.message_types import MESSAGE_TYPE
from ant.renderer import Renderer

class RenderSystem(System):
    def __init__(self):
        self.entities = []
        self.renderer = Renderer(800, 600)

        message_handlers = {
            MESSAGE_TYPE.CREATE_ENTITY: self.handle_create_entity,
        }

        super(RenderSystem, self).__init__(message_handlers)

    def handle_create_entity(self, message):
        self.entities.append(message['entity'])

    def update(self, delta):
        self.handle_messages()

        self.renderer.clear()

        # for obstacle in obstacles:
        #     renderer.draw(obstacle)

        for entity in self.entities:
            movement_component = entity.get_component(MovementComponent)
            if movement_component is not None and movement_component.path is not None:
                self.renderer.draw_lines(movement_component.path, (255, 0, 0))

            self.renderer.draw_circle(Vec2d(int(entity.position[0]), int(entity.position[1])))
        self.renderer.flip()
