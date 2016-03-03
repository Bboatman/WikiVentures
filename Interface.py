from Gamestate import *

GREET_STRING = '\nWelcome to Wikiventures.\n'
def main():
	print(GREET_STRING)
	gamestate = Gamestate()

	print("You are on page", gamestate.getCurrentPage())
	print("Your goal destination is", gamestate.getTarget(), "\n")
	while True:
		prompt = input('From here you can do the followning: \
			\n Type "where" to look at links you can click \
			\n Type "target?" to see your target link again \
			\n Type "exit" to quit the game \
			\n Type "go" to follow a link \n \
			\nPlease Enter A Command: ')
		if prompt == 'go':
			where = input('Enter a destination: ')
			if gamestate.addToPath(where):
				print('Moved to ' + gamestate.getCurrentPage() + "\n")
			else:
				print('Failed to move\n')
		elif prompt == 'path':
			print(gamestate.getPath())
		elif prompt == 'target?':
			print(gamestate.getTarget(), "\n")
		elif prompt == 'exit':
			quit()
		elif prompt == 'where':
			possibleDestinations = gamestate.currentArea.getChildren()
			print("You're at: " + gamestate.getCurrentPage())
			print('You can go to: ')
			for title in possibleDestinations:
				print(title)
		else:
			print('That was not a valid commmand, please try again \n')

		if gamestate.isWin():
			print('You win in ' + str(gamestate.getNumClicks()) + ' clicks')
			break;


main()