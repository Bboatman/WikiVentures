from kivy.uix.widget import Widget
from kivy.properties import NumericProperty
from kivy.properties import BooleanProperty
from kivy.clock import Clock


class Collider(Widget):
	def __init__(self, **kwargs):
		super(Collider, self).__init__(**kwargs)
		self.count = 0 #for debugging purposes
	def collision_check_cb(self, instance, value):
		if instance.parent:
			for widget in instance.parent.children:
				if self.did_collide(instance, widget):
					instance.on_collide(widget)
					widget.on_collide(instance)
	def did_collide(self, widA, widB):
		if widA is widB:
			return False
		if not(isinstance(widB, Collidable)) or not(isinstance(widA, Collidable)):
			return False
		else:
			return widA.collide_widget(widB) and (widA.collidable and widB.collidable)

class Collidable(Widget):
	is_dead = BooleanProperty(True)
	def __init__(self, **kwargs):
		super(Collidable, self).__init__(**kwargs)
		self.is_dead = False
		self.collidable = True
		self.bind(is_dead = self.clean_up_self_cb)
		self.bind(parent = self.bind_to_collider)
	def on_collide(self, other_widget):
		pass
	def destory(self):
		self.is_dead = True
	def bind_to_collider(self, instance, value):
		if value:
			self.bind(pos=value.collider.collision_check_cb)
	def clean_up_self_cb(self, instance, value):
		if value and self.parent:
			self.parent.remove_widget(self)
			del self