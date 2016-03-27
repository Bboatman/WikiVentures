from wikipedia import page
from body import *
from kivy.core.window import Window

class System():
	def __init__(self, title):
		self.page = page(title)
		self.star = Body('./assets/big_planet.png', title)
		self.centerSystem()
		self.planets = []
		for child_title in self.page.links:
			self.planets.append(Body('./assets/planet.png', child_title))

	def update(self, dt):
		for planet in self.planets:
			planet.orbit((self.star.x + 128, self.star.y + 128), dt)

	def centerSystem(self):
		self.star.setPos(Window.width/2-128, Window.height/2-128)

