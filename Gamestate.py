class Gamestate(object):
	def __init__(self):
		self.numClicks = 0
		self.source = "Pickles"
		self.target = "Jesus"
		self.currentPage = self.source
		self.win = False

	def updateCount(self):
		# Do stuff here
		return null

	def isWin(self):
		# Do stuff here
		return False

	def setCurrentPage(self):
		return ""

	def getNumClicks(self):
		return self.numClicks

	def getTarget(self):
		return self.target