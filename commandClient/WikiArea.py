import wikipedia

class WikiArea():
	def __init__(self, title):
		self.title = title
		self.page = wikipedia.page(title)
		self.children = self.page.links

	def getTitle(self):
		return self.title

	def getChildren(self):
		return self.page.links

	def update(self):
