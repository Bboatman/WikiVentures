import sys
import unittest
sys.path.append('./..')
from GameState import *

class TestGameStateMethod(unittest.TestCase):
	def setUp(self):
		this.gameState = GameState()

if __name__=='__main__':
	unittest.main()