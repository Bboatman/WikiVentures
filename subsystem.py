from body import Body, Star
from kivy.core.window import Window
from random import shuffle

class SubSystem(object):
    def __init__(self, planet_names, title):
        self.title = title
        self.star = Star(title)
        shuffle(planet_names)
        self.planets = []
        i = 1
        for name in planet_names:
            self.planets.append(Body(name, i))
            i += 1
        

    def update(self, dt):
        for planet in self.planets:
            planet.update((self.star.x + self.star.size//2, self.star.y+ self.star.size//2), dt)
        
    