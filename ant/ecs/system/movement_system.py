from lib.ecs.system.system import System
from ant.ecs.component.movement_component import MovementComponent

class MovementSystem(System):
    entities = []
    queued_entities = []
    instance = None

    @staticmethod
    def get_instance():
        if MovementSystem.instance is None:
            MovementSystem.instance = MovementSystem()

        return MovementSystem.instance

    def set_planner(self, planner):
        self.planner = planner

    def set_target(self, entity, goal):
        movement_component = entity.get_component(MovementComponent)
        movement_component.path_index = 0
        movement_component.path = self.planner.find_path(int(entity.position[0]), int(entity.position[1]), goal[0], goal[1])

    # delta - seconds
    # speed - pixels/second
    def update(self, delta):
        self.append_queued_entities()

        for entity in MovementSystem.entities:
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
        