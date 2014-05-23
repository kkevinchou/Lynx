class Entity(object):
    def __init__(self, components, systems):
        self.components = {}
        for component in components:
            self.components[component.component_id] = component

        for system in systems:
            system.register(self)

    def get_component(self, component_class):
        return self.components.get(component_class.component_id, None)