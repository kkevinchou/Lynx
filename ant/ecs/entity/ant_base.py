from lib.ecs.entity.entity import Entity
from ant.ecs.message_center import MessageCenter

class AntBase(Entity):
	message_center = MessageCenter.get_instance()