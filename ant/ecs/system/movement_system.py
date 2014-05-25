from lib.ecs.system.system import System
from ant.ecs.component.movement_component import MovementComponent
from ant.ecs.message_types import MESSAGE_TYPE

class MovementSystem(System):
    def __init__(self):
        self.entities = []

        message_handlers = {
            MESSAGE_TYPE.CREATE_ENTITY: self.handle_create_entity,
            MESSAGE_TYPE.MOVE_ENTITY: self.handle_move_entity,
        }

        super(MovementSystem, self).__init__(message_handlers)

    def handle_create_entity(self, message):
        self.entities.append(message['entity'])

    def handle_move_entity(self, message):
        entity = message['entity']
        goal = message['goal']

        movement_component = entity.get_component(MovementComponent)
        movement_component.path_index = 0
        movement_component.path = self.planner.find_path(int(entity.position[0]), int(entity.position[1]), goal[0], goal[1])

    def set_planner(self, planner):
        self.planner = planner

    def handle_messages(self):
        supported_message_handlers = self.message_handlers.keys()
        for message in self.messages:
            message_type = message['message_type']
            if message_type not in supported_message_handlers:
                continue
            self.message_handlers[message_type](message)

        self.messages = []

    # delta - seconds
    # speed - pixels/second
    def update(self, delta):
        self.handle_messages()

        for entity in self.entities:
            movement_component = entity.get_component(MovementComponent)
            path = movement_component.path
            path_index = movement_component.path_index
            speed = movement_component.speed

            if path is None:
                continue

            if path_index < len(path):
                intermediate_target = path[path_index]

                if intermediate_target.get_distance(entity.position) < speed * delta:
                    entity.position = intermediate_target.copy()
                    movement_component.path_index += 1
                else:
                    direction = (intermediate_target - entity.position).normalized()
                    scaled_velocity = direction * speed * delta
                    entity.position += scaled_velocity
            else:
                # Path complete
                movement_component.path = None
        