from .models import Constants

class Node(object):

    def get_description(self):
        if self.probability >= 90:
            return "Highly Probably"
        elif self.probability >= 75:
            return "Quite Likely"
        elif self.probability >= 65:
            return "Rather Likely"
        elif self.probability >= 56:
            return "Better Than Even"
        elif self.probability >= 46:
            return "Toss-up"
        elif self.probability >= 40:
            return "Uncertain"
        elif self.probability > 10:
            return "Not very Probable"
        else:
            return "Very Unlikely"


    def get_event(self):

        if self.event == 0:
            return self.tree
        else:
            return Constants.events[self.event-1]

    def __init__(self, tree, event):
        self.event = event
        self.probability = Constants.probabilities[tree][event-1]
        self.children = Constants.children[event]
