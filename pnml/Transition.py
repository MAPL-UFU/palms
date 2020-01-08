
import time # timestamp for id generation
from random import randint # random number for id generation

class Transition:
    """ This class represents a labelled transition of a Petri net. 

    A transition represents an activity.

    transition.id: Unique ID of this transition.
    transition.label: Label of this transition.

    Layout information:
      transition.position: Position to display the transition in graphical representations.
        Usually a transition is drawn as a square. The position is the center of this square.
      transition.offset: Offest of the transition label.
        Usually the label of a transition is printed centered below the square which
        represents the transition in graphical representations. This offset represents
        a vector which defines a translation of the label inscription from its
        usual position.
    """
    
    def __init__(self):
        self.label = "Transition" # default label of event
        #generate a unique id
        self.id = ("Transition" + str(time.time())) + str(randint(0, 1000))
        self.offset = [0, 0]
        self.position = [0, 0]

    def __str__(self):
        return self.label