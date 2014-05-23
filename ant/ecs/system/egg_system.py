from lib.ecs.system.system import System

class EggSystem(System):
    entities = []

    def register(self, entity):
        EggSystem.entities.append(entity)

    def update(self, delta):
        for entity in EggSystem.entities:
            