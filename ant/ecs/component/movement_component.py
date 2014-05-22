from lib.ecs.component.component import Component

class MovementComponent(Component):
    component_id = 'MovableComponent'

    def __init__(self):
    	self.path = None
    	self.path_index = 0