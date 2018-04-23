from node import *
import math

class SineOscillatorNode(GraphNode):
    def __init__(self):
        GraphNode.__init__(self)
        self.__t = 0
    
    def process(self, dt):
        self.__t += dt
        self.set_output("value", math.sin(self.__t * 2 * math.pi * self.get_input("freq")))
