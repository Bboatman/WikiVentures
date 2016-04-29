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
from kivy.graphics import Rectangle
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.scrollview import ScrollView
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.image import AsyncImage
from kivy.graphics import Color, Rectangle
from kivy.uix.button import Button

from enemyShip import *
from spaceship import *
from system import *
from controller import *
from collider import Collider
from scrollFeatures import *

from kivy.config import Config
Config.set('graphics','resizable',0) #don't make the app re-sizeable
Window.clearcolor = (0,0,0,1.0) #this fixes drawing issues on some phones

 
class Game(Widget):
    '''
    The main widget class that contains the game, the game loop and runs everything
    '''
    def __init__(self, **kwargs):
        super(Game, self).__init__(**kwargs)
        self.source = 'Macalester College'
        self.destination = 'Steve Jobs'
        self.path = [self.source]
        self.system = System('Macalester College')
        self.collider = Collider()
        self.player = Spaceship()
        self.player.setPos(Window.width/4, Window.height/4)
        self.add_widget(self.system.star)
        for planet in self.system.planets:
            self.add_widget(planet)

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
        self.enemy.update(dt)
        self.player.update(dt)
        self.controller.update(dt)
        self.system.centerSystem()
        self.parent.scroll_to(self.player)

    def remake_system(self, title = 'notta_page'):
        for planet in self.system.planets:
            self.remove_widget(planet)
        self.remove_widget(self.system.star)
        if title == 'notta_page':
            jump_back = -2 if len(self.path) > 1 else -1
            self.system = System(self.path[jump_back])
            print('jump_back')
            if jump_back < -1: self.path.pop(-1)
        else:
            self.system = System(title) 
            self.path.append(title)       
        self.add_widget(self.system.star)
        for planet in self.system.planets:
            self.add_widget(planet)
        self.player.pos = self.system.star.pos
        print(self.path)


class MenuScreen(Screen):
    options_popup = ObjectProperty(None)

    def show_popup(self):
        self.options_popup = OptionsPopup()
        self.options_popup.open()

class GameScreen(Screen):
    def on_enter(self):
        self.scrollview = ScrollView()
        #self.scrollview.viewport_size = (Window.width, Window.height)
        self.floatlayout = FloatLayout(
            size=(100000, 100000),
            size_hint=(None, None))
        #print self.floatlayout.size_hint
        self.game = Game()


        self.scrollview.add_widget(self.game)
        self.floatlayout.add_widget(self.scrollview)

        self.scrollview.do_scroll = True
        self.add_widget(self.floatlayout)
        Window.show_cursor = False
        self.game.player.bind(pos=self.scroll_to_player_cb)

    def scroll_to_player_cb(self, player, pos):
        #self.game.x, self.game.y = -(player.x - Window.width/2), -(player.y - Window.height/2)
        self.scrollview.x, self.scrollview.y = -(player.x - Window.width/2), -(player.y - Window.height/2)




class TutorialScreen(Screen):
    pass

class PreTutorialScreen(Screen):
    pass

class OptionsPopup(Popup):
    pass

class MissionControlScreen(Screen):
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
        pts = PreTutorialScreen(name="pretutorial_screen")
        ts = TutorialScreen(name="tutorial_screen")
        mcs = MissionControlScreen(name="missioncontrol_screen")

        self.screen_manager.add_widget(ms)
        self.screen_manager.add_widget(pts)
        self.screen_manager.add_widget(ts)
        self.screen_manager.add_widget(gs)
        self.screen_manager.add_widget(mcs)

        #parent = Widget() #this is an empty holder for buttons, etc
        #app = Game()        
        #Start the game clock (runs update function once every (1/60) seconds
        #Clock.schedule_interval(app.update, 1.0/60.0) 
        #parent.add_widget(app) #use this hierarchy to make it easy to deal w/buttons
        return self.screen_manager

if __name__ == '__main__' :
    ClientApp().run()