from lib.ecs.system.system import System
from lib.geometry.polygon import Polygon
from ant.ecs.component.movement_component import MovementComponent
from ant.ecs.component.shape import ShapeComponent
from ant.ecs.message_types import MESSAGE_TYPE
from ant.ecs.entity_types import ENTITY_TYPE

class MovementSystem(System):
    def __init__(self, planner=None):
        self.entities = []
        self.obstacles = []
        self.planner = planner

        message_handlers = {
            MESSAGE_TYPE.CREATE_ENTITY: self.handle_create_entity,
            MESSAGE_TYPE.MOVE_ENTITY: self.handle_move_entity,
            MESSAGE_TYPE.INIT_MOVEMENT_PLANNER: self.handle_init_movement_planner,
        }

        self.agent_prototype = Polygon.rectangular_polygon(64, 64)

        super(MovementSystem, self).__init__(message_handlers)

    def handle_init_movement_planner(self, message):
        self.planner.init()

    def handle_create_entity(self, message):
        entity = message['entity']

        if message['entity_type'] == ENTITY_TYPE.OBSTACLE:
            # self.obstacles.append(entity)
            self.planner.register_obstacle(entity, self.agent_prototype)
        else:
            self.entities.append(entity)

    def handle_move_entity(self, message):
        entity = message['entity']
        goal = message['goal']

        movement_component = entity[MovementComponent]
        movement_component.path_index = 0
        movement_component.path = self.planner.find_path(int(entity.position[0]), int(entity.position[1]), goal[0], goal[1])

    def set_planner(self, planner):
        self.planner = planner

    # delta - seconds
    # speed - pixels/second
    def update(self, delta):
        self.handle_messages()

        for entity in self.entities:
            movement_component = entity[MovementComponent]
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
        
