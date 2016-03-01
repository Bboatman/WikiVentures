class Gamestate(object):
	def __init__(self):
		self.source = "Pickles"
		self.target = "Jesus"
		self.path = []
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
		return len(self.path)

	def getTarget(self):
		return self.target