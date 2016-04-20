from math import degrees

from kivy.uix.widget import Widget
from kivy.properties import NumericProperty
from kivy.properties import StringProperty
from kivy.properties import BooleanProperty
from kivy.core.window import Window

from kivy.clock import Clock

from collider import Collidable

class Spaceship(Collidable):

    ''' 
    Player's spaceship used to travel to other planets.
    '''
    size = NumericProperty(0)
    x = NumericProperty(0)
    y = NumericProperty(0)

    warp = BooleanProperty(False)

    def __init__(self, **kwargs):
        super(Spaceship, self).__init__(**kwargs)
        self.size = 50
        self.speed = 200
        self.dir_x = 0
        self.dir_y = 0
        self.angle = 0
        self.x = self.center_x
        self.y = self.center_y
        
    def setPos(self, xpos, ypos):
        self.x = xpos
        self.y = ypos

    def update(self, dt):
        self.x += (self.speed * self.dir_x) * dt
        self.y += (self.speed * self.dir_y) * dt

    def warp_activate(self):
        self.warp = True
        print('warp activated')
        Clock.schedule_once(self.warp_deactivate, 1)

    def warp_deactivate(self, dt = 0):
        if self.warp:
            self.warp = False
            print('warp off')