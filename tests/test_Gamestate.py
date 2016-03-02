import sys
import unittest
sys.path.append('./..')
from Gamestate import *

class TestGamestateMethod(unittest.TestCase):
	def __init__(self, arg='-v'):
		super(TestGamestateMethod, self).__init__()
		self.arg = arg

if __name__=='__main__':
	unittest.main()
	