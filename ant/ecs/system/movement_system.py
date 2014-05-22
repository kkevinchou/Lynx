from lib.ecs.system.system import System
from ant.ecs.component.movement_component import MovementComponent

class MovementSystem(System):
    entities = []

    def __init__(self):
        self.paths = {}
        self.path_indices = {}

    def register(self, entity):
        MovementSystem.entities.append(entity)

    def set_target(self, entity, goal):
        self.path_indicies[entity] = 0
        self.paths[entity] = planner.find_path(int(entity.position[0]), int(entity.position[1]), goal[0], goal[1])

    # delta - seconds
    # speed - pixels/second
    def update(self, delta):
        speed = 50

        for entity in entities:
            path = self.paths.get(entity)
            path_index = self.path_indicies.get(entity)

            if path is None or path_index is None:
                continue

            if path_index < len(path):
                intermediate_target = path[path_index]

                if intermediate_target.get_distance(entity.position) < speed:
                    entity.position = intermediate_target
                    self.path_indicies[entity] += 1
                else:
                    direction = self.target - entity.position
                    distance = direction.normalized() * speed * delta
                    entity.position += distance
            else:
                # Path complete
                self.paths.pop(entity)
                self.path_indicies.pop(entity)
        