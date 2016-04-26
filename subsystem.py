from body import Body, Star
from kivy.core.window import Window

class SubSystem(object):
	def __init__(self, planet_names, title):
		self.title = title
		self.star = Star(title)
		self.star.label.color = (0, 255, 255, 1)
		self.star.label.bold = True
		self.star.label.font_size = 30
		self.centerSystem()
		self.planets = []
		i = 1
		for name in planet_names:
			self.planets.append(Body(name, i))
			i += 1


	def update(self, dt):
		for planet in self.planets:
			planet.update((self.star.x + self.star.size//2, self.star.y+ self.star.size//2), dt)
		self.star.label.text = self.title

	def centerSystem(self):
		self.star.setPos(Window.width/2-128, Window.height/2-128)