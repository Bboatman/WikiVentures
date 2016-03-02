import sys
import unittest
sys.path.append('./..') #Add the Wikiventures parent folder to the path
from Page import *

# Documentation on testing!
# https://docs.python.org/3/library/unittest.html

class TestPageMethods(unittest.TestCase):
	def setUp(self):
		self.test = Page('Sample')

	def test_getUrl(self):
		self.assertEqual(self.test.getUrl(), 'Sample')

	def test_getChildren(self):
		self.assertEqual(self.test.getChildren(), [])


if __name__ == '__main__':
    unittest.main()