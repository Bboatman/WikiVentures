from widgetrenderer import *
from kivy.properties import NumericProperty


class Body(WidgetRenderer):
	theta = NumericProperty(0)
	magnitude = NumericProperty(100)
	speed = NumericProperty(100)