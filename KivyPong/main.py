from kivy.app import App
from kivy.uix.widget import Widget

class PongGame(widget):
	pass

class PongApp(app):
	def build(self):
		return PongGame()

if __name__ == '__main__':
	PongApp().run()