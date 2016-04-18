import sys
import unittest
from cStringIO import StringIO
from code_golf import palindrome
from code_golf import vectorAddition
from code_golf import mostFrequentCharacter
from code_golf import fizzBuzz

class testPalindrome(unittest.TestCase):
	def test_racecar(self):
		pal = palindrome("racecar")
		self.assertTrue(pal)

	def test_cat(self):
		pal = palindrome("cat")
		self.assertFalse(pal)

	def test_letters(self):
		pal = palindrome("aabbcd")
		self.assertFalse(pal)

	def test_L(self):
		pal = palindrome("l")
		self.assertTrue(pal)

	def test_sentence(self):
		pal = palindrome("this is a test")
		self.assertFalse(pal)

class testVectorAddition(unittest.TestCase):
	def test_one(self):
		a = [1,2,1]
		b = [1,2,4]
		theirs = vectorAddition(a,b)
		ans = [2,4,5]
		self.assertEqual(theirs, ans)

	def test_two(self):
		a = [3]
		b = [5]
		theirs = vectorAddition(a,b)
		ans = [8]
		self.assertEqual(theirs, ans)

	def test_three(self):
		a = [1]
		b = [1]
		theirs = vectorAddition(a,b)
		ans = [2]
		self.assertEqual(theirs, ans)

	def test_four(self):
		a = [1, 11]
		b = [2, 12]
		theirs = vectorAddition(a,b)
		ans = [3, 23]
		self.assertEqual(theirs, ans)

	def test_five(self):
		a = [-1, 0]
		b = [5, -1]
		theirs = vectorAddition(a,b)
		ans = [4, -1]
		self.assertEqual(theirs, ans)

class testMostFrequentCharacter(unittest.TestCase):
	def test_hello(self):
		theirs = mostFrequentCharacter("hello word")
		self.assertEqual('l', theirs)

	def test_poppins(self):
		theirs = mostFrequentCharacter("supercalifragilisticexpialdocious")
		self.assertEqual('i', theirs)

	def test_sentence(self):
		theirs = mostFrequentCharacter("i'm a sentence")
		self.assertEqual('e', theirs)

	def test_python(self):
		theirs = mostFrequentCharacter("python rocks")
		self.assertEqual('o', theirs)

class Capturing(list):
    def __enter__(self):
        self._stdout = sys.stdout
        sys.stdout = self._stringio = StringIO()
        return self
    def __exit__(self, *args):
        self.extend(self._stringio.getvalue().splitlines())
        sys.stdout = self._stdout

class testFizzBuzz(unittest.TestCase):
	def test_three(self):
		with Capturing() as output:
			fizzBuzz(3)
			ans = ["1", "2", "Fizz"]
    		self.assertListEqual(output, ans)
	
	def test_five(self):
		with Capturing() as output:
			fizzBuzz(5)
			ans = ["1", "2", "Fizz", "4", "Buzz"]
    		self.assertListEqual(output, ans)

if __name__ == '__main__':
    unittest.main()