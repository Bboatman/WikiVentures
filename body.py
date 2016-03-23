import math

from random import randrange
from widgetrenderer import *
from kivy.properties import NumericProperty
from kivy.properties import StringProperty
from kivy.uix.label import Label

class Body(WidgetRenderer):
	def __init__(self, imgStr, title, **kwargs):
		super(Body, self).__init__(imgStr, **kwargs)
		self.theta = randrange(0, 360)
		self.magnitude = randrange(60, 600, 20)
		self.speed = randrange(20, 70)
		self.label = Label(text = title)
		self.add_widget(self.label)
	def move(self, starPos, dt):
		self.theta = self.theta + self.speed * dt
		self.x = math.cos(math.radians(self.theta)) * self.magnitude + starPos[0]
		self.y = math.sin(math.radians(self.theta)) * self.magnitude + starPos[1]
		self.label.x = self.x
		self.label.y = self.y

	def setPos(self, xpos, ypos):
		self.x = xpos
		self.y = ypos
		self.label.x = self.x
		self.label.y = self.y


