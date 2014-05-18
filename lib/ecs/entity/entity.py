class Entity(object):
    def __init__(self):
        self.components = {}
        self.initialize_entity()

    def get_component(self, component_id):
        return self.components.get(component_id, None)

    def add_component(self, component):
        self.components[component.component_id] = component