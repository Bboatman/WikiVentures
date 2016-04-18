from collections import Counter
import subprocess


def palindrome(s):
	return s[::-1] == s

def vectorAddition(a,b):
	return [a[x] + b[x] for x in range(len(a))]

def mostFrequentCharacter(s):
	return Counter(s).most_common()[0][0]

def fizzBuzz(n):
	for x in range(1,n+1):
		if x % 3 == 0 and x % 5 == 0:
			print "FizzBuzz"
		elif x % 3 == 0:
			print "Fizz"
		elif x % 5 == 0:
			print "Buzz"
		else:
			print x