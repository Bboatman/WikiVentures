class Page(object):
	def __init__(self, url):
		self.url = url
		self.children = []

	def getUrl(self):
		return self.url

	def getChildren(self):
		return self.children