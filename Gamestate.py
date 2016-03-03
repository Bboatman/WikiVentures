
from WikiArea import *

class Gamestate(object):
	def __init__(self, source = 'Picked Cucumber', target = 'Jesus', debugState = False):
		self.source = source
		self.target = target
		self.currentArea = WikiArea(source)
		self.path = [source]
		self.debugState = debugState

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