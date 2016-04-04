from wikipedia import page
from body import Body
from subsystem import SubSystem
from kivy.core.window import Window
from string import ascii_lowercase as LETTERS 

class System(SubSystem):
	def __init__(self, title):
		self.page = page(title)
		self.sections = {}
		for letter in LETTERS:
			links = []
			for link in self.page.links:
				if link[0].lower() == letter:
					links.append(link)
			if len(links) > 0:
				self.sections[letter] = links
		planet_names = sorted(list(self.sections.keys()))
		i = 0
		for key in planet_names:
			planet_names[i] = key + ' : ' + str(len(self.sections[key]))
			i += 1
			print(key)
		print(planet_names)
		super(System, self).__init__(planet_names, title)

	def update(self, dt):
		for planet in self.planets:
			planet.orbit((self.star.x + 120, self.star.y + 120), dt)

	def centerSystem(self):
		self.star.setPos(Window.width/2-128, Window.height/2-128)