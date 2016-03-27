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
			\n Type "target" to see your target link again \
			\n Type "exit" to quit the game \
			\n Type "go" or "go "Title"" to follow a link \n \
			\nPlease Enter A Command: ')

		if prompt[0:2] == 'go':
			goToLink(prompt, gamestate)

		elif prompt == 'path':
			print(gamestate.getPath())

		elif prompt == 'target':
			print(gamestate.getTarget(), "\n")

		elif prompt == 'exit':
			quit()

		elif prompt == 'where':
			listAllLinks(gamestate)

		else:
			print('That was not a valid commmand, please try again \n')

		if gamestate.isWin():
			print('You win in ' + str(gamestate.getNumClicks()) + ' clicks')
			break;

def goToLink(prompt, gamestate):
	destination = ""
	# Check to see if the user inputted just go, or go and destination
	if len(prompt) == 2:
		destination = input('Enter a destination: ')
	# If they printed both, handle cases where desination is multiple words
	elif " " in prompt:
		promptWithArg = prompt.split(" ")
		for i in range(len(promptWithArg[1:])):
			destination += promptWithArg[1 + i] + " "
			destination = destination[:-1]
	else: 
		print("Please enter a valid command\n")

	# If the destination they entered is a viable option, move there
	if gamestate.addToPath(destination):
		print('Moved to', gamestate.getCurrentPage(), "\n")
	else:
		print('Failed to move\n')

def listAllLinks(gamestate):
	debugVals = []
	possibleDestinations = gamestate.currentArea.getChildren()
	print("You're at: " + gamestate.getCurrentPage())
	print('You can go to: ')
	for title in possibleDestinations:
		# Catch any unencodable strings and log them for debug purposes
		try:
			print(title)
		except:
			debugVals += title

	# Formatting and printing for debug state
	if gamestate.isDebug():
		print("==============================\n \
			>>>> Start Debug Output \n \
			>> Number of Unencodable Links" + str(len(debugVals)) + \
			"\n ==============================")


main()