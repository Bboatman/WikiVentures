import random
from math import degrees
from aiBrain import SubsumptionBrain
from kivy.uix.widget import Widget
from kivy.properties import NumericProperty
from kivy.properties import StringProperty
from kivy.core.window import Window

class Enemy(Widget):

    ''' 
    Enemy ship with subsumption AI
    '''
    size = NumericProperty(0)
    x = NumericProperty(0)
    y = NumericProperty(0)

    def __init__(self, **kwargs):
        super(Enemy, self).__init__(**kwargs)
        self.size = 50
        self.baseSpeed = random.randint(80, 110)
        self.dir_x = 0
        self.dir_y = 0
        self.angle = 0
        self.x = self.center_x
        self.y = self.center_y
        self.brain = SubsumptionBrain(self)

    def setPos(self, xpos, ypos):
        self.x = xpos
        self.y = ypos

    def update(self, dt):
        self.brain.step(dt)