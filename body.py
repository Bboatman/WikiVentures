import math
from kivy.uix.widget import Widget
from random import randrange
from kivy.properties import NumericProperty
from kivy.properties import StringProperty
from kivy.properties import BooleanProperty
from kivy.uix.label import Label

from collider import Collidable
from spaceship import Spaceship

class Body(Collidable):
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
		self.speed = randrange(20, 70)
		
		self.label = Label(text = title, pos = (self.center_x, self.center_y))
		self.add_widget(self.label)

		self.source = imgStr
		self.size = 50 if imgStr == './assets/planet.png' else 256

	def orbit(self, starPos, dt):
		'''
		Move the body in orbit around its star's position
		starPos - (x,y) tuple of the center point of the star
		'''
		self.theta = self.theta + self.speed * dt
		self.x = int(math.cos(math.radians(self.theta)) * self.magnitude + starPos[0])
		self.y = int(math.sin(math.radians(self.theta)) * self.magnitude + starPos[1])
		self.label.x = self.x
		self.label.y = self.y
	def on_collide(self, other_widget):
		if isinstance(other_widget, Spaceship) and other_widget.warp:
			#print(self.parent.remake_system)
			other_widget.warp_deactivate()
			self.parent.remake_system(self.label.text)

	def setPos(self, xpos, ypos):
		self.x = xpos
		self.y = ypos
		self.label.x = self.x
		self.label.y = self.y