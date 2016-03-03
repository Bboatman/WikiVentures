from GameState import *

GREET_STRING = 'Welcome to Wikiventures.'
def main():
	print(GREET_STRING)
	gamestate = GameState()
	while 1:
		prompt = input('Enter A Command: ')
		if prompt == 'go':
			where = input('Enter a destination: ')
			if gamestate.addToPath(where):
				print('Moved to ' + gamestate.getCurrentPage())
			else:
				print('Failed to move')
		elif prompt == 'path':
			print(gamestate.getPath())
		elif prompt == 'target?':
			print(gamestate.getTarget())
		elif prompt == 'exit':
			quit()
		elif prompt == 'where':
			possibleDestinations = gamestate.currentArea.getChildren()
			print("You're at: " + gamestate.getCurrentPage())
			print('You can go to: ')
			for title in possibleDestinations:
				print(title)

		if gamestate.isWin():
			print('You win in ' + str(gamestate.getNumClicks()) + ' clicks')
			break;


main()