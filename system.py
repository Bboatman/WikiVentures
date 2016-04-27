from wikipedia import page
from subsystem import SubSystem
from kivy.core.window import Window
from string import ascii_lowercase as LETTERS 

class System(SubSystem):
	def __init__(self, title):
		self.page = page(title)
		# self.sections = {}
		# for letter in LETTERS:
		# 	links = []
		# 	for link in self.page.links:
		# 		if link[0].lower() == letter:
		# 			links.append(link)
		# 	if len(links) > 0:
		# 		self.sections[letter] = links
		# planet_names = sorted(list(self.sections.keys()))
		# i = 0
		# for key in planet_names:
		# 	planet_names[i] = key + ' : ' + str(len(self.sections[key]))
		# 	i += 1
		super(System, self).__init__(self.page.links, title)
