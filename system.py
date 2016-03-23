from wikipedia import page
from body import *
from kivy.core.window import Window

class System():
	def __init__(self, title):
		self.page = page(title)
		self.star = Body('./assets/big_planet.png', title)
		self.star.setPos(Window.height/2, Window.width/2)
		self.planets = []
		for child_title in self.page.links:
			self.planets.append(Body('./assets/planet.png', child_title))

	def update(self, dt):
		for planet in self.planets:
			planet.move((self.star.x, self.star.y), dt)

