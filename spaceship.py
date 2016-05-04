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
    rotation = NumericProperty(0)

    warp = BooleanProperty(False)

    def __init__(self, **kwargs):
        super(Spaceship, self).__init__(**kwargs)
        self.size = 50
        self.dir_x = 0
        self.dir_y = 0
        self.v_x = 0 
        self.v_y = 0
        self.rotation = 0
        self.x = self.center_x
        self.y = self.center_y

    def setPos(self, xpos, ypos):
        self.x = xpos
        self.y = ypos

    def update(self, dt):
        if self.dir_x != 0 and self.v_x < 300:
            self.v_x += self.dir_x * 10
        elif self.dir_x == 0 and self.v_x != 0:
            self.v_x -= abs(self.v_x)/self.v_x * 10
        if self.dir_y != 0 and self.v_y < 300:
            self.v_y += self.dir_y * 10
        elif self.dir_y == 0 and self.v_y != 0:
            self.v_y -= abs(self.v_y)/self.v_y * 10
        self.x += self.v_x * dt
        self.y += self.v_y * dt

    def warp_activate(self):
        self.warp = True
        Clock.schedule_once(self.warp_deactivate, 1)

    def warp_deactivate(self, dt = 0):
        if self.warp:
            self.warp = False
