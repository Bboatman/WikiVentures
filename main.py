import kivy
kivy.require('1.9.1')

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.core.window import Window
from kivy.clock import Clock
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import ObjectProperty
from kivy.uix.popup import Popup
from enemyShip import *
from spaceship import *
from system import *
from controller import *

from kivy.config import Config
Config.set('graphics','resizable',0) #don't make the app re-sizeable
Window.clearcolor = (0,0,0,1.0) #this fixes drawing issues on some phones
 
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
        self.controller = Controller(self.player)
        self.add_widget(self.player)

        self.enemy = Enemy()
        self.enemy.setPos(Window.width/2, Window.width/2)
        self.add_widget(self.enemy)

        Clock.schedule_interval(self.update, 1.0/60.0)
 
    def update(self,dt):
        '''
        This update function is the main update function for the game
        All of the game logic has its origin here
        dt - The change in time between updates of the game logic
        '''
        self.system.update(dt)
        self.player.update(dt)
        self.enemy.update(dt)
        self.controller.update(dt)
        self.system.centerSystem()


class MenuScreen(Screen):
    options_popup = ObjectProperty(None)

    def show_popup(self):
        self.options_popup = OptionsPopup()
        self.options_popup.open()

class GameScreen(Screen):
    game_engine = ObjectProperty(None)

    def on_enter(self):
        self.game_engine.__init__(self)

class OptionsPopup(Popup):
    pass
        
class ClientApp(App):
    screen_manager = ObjectProperty(None)
    ''' 
    The root widget canvas upon which the game is drawn
    Because this named ClientApp, the kv file needs to be client.kv
    '''
    def build(self):
        ClientApp.screen_manager = ScreenManager()

        ms = MenuScreen(name="menu_screen")
        gs = GameScreen(name="game_screen")

        self.screen_manager.add_widget(ms)
        self.screen_manager.add_widget(gs)
        #parent = Widget() #this is an empty holder for buttons, etc
        #app = Game()        
        #Start the game clock (runs update function once every (1/60) seconds
        #Clock.schedule_interval(app.update, 1.0/60.0) 
        #parent.add_widget(app) #use this hierarchy to make it easy to deal w/buttons
        return self.screen_manager

if __name__ == '__main__' :
    ClientApp().run()