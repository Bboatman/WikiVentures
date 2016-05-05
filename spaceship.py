from kivy.uix.widget import Widget
from kivy.properties import NumericProperty
from kivy.properties import StringProperty
from kivy.properties import BooleanProperty
from kivy.core.window import Window
from kivy.graphics import Ellipse
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
        self.frame_count = 0

    def setPos(self, xpos, ypos):
        self.x = xpos
        self.y = ypos

    def update(self, dt):
        if (self.v_x or self.v_y) and (self.frame_count % 3 == 0):
            self.parent.add_widget(Trail(pos = (self.x + self.width/4, self.y + self.height/4)))
            self.frame_count = 0
        if self.dir_x == 0 and abs(self.v_x) > 0:
            self.v_x  -= abs(self.v_x)/self.v_x * 10
        elif abs(self.v_x) < 300:
            self.v_x += self.dir_x * 10
        if self.dir_y == 0 and abs(self.v_y) > 0:
            self.v_y  -= abs(self.v_y)/self.v_y * 10
        elif abs(self.v_y) < 300:
            self.v_y += self.dir_y * 10
        self.x += self.v_x * dt
        self.y += self.v_y * dt
        self.frame_count += 1

    def warp_activate(self):
        self.warp = True
        Clock.schedule_once(self.warp_deactivate, 1)

    def warp_deactivate(self, dt = 0):
        if self.warp:
            self.warp = False

class Trail(Widget):
    expired = BooleanProperty(False)
    def __init__(self, **kwargs):
        super(Trail, self).__init__(**kwargs)
        Clock.schedule_once(self.expire, 1.3)
        self.bind(expired= self.clean_up_self_cb)
    def expire(self, dt):
        self.expired = True
    def clean_up_self_cb(self, instance, value):
        if value and self.parent:
            self.parent.remove_widget(self)
            del self