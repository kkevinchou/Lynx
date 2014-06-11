class Entity(object):
    def __init__(self, components):
        self.components = {}
        for component in components:
        	self.components[component.component_id] = component

    def __getitem__(self, component_class):
        return self.components[component_class.component_id]

    def get(self, component_class):
        return self.components.get(component_class.component_id)
