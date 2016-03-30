import math

from random import randrange
from widgetrenderer import *
from kivy.properties import NumericProperty
from kivy.properties import StringProperty
from kivy.uix.label import Label

class Body(Widget):
	''' 
	A 'celestial body', each planet or star in the solar system is one of these
	It represents a link on a wikipedia article
	'''
	size = NumericProperty(0)
	x = NumericProperty(0)
	y = NumericProperty(0)

	source = StringProperty("")

	def __init__(self, imgStr, title, order, **kwargs):
		super(Body, self).__init__( **kwargs)
		self.theta = randrange(0, 360)
		self.magnitude = order * 50 + 100
		print(str(order) + ' ' +  str(self.magnitude))
		self.speed = randrange(20, 70)
		
		self.label = Label(text = title)
		self.add_widget(self.label)

		self.source = imgStr
		self.size = 50 if imgStr == './assets/planet.png' else 256
		self.x = self.center_x
		self.y = self.center_y

	def orbit(self, starPos, dt):
		'''
		Move the body in orbit around its star's position
		starPos - (x,y) tuple of the center point of the star
		'''
		self.theta = self.theta + self.speed * dt
		self.setPos(math.cos(math.radians(self.theta)) * self.magnitude + starPos[0], math.sin(math.radians(self.theta)) * self.magnitude + starPos[1])


	def setPos(self, xpos, ypos):
		self.x = xpos
		self.y = ypos
		self.label.x = self.x
		self.label.y = self.y



