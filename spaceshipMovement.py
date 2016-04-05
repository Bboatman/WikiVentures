# from kivy.uix.widget import Widget
# from kivy.core.window import Window
# from kivy.properties import NumericProperty
# from kivy.properties import StringProperty
# from spaceship import *

# class spaceshipMovement(Widget):
#     '''
#     Sets up keyboard listeners and spaceship movement.
#     '''
#     x = NumericProperty(0)
#     y = NumericProperty(0)
#     player = Spaceship()

#     def __init__(self, arg):
#         super(key, self).__init__()
#         self.arg = arg

#     def __init__(self, **kwargs):
#         super(spaceshipMovement, self).__init__(**kwargs)
#         self._keyboard = Window.request_keyboard(self._keyboard_closed, self)
#         self._keyboard.bind(on_key_down=self._on_keyboard_down)

#     def _keyboard_closed(self):
#         self._keyboard.unbind(on_key_down=self._on_keyboard_down)
#         self._keyboard = None

#     def _on_keyboard_down(self, keyboard, keycode, text, modifiers):

#         if keycode[1] == 'right':
#             self.player.center_y += 10
#         elif keycode[1] == 'left':
#             self.player.center_y -= 10
#         elif keycode[1] == 'up':
#             self.player.center_y += 10
#         elif keycode[1] == 'down':
#             self.player.center_y -= 10
#         return True