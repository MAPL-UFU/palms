
import time # timestamp for id generation
from random import randint # random number for id generation

class PetriNet:
    """ This class represents a Petri net.

    This class represents a Petri net. A Petri net consists of
    a set of labelled labelled transitions, labelled places and
    arcs from places to transitions or transitions to places.

    net.edges: List of all edges of this Petri net
    net.transitions: Map of (id, transition) of all transisions of this Petri net
    net.places: Map of (id, place) of all places of this Petri net
    """
    
    def __init__(self):
        #generate a unique id
        self.id = ("PetriNet" + str(time.time())) + str(randint(0, 1000))
        self.arcs = [] # List or arcs
        self.transitions = {} # Map of transitions. Key: transition id, Value: event
        self.places = {} # Map of places. Key: place id, Value: place
        self.name =''


    def __str__(self):
        text = '--- Net: ' + self.name + '\nTransitions: '
        for transition in self.transitions.values():
            text += str(transition) + ' '
        text += '\nPlaces: '
        for place in self.places.values():
            text += str(place) + ' '
        text += '\n'
        for arc in self.arcs:
                text += str(arc) + '\n'
        text += '---'
        
        return text