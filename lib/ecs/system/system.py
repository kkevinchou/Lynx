class System(object):
    def register(self, entity):
        self.queued_entities.append(entity)

    def append_queued_entities(self):
        self.entities.extend(self.queued_entities)
        self.queued_entities = []