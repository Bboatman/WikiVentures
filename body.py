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
    imgPath = StringProperty("")

    def __init__(self, title, order, **kwargs):
        super(Body, self).__init__( **kwargs)
        self.theta = randrange(0, 360)
        self.magnitude = order * 100 + 100
        self.speed = randrange(38, 42) * 150.0 / self.magnitude
        self.label = Label(text = title, size = (self.width-10, self.height/3), font_size = 10)
        self.add_widget(self.label)
        pickAsset = randrange(1, 6)
        self.imgPath = './assets/planet' + str(pickAsset) + '.png'

        self.size = 90

    def update(self, starPos, dt):
        '''
        Move the body in orbit around its star's position
        starPos - (x,y) tuple of the center point of the star
        '''
        self.theta = (self.theta + self.speed * dt) % 360.0
        self.x = (math.cos(math.radians(self.theta)) * self.magnitude + starPos[0]) - self.size/2
        self.y = (math.sin(math.radians(self.theta)) * self.magnitude + starPos[1]) - self.size/2
        self.label.x = self.x
        self.label.y = self.y
    def on_collide(self, other_widget):
        if isinstance(other_widget, Spaceship) and other_widget.warp:
            other_widget.warp_deactivate()
            self.parent.remake_system(self.label.text)

    def setPos(self, xpos, ypos):
        self.x = xpos
        self.y = ypos
        self.label.x = self.x - self.label.width/2
        self.label.y = self.y

class Star(Collidable):
    size = NumericProperty(0)
    x = NumericProperty(0)
    y = NumericProperty(0)
    imgPath = StringProperty('')

    def __init__(self, title, **kwargs):
        super(Star, self).__init__(**kwargs)
        self.label = Label(text = title, size = (self.width-10, self.height/3), font_size = 10)
        self.label.font_size = 30
        self.label.pos = (self.width/2-5, self.height/6)
        self.add_widget(self.label)
        self.size = 240
        pickAsset = randrange(1, 4)
        self.imgPath = './assets/sun' + str(pickAsset) + '.png'

    def setPos(self, xpos, ypos):
        self.x = xpos
        self.y = ypos
        self.label.x = self.x
        self.label.y = self.y