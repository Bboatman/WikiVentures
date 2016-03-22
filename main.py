import kivy
kivy.require('1.7.2')
 
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.core.window import Window
from kivy.clock import Clock

from system import *

from kivy.config import Config
Config.set('graphics','resizable',0) #don't make the app re-sizeable
#Graphics fix
#this fixes drawing issues on some phones
Window.clearcolor = (0,0,0,1.) 

class Game(Widget):
    #this is the main widget that contains the game. 
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        l = Label(text='WikiVentures') #give the game a title
        l.x = Window.width/2 - l.width/2
        l.y = Window.height*0.8
        self.add_widget(l) #add the label to the screen

        self.system = System()
        self.add_widget(self.system.star)
        for planet in self.system.planets:
            self.add_widget(planet)
 
    def update(self,dt):
        #This update function is the main update function for the game
        #All of the game logic has its origin here
        self.system.update(dt)

        
class ClientApp(App):
    def build(self):
        #this is where the root widget goes
        #should be a canvas
        parent = Widget() #this is an empty holder for buttons, etc
 
        app = Game()        
        #Start the game clock (runs update function once every (1/60) seconds
        Clock.schedule_interval(app.update, 1.0/60.0) 
        parent.add_widget(app) #use this hierarchy to make it easy to deal w/buttons
        return parent

if __name__ == '__main__' :
    ClientApp().run()