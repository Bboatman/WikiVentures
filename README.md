# WikiVentures
Software Dev group

much of our documentation is avaliable here:

https://docs.google.com/a/macalester.edu/document/d/1ffYBqFHiXW-TGoFv0WGkYDp_T80qaOYokwHChSSXIYg/edit?usp=sharing
## Style Convention Agreements
* Tests will be declared in the tests folder with the prefix 'test_' followed by what you are testing
* All strings will be declared using single quotes so we don't have to escape our double quotes 

## Class Breakdown
#### WikiArea
This class represents a single wikipedia page using the Wikipedia api. It will serve as all of the information needed for one area or level in the actual gamified part of the program. It has all of the information that we had on the previous page class that it replaced plus a ton more for future features we might add.

#### GameState
This is the information about game data for one instance of the game, it keeps track of the following
* The Start Page
* The Goal Page
* Every link the user clicks while traversing from start to goal
* Whether or not the game has been won

The class is currently set up to initialize with a default start of 'Pickles' and a default end of 'Jesus'

#### Interface
This class should handle the display and interaction portion of the game. Currently just a command line client,
but eventually it should handle gui things as well