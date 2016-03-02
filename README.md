# WikiVentures
Software Dev group

much of our documentation is avaliable here:

https://docs.google.com/a/macalester.edu/document/d/1ffYBqFHiXW-TGoFv0WGkYDp_T80qaOYokwHChSSXIYg/edit?usp=sharing
## Style Convention Agreements
* Tests will be declared in the tests folder with the prefix 'test_' followed by what you are testing
* All strings will be declared using single quotes so we don't have to escape our double quotes 

## Class Breakdown
#### Page
This class represents a single wikipedia page. Waab is working on this currently and is trying to figure out a way to
incorporate the parser into the page class so that each initialized page does its own link scraping

#### Gamestate
This is the information about game data for one instance of the game, it keeps track of the following
* The Start Page
* The Goal Page
* Every link the user clicks while traversing from start to goal
* Whether or not the game has been won

The class is currently set up to initialize with a default start of 'Pickles' and a default end of 'Jesus'

#### Interface
This class should handle the display and interaction portion of the game. Currently just a command line client,
but eventually it should handle gui things as well