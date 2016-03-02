class Gamestate(object):
	def __init__(self, source = 'Pickles', target = 'Jesus'):
		self.source = source
		self.target = target
		self.path = [source]
		self.win = False

	def addNewPageToPath(self):
		# Add a page to the path
		return null

	def isWin(self):
		# Check if this page is a win
		if getCurrentPage == self.target:
			return True
		return False

	def getCurrentPage(self):
		# Return last page of the path
		return self.path[-1]

	def getNumClicks(self):
		return len(self.path)

	def getTarget(self):
		return self.target

	def gameIsWon(self):
		return self.win

	def winGame(self):
		self.win = True