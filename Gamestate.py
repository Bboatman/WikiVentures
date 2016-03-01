class Gamestate(object):
	def __init__(self):
		self.source = "Pickles"
		self.target = "Jesus"
		self.path = []
		self.win = False

	def addNewPageToPath(self):
		# Add a page to the path
		return null

	def isWin(self):
		# Check if this page is a win
		return False

	def getCurrentPage(self):
		# Return last page of the path
		return ""

	def getNumClicks(self):
		return len(self.path)

	def getTarget(self):
		return self.target