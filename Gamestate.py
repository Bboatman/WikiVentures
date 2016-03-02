from Page import *
class Gamestate(object):
	def __init__(self):
		self.source = "Pickles"
		self.target = "Jesus"
		self.path = []
		self.win = False

	def addNewPageToPath(self, page):
		newPage = Page(THEURL) #need to fix this part
		self.path.append(newPage)
		return null

	def isWin(self):
		# Check if this page is a win
		return False

	def getCurrentPage(self):
		return self.path[-1]

	def getNumClicks(self):
		return len(self.path)

	def getTarget(self):
		return self.target