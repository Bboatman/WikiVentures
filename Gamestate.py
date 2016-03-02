<<<<<<< HEAD
from Page import *
class Gamestate(object):
	def __init__(self):
		self.source = "Pickles"
		self.target = "Jesus"
		self.path = []
=======
from WikiArea import *

class GameState(object):
	def __init__(self, source = 'Pickles', target = 'Jesus'):
		self.source = source
		self.target = target
		self.currentArea = WikiArea(source)
		self.path = [source]
>>>>>>> eedc6093834c052ad096358cfa6c1a62b20a3044
		self.win = False

	def addNewPageToPath(self, page):
		newPage = Page(THEURL) #need to fix this part
		self.path.append(newPage)
		return null

	def isWin(self):
		# Check if this page is a win
		if getCurrentPage == self.target:
			return True
		return False

	def getCurrentPage(self):
<<<<<<< HEAD
=======
		# Return last page of the path
>>>>>>> eedc6093834c052ad096358cfa6c1a62b20a3044
		return self.path[-1]

	def getNumClicks(self):
		return len(self.path)

	def getTarget(self):
		return self.target

	def gameIsWon(self):
		return self.win

	def winGame(self):
		self.win = True

	def addToPath(self, destination):
		possibleDestinations = self.currentArea.getChildren()
		if destination in possibleDestinations:
			self.path.append(destination)
			self.currentArea = WikiArea(destination)