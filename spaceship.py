import math

from random import randrange
from widgetrenderer import *
from kivy.properties import NumericProperty
from kivy.properties import StringProperty

class Spaceship(Widget):
	''' 
	Player's spaceship used to travel to other planets.
	'''
	size = NumericProperty(0)
	x = NumericProperty(0)
	y = NumericProperty(0)

	source = StringProperty("")

	def __init__(self, imgStr, **kwargs):
		super(Spaceship, self).__init__( **kwargs)
		self.source = imgStr
		self.size = 128 
		self.x = self.center_x
		self.y = self.center_y

	def setPos(self, xpos, ypos):
		self.x = xpos
		self.y = ypos