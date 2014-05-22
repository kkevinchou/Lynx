from lib.ecs.component.component import Component

class MovementComponent(Component):
    component_id = 'MovableComponent'

    def __init__(self, speed=100):
        self.path = None
        self.path_index = 0
        self.speed = speed