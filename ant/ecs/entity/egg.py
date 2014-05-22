from lib.ecs.entity.entity import Entity
from ant.ecs.component.creproduce import CHatch

class Egg(Entity):
    def initialize_entity(self):
        reproduce_component = ReproduceComponent()
        self.add_component(reproduce_component)
