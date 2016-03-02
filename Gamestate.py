
from WikiArea import *

class GameState(object):
	def __init__(self, source = 'Picked Cucumber', target = 'Jesus'):
		self.source = source
		self.target = target
		self.currentArea = WikiArea(source)
		self.path = [source]

	def isWin(self):
		# Check if this page is a win
		if self.path[-1] == self.target:
			return True
		return False

	def getPath(self):
		return self.path

	def getCurrentPage(self):
		# Return last page of the path
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