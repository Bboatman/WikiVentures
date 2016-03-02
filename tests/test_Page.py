import sys
import unittest
sys.path.append('./..') #Add the Wikiventures parent folder to the path
from Page import *

# Documentation on testing!
# https://docs.python.org/3/library/unittest.html

class TestPageMethod(unittest.TestCase):
	def setUp(self):
		self.testPage = Page('Sample')

	def test_getUrl(self):
		self.assertEqual(self.testPage.getUrl(), 'Sample')

	def test_getChildren(self):
		self.assertEqual(self.testPage.getChildren(), [])


if __name__ == '__main__':
    unittest.main()