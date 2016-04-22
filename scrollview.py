from functools import partial
from kivy.animation import Animation

from kivy.uix.stencilview import StencilView
from kivy.properties import NumericProperty, BooleanProperty, AliasProperty, \
    ObjectProperty, ListProperty, ReferenceListProperty, OptionProperty

class ScrollView(StencilView):

	scroll_x = NumericProperty(0.)

	scroll_y = NumericProperty(1.)

	do_scroll_x = BooleanProperty(True)

	do_scroll_y = BooleanProperty(True)

	def get_do_scroll(self):
		return (self.do_scroll_x, self.do_scroll_y)

	def set_do_scroll(self, value):
		if type(value) in (list, tuple):
			self.do_scroll_x, self.do_scroll_y = value
		else:
			self.do_scroll_x = self.do_scroll_y = bool(value)

	do_scroll = AliasProperty(get_do_scroll, set_do_scroll, bind=('do_scroll_x', 'do_scroll_y'))