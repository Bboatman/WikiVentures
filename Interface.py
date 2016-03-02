from Page import *
from Gamestate import *

GREET_STRING = "Welcome to Wikiventures."
def main():
	print(GREET_STRING)
	gamestate = Gamestate()
	while not gamestate.gameIsWon():
		print("You are on page", gamestate.getCurrentPage())
		gamestate.winGame()
main()