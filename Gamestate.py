
from WikiArea import *

class Gamestate(object):
	def __init__(self, source = 'Picked Cucumber', target = 'Jesus', debugState = False):
		self.source = source
		self.target = target
		self.currentArea = WikiArea(source)
		self.path = [source]
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> eedc6093834c052ad096358cfa6c1a62b20a3044
		self.win = False

	def addNewPageToPath(self, page):
		newPage = Page(THEURL) #need to fix this part
		self.path.append(newPage)
		return null
=======
>>>>>>> 450226eca46ea9a5626b101a1b056533023bab1a
=======
>>>>>>> 013e724a941ccad5dc97bc8f2b1789580e240d78
=======
		self.debugState = debugState
>>>>>>> 1fbbcc4f7d223891bbd1b8c73afcd628d8d45c65

	def isWin(self):
		# Check if this page is a win
		if self.path[-1] == self.target:
			return True
		return False

	def isDebug(self):
		return self.debugState

	def getPath(self):
		return self.path

	def getCurrentPage(self):
		# Return last page of the path
		return self.path[-1]

	def getNumClicks(self):
		return len(self.path) - 1

	def getTarget(self):
		return self.target

	def addToPath(self, destination):
		possibleDestinations = self.currentArea.getChildren()
		if destination in possibleDestinations:
			self.path.append(destination)
			self.currentArea = WikiArea(destination)
			return True
		else:
			return False