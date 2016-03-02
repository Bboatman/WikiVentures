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
	def __init__(self, source = 'Picked Cucumber', target = 'Jesus'):
		self.source = source
		self.target = target
		self.currentArea = WikiArea(source)
		self.path = [source]
<<<<<<< HEAD
>>>>>>> eedc6093834c052ad096358cfa6c1a62b20a3044
		self.win = False

	def addNewPageToPath(self, page):
		newPage = Page(THEURL) #need to fix this part
		self.path.append(newPage)
		return null
=======
>>>>>>> 450226eca46ea9a5626b101a1b056533023bab1a

	def isWin(self):
		# Check if this page is a win
		if self.path[-1] == self.target:
			return True
		return False

	def getPath(self):
		return self.path

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

	def winGame(self):
		self.win = True

	def addToPath(self, destination):
		possibleDestinations = self.currentArea.getChildren()
		if destination in possibleDestinations:
			self.path.append(destination)
			self.currentArea = WikiArea(destination)
			return True
		else:
			return False