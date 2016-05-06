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
from kivy.uix.scrollview import ScrollView
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import AsyncImage
from kivy.graphics import Color, Rectangle
from kivy.uix.button import Button
from kivy.core.text import LabelBase
from kivy.core.audio import SoundLoader
from kivy.config import Config
from functools import partial

from wikipedia import page as wiki_page
from testPages import page as dummy_page
from wikipedia import random as random_page
from wikipedia import DisambiguationError

from random import sample
from spaceship import *
from system import *
from controller import *
from collider import Collider

Config.set('graphics','resizable',0) #don't make the app re-sizeable
Window.clearcolor = (0,0,0,1.0) #this fixes drawing issues on some phones

LabelBase.register(name='astron boy',  
                   fn_regular='./assets/astron boy.ttf')

LabelBase.register(name='joystix monospace',  
                   fn_regular='./assets/joystix monospace.ttf')

sound = SoundLoader.load('./assets/wikiverseTune.wav')
tutorial_mode = False
 

class Game(Widget):
    '''
    The main widget class that contains the game, the game loop and runs everything
    '''

    def __init__(self, **kwargs):
        super(Game, self).__init__(**kwargs)
        self.set_gamemode()
        self.path = [self.source]
        self.system = System(page(self.source))
        self.collider = Collider()
        self.player = Spaceship()
        self.add_widget(self.system.star)

        for planet in self.system.planets:
            self.add_widget(planet)

        self.controller = Controller(self.player)
        self.add_widget(self.player)

        Clock.schedule_interval(self.update, 1.0/60.0)



    def set_gamemode(self):
        global page
        if tutorial_mode:
            self.source = 'Pickled Cucumber'
            self.destination = 'Jesus'
            page = dummy_page
        else:
            page = wiki_page
            try:
                self.source = random_page()
                page(self.source)
            except DisambiguationError as disambig:
                strList = str(disambig)
                optionArr = strList.split("\n")
                self.source = wiki_page(optionArr[1])

            self.destination = sample(['Jesus', 'Kevin Bacon', 'Hitler', 'Prince (musician)', 'Game of Thrones', 'Computer science', 'Horse', 'United States', 'Marlon Brando', 'Murder', 'Wiki', 'Facebook', 'SpaceX', 'NASA'], 1)[0]
           
 
 
    def update(self,dt):
        '''
        This update function is the main update function for the game
        All of the game logic has its origin here
        dt - The change in time between updates of the game logic
        '''
        
        self.player.update(dt)
        self.system.update(dt)
        self.controller.update(dt)

    def remake_system(self, title = 'notta_page'):
        self.parent.remove_widget(self.parent.parent.parent.page_summary_button)
        for planet in self.system.planets:
            self.remove_widget(planet)
        self.remove_widget(self.system.star)
        if title == 'notta_page':
            jump_back = -2 if len(self.path) > 1 else -1
            self.system = System(page(self.path[jump_back]))
            if jump_back < -1: self.path.pop(-1)
        elif title == self.destination:
            self.parent.parent.parent.parent.current = 'winning_screen'
        else:
            try:
                newPage = page(title)
            except DisambiguationError as disambig:
                strList = str(disambig)
                optionArr = strList.split("\n")
                newPage = page(optionArr[1])
            self.system = System(newPage)
            self.path.append(title)       
        self.add_widget(self.system.star)
        for planet in self.system.planets:
            self.add_widget(planet)
        self.system.star.setPos(self.parent.parent.width/2, self.parent.parent.height/2)
        self.player.pos = self.system.star.pos

        page_summary = self.system.summary.split('\n')
        self.parent.parent.parent.page_summary_popup = PageSummaryPopup(
            title=self.system.title,
            content=Label(text=page_summary[0], text_size=(400, None)),
            size_hint=(None, None),
            size=(450, 450))
        self.parent.parent.parent.page_summary_button = Button(
            size_hint=(0.0025, 0.0005),
            pos=(self.parent.parent.parent.scrollview.size[0]/2+100, self.parent.parent.parent.scrollview.size[1]/2-40),
            text='page summary')
        self.parent.parent.parent.page_summary_button.bind(on_press=self.parent.parent.parent.page_summary_popup .open)
        self.parent.add_widget(self.parent.parent.parent.page_summary_button)


class MenuScreen(Screen):
    '''
    Opening menu screen
    '''
    pass

