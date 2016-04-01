from body import *
from kivy.core.window import Window

class SubSystem(object):
	def __init__(self, planet_names, title):
		self.title = title
		self.star = Body('./assets/big_planet.png', title, 0)
		self.centerSystem()
		self.planets = []
		i = 0
		for name in planet_names:
			self.planets.append(Body('./assets/planet.png', name, i))
			i += 1


	def update(self, dt):
		for planet in self.planets:
			planet.orbit((self.star.x + 120, self.star.y + 120), dt)

	def centerSystem(self):
		self.star.setPos(Window.width/2-128, Window.height/2-128)

