import random
import math

class SubsumptionBrain:
    """A class that implements the Subsumption reactive architecture. It
    keeps a list of behavior objects. The higher the index in the list, the
    more important the behavior is. Wander, as the most basic behavior, will
    be in position 0. The brain includes methods for adding behaviors to the
    list. It then has a step method, which runs one cycle of sensor to action,
    and a run method that just repeats the step."""
    
    def __init__(self, enemyEntity):
        """set up the Brain with an empty list of behaviors, and attach
        the enemy that this brain is controlling."""
        self.behaviors = []
        self.entity = enemyEntity
        """
        self.add(subsumptionBehaviors.wanderWander)
        self.add(subsumptionBehaviors.fleet)
        self.add(subsumptionBehaviors.defend)
        self.add(subsumptionBehaviors.chase)
        self.add(subsumptionBehaviors.avoid)
"""
    def add(self, behavior):
        """Takes a behavior method as input, and initializes it, and
        adds it to the list"""
        self.behaviors.append( behavior )

    def step(self, dt):
        """Runs one cycle/step of the reactive actions. It figures out the
        highest-level behavior that is currently applicable, and takes its
        recommendation for motor values"""
        (speed, angle, behavName) = self._updateBehaviors()
        self.updateEntity(speed, angle, dt)

    def _updateBehaviors(self):
        """A private helper method that determines the highest applicable
        behavior, and returns it, in the process updating all the higher
        behaviors. Note that lower behaviors aren't updated at all."""

        # starting at the end and working backwards,
        for b in range(len(self.behaviors) - 1, -1, -1):
            behav = self.behaviors[b]
            resp = behav()
            # If the behavior fired, then return its response
            if resp != None:
                return (resp[0], resp[1], behav.__name__)
        return (0, 0, "None")  # if all else fails, stop moving

    def updateEntity(self, speed, angle, dt):
        self.entity.x += speed * math.cos(angle) * dt
        self.entity.y += speed * math.sin(angle) * dt


# end of SubsumptionBrain Class
"""
class subsumptionBehaviors:
    def avoid():
        return None

    def chase():
        return None

    def defend():
        return None

    def fleet():
        return None

    def wanderWander():
        speed = random.randint(80, 150)
        angle = random.randint(80, 100)
        return(speed, angle)
"""