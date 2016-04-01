import kivy
kivy.require('1.9.1')

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.core.window import Window
from kivy.clock import Clock
from spaceship import *
from system import *
from spaceship import *

from kivy.config import Config
Config.set('graphics','resizable',0) #don't make the app re-sizeable
Window.clearcolor = (0,0,0,1.) #this fixes drawing issues on some phones

class Game(Widget):
    '''
    The main widget class that contains the game, the game loop and runs everything
    '''
    def __init__(self, **kwargs):
        super(Game, self).__init__(**kwargs)

        self.system = System('Macalester College')
        self.add_widget(self.system.star)
        for planet in self.system.planets:
            self.add_widget(planet)
        self.player = Spaceship()
        self.player.setPos(Window.width/4, Window.height/4)
 
    def update(self,dt):
        '''
        This update function is the main update function for the game
        All of the game logic has its origin here
        dt - The change in time between updates of the game logic
        '''
        self.system.update(dt)
        self.player.setPos(Window.width/4, Window.height/4)
        self.system.centerSystem()

        
class ClientApp(App):
    ''' 
    The root widget canvas upon which the game is drawn
    Because this named ClientApp, the kv file needs to be client.kv
    '''
    def build(self):
        parent = Widget() #this is an empty holder for buttons, etc
        app = Game()        
        #Start the game clock (runs update function once every (1/60) seconds
        Clock.schedule_interval(app.update, 1.0/60.0) 
        parent.add_widget(app) #use this hierarchy to make it easy to deal w/buttons
        return parent

if __name__ == '__main__' :
    ClientApp().run()