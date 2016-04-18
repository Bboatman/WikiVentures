from math import degrees

from kivy.uix.widget import Widget
from kivy.properties import NumericProperty
from kivy.properties import StringProperty
from kivy.core.window import Window

class Spaceship(Widget):

    ''' 
    Player's spaceship used to travel to other planets.
    '''
    size = NumericProperty(0)
    x = NumericProperty(0)
    y = NumericProperty(0)

    def __init__(self, **kwargs):
        super(Spaceship, self).__init__(**kwargs)
        self.size = 50
        self.speed = 100
        self.dir_x = 0
        self.dir_y = 0
        self.angle = 0
        self.x = self.center_x
        self.y = self.center_y
        # self._keyboard = Window.request_keyboard(self._keyboard_closed, self)
        # self._keyboard.bind(on_key_down=self._on_keyboard_down)

    def setPos(self, xpos, ypos):
        self.x = xpos
        self.y = ypos

    def update(self, dt):
        self.x += (self.speed * self.dir_x) * dt
        self.y += (self.speed * self.dir_y) * dt
        #   print(degrees(self.angle))

    # def _keyboard_closed(self):
    #     self._keyboard.unbind(on_key_down=self._on_keyboard_down)
    #     self._keyboard = None

    # def _on_keyboard_down(self, keyboard, keycode, text, modifiers):
    #     if keycode[1] == 'right':
    #         self.x+=10
    #     elif keycode[1] == 'left':
    #         self.x-=10
    #     elif keycode[1] == 'up':
    #         self.y+=10
    #     elif keycode[1] == 'down':
    #         self.y-=10
    #     return True

    # don't forget to add rotation, movement
