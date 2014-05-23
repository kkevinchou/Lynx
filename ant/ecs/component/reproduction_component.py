from lib.ecs.component.component import Component

class ReproductionComponent(Component):
    component_id = 'ReproductionComponent'

    def __init__(self):
        self.egg = None
