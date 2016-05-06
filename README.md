# WikiVentures
Software Dev (Macalester COMP 255) Project

Much of the planning and outlining documentation is available [here](https://docs.google.com/a/macalester.edu/document/d/1ffYBqFHiXW-TGoFv0WGkYDp_T80qaOYokwHChSSXIYg/edit?usp=sharing)
### About
WikiVentures is a space exploration game reimagining the Wiki-Race game. It's designed to put a spin on how we envision wandering the web and data. Get a mission, wander the WikiVerse and discover out how quickly you can reach your destination.

## WikiVentures Build Guide:
Compatible on python 2.7 and 3.5*
### Install Wikipedia API
    pip install wikipedia

### Install Kivy
#### Windows:
Christopher Gohlke generously provides precompiled binaries for windows [here]: http://www.lfd.uci.edu/~gohlke/pythonlibs/
Download your prefered python's precompiled wheel

    pip install [wheelPath]


#### Mac:
	sudo mv Kivy2.app /Applications/Kivy.app
	ln -s /Applications/Kivy.app/Contents/Resources/script /usr/local/bin/kivy
	kivy -m pip install wikipedia (kivy runs in a virtual env on macs)

#### Linux (Ubuntu and Ubuntu-esque Flavors):
	sudo add-apt-repository ppa:kivy-team/kivy
Python 2.7:

	sudo apt-get install python-kivy
Python 3.5:

Kivy has problems with linux and pygame dependencies in python3
	
### Run
#### Windows / Linux:

	cd [wikiVenturesPath]
	python main.py
#### Mac:
	kivy main.py