class GameScreen(Screen):
    '''
    Screen where game is played
    '''
    def on_enter(self):
        try:
            self.game.set_gamemode()
            self.game.remake_system(self.game.source)
            self.game.path = [self.game.source]
            self.floatlayout.remove_widget(self.endDestination)
        except AttributeError:
            self.game = Game()
            self.scrollview = ScrollView(
                size=(50000, 50000),
                size_hint=(None, None))
            self.floatlayout = FloatLayout()

            self.game.system.star.setPos(self.scrollview.width/2, self.scrollview.height/2)
            self.game.player.pos = self.game.system.star.pos
            
            self.floatlayout.add_widget(self.game)
            self.scrollview.add_widget(self.floatlayout)
            self.add_widget(self.scrollview)

            self.scrollview.do_scroll = True       
            self.game.player.bind(pos=self.scroll_to_player_cb)
            Clock.schedule_once(self.bump, 0.0001)

        self.endDestination = Label(pos=(Window.width/4-200, Window.height/4-200),
            text = 'Find your way to the\n"'+self.game.destination+'" wiki system, Cadet.')
        self.floatlayout.add_widget(self.endDestination)
            
        self.page_summary_popup = PageSummaryPopup(
            title=self.game.system.title,
            content=Label(text=self.game.system.summary, text_size=(400, None)),
            size_hint=(None, None),
            size=(450, 450))

        self.page_summary_button = Button(
            size_hint=(0.0025, 0.0005),
            pos=(self.scrollview.size[0]/2+100, self.scrollview.size[1]/2-40),
            text='page summary')
        self.page_summary_button.bind(on_press=self.page_summary_popup.open)
        self.floatlayout.add_widget(self.page_summary_button)

    def scroll_to_player_cb(self, player, pos):
        self.scrollview.x, self.scrollview.y = -(player.x - Window.width/2), -(player.y - Window.height/2)

    def bump(self, dt):
        '''
        here's a little bump on the player to force rendering of the screen, 
        it's scheduled to occur a millisecond after everything is loaded
        '''
        self.game.player.x += 1


class PageSummaryPopup(Popup):
    pass
    '''
    def __init__(self, page, **kwargs):
        #super(PageSummary, self).__init__( **kwargs)
        self.page = page
        self.title = self.page.title
        self.content = Label(text="This is a summary")
    '''

class PreTutorialScreen(Screen):
    '''
    Gives player option to read directions or to play gmae
    '''
    pass

class TutorialScreen(Screen):
    '''
    Tutuorial screen displays directions for game play
    '''
    pass

class MissionControlScreen(Screen):
    '''
    Mission control screen tells user end target
    '''
    pass

class WinningScreen(Screen):
    '''
    Winning screen displays when you reach the destination page
    '''
    pass

class TutorialMissionControlScreen(Screen):
    '''
    Mission Control for tutorial mode
    '''
    pass
        
class ClientApp(App):
    screen_manager = ObjectProperty(None)
    ''' 
    The root widget canvas upon which the game is drawn
    Because this named ClientApp, the kv file needs to be client.kv
    '''
    def build(self):
        ClientApp.screen_manager = ScreenManager()
        self.screen_manager.bind(current = set_tutorial_mode)

        ms = MenuScreen(name='menu_screen')
        mcs = MissionControlScreen(name = 'missionControl_screen')
        gs = GameScreen(name='game_screen')
        pts = PreTutorialScreen(name='pretutorial_screen')
        ts = TutorialScreen(name='tutorial_screen')
        ws = WinningScreen(name='winning_screen')
        tms = TutorialMissionControlScreen(name='tutorialMissionControl_screen')
 
        self.screen_manager.add_widget(ms)
        self.screen_manager.add_widget(pts)
        self.screen_manager.add_widget(ts)
        self.screen_manager.add_widget(gs)
        self.screen_manager.add_widget(mcs)
        self.screen_manager.add_widget(ws)
        self.screen_manager.add_widget(tms)
        
        sound.loop = True
        if sound:
            sound.play()

        return self.screen_manager

def set_tutorial_mode(instance, value):
    global tutorial_mode
    if value == 'tutorial_screen':
        tutorial_mode = True
    elif value == 'missioncontrol_screen' and not tutorial_mode:
        tutorial_mode = False
    elif value == 'menu_screen':
        tutorial_mode = False

if __name__ == '__main__' :
    ClientApp().run()