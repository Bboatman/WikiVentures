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

	def __init__(self, **kwargs):
		super(Spaceship, self).__init__( **kwargs)
		self.size = 128
		self.x = self.center_x
		self.y = self.center_y

	def move(self):
		return null

	def rotate(self):
		return null

	def setPos(self, xpos, ypos):
		self.x = xpos
		self.y = ypos