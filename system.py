import math

from body import *
from kivy.core.window import Window

class System():
	def __init__(self):
		self.star = Body('./assets/big_planet.png')
		self.star.x = Window.width/2
		self.star.y = Window.height/2
		self.planets = [Body('./assets/planet.png')]

	def update(self, dt):
		for planet in self.planets:
			planet.theta = planet.theta + planet.speed * dt
			planet.x = math.cos(math.radians(planet.theta)) * planet.magnitude + self.star.x
			planet.y = math.sin(math.radians(planet.theta)) * planet.magnitude + self.star.y

