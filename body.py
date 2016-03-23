import math

from random import randrange
from widgetrenderer import *
from kivy.properties import NumericProperty
from kivy.properties import StringProperty
from kivy.uix.label import Label

class Body(WidgetRenderer):
	''' 
	A 'celestial body', each planet or star in the solar system is one of these
	It represents a link on a wikipedia article
	'''
	def __init__(self, imgStr, title, **kwargs):
		super(Body, self).__init__(imgStr, **kwargs)
		self.theta = randrange(0, 360)
		self.magnitude = randrange(60, 600, 20)
		self.speed = randrange(20, 70)
		self.label = Label(text = title)
		self.add_widget(self.label)

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


