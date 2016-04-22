from body import Body
from kivy.core.window import Window

class SubSystem(object):
	def __init__(self, planet_names, title):
		self.title = title
		self.star = Body('./assets/big_planet.png', title, 0)
		self.star.label.color = (0, 255, 255, 1)
		self.star.label.bold = True
		self.star.label.font_size = 30
		self.centerSystem()
		self.planets = [self.star]
		i = 0
		for name in planet_names:
			self.planets.append(Body('./assets/planet.png', name, i))
			i += 1


	def update(self, dt):
		for planet in self.planets:
			planet.orbit((self.star.x + 120, self.star.y + 120), dt)
		self.star.label.text = self.title



	def centerSystem(self):
		self.star.setPos(Window.width/2-128, Window.height/2-128)