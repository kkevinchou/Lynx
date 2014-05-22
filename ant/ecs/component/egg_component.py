from lib.ecs.component.component import Component

class EggComponent(Component):
    component_id = 'EggComponent'

    def __init__(self):
        self.egg = None

    def update(self):
        pass