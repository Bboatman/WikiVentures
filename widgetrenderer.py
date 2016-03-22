import kivy
kivy.require('1.7.2')

from kivy.uix.widget import Widget
from kivy.core.window import Window
from kivy.graphics import Rectangle

class WidgetRenderer(Widget):
    #This widget is used to draw all of the objects on the screen
    #it handles the following:
    #widget movement, size, positioning
    #whever a WidgetDrawer object is created, an image string needs to be specified
    #example:    wid - WidgetDrawer('./image.png')
 
    #objects of this class must be initiated with an image string
	#;You can use **kwargs to let your functions take an arbitrary number of keyword arguments
	#kwargs ; keyword arguments
    def __init__(self, imageStr, **kwargs): 
        super().__init__(**kwargs) #this is part of the **kwargs notation
		#if you haven't seen with before, here's a link <a href="http://effbot.org/zone/python-with-statement.html">http://effbot.org/zone/python-with-statement.html</a>     
        with self.canvas: 
			#setup a default size for the object
            self.size = (Window.width*.002*25, Window.width*.002*25) 
			#this line creates a rectangle with the image drawn on top
            self.rect_bg = Rectangle(source=imageStr,pos=self.pos,size = self.size) 
			#this line calls the update_graphics_pos function every time the position variable is modified
            self.bind(pos=self.update_graphics_pos) 
            self.x = self.center_x
            self.y = self.center_y
			#center the widget 
            self.pos = (self.x,self.y) 
			#center the rectangle on the widget
            self.rect_bg.pos = self.pos 
 
    def update_graphics_pos(self, instance, value):
		#if the widgets position moves, the rectangle that contains the image is also moved
        self.rect_bg.pos = value  

	#use this function to change widget size        
    def setSize(self,width, height): 
        self.size = (width, height)

 	#use this function to change widget position    
    def setPos(xpos,ypos):
        self.x = xpos
        self.y = ypos