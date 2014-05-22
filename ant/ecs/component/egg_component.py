from lib.ecs.component.component import Component

class ReproduceComponent(Component):
    component_id = 'ReproduceComponent'

    def __init__(self):
        self.egg = None

    def update(self):
        pass