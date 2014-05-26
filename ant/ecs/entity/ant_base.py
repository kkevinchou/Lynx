from lib.ecs.entity.entity import Entity
from ant.notification_center import NotificationCenter

class AntBase(Entity):
	notification_center = NotificationCenter.get_instance()