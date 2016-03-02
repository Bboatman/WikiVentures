import wikipedia

class WikiArea(object):
	def __init__(self, title):
		self.title = title
		self.page = wikipedia.page(title)

	def getTitle(self):
		return self.title

	def getChildren(self):
		return self.page.links