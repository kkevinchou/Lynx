class Entity(object):
    def __init__(self, components):
        self.components = {}
        for component in components:
        	self.components[component.component_id] = component

    def get_component(self, component_class):
        return self.components.get(component_class.component_id, None)