from wikipedia import page
from random import shuffle
from body import Body, Star
from kivy.core.window import Window
from string import ascii_lowercase as LETTERS 

class System(object):
    def __init__(self, title):
        self.page = page(title)
        self.title = title
        self.star = Star(title)
        planet_names = self.page.links
        shuffle(planet_names)
        if len(planet_names) > 400:
            planet_names = planet_names[:400]
        self.planets = []
        i = 1
        for name in planet_names:
            self.planets.append(Body(name, i))
            i += 1
        

    def update(self, dt):
        for planet in self.planets:
            planet.update((self.star.x + self.star.size//2, self.star.y+ self.star.size//2), dt)