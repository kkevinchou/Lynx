from lib.ecs.entity.entity import Entity
from ant.ecs.component.cqueen import CQueen

class Queen(Entity):
    def initialize_entity(self):
        queen_component = CQueen()
        self.add_component(queen_component)
