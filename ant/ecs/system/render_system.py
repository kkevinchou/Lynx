from lib.ecs.system.system import System

class RenderSystem(System):
    entities = []
    queued_entities = []
    instance = None

    @staticmethod
    def get_instance():
        if RenderSystem.instance is None:
            RenderSystem.instance = RenderSystem()

        return RenderSystem.instance

    def update(self, delta):
        pass
