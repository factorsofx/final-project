from node import *
import math
import pdb

class LowPassFilterNode(TimeTrackingNode):
    def process(self, dt):
        alpha = (2 * math.pi * dt * self.get_input("cutoff")) / (2 * math.pi * dt * self.get_input("cutoff") + 1)
        self.set_output("value", self.get_output_value("value") + alpha * (self.get_input("value") - self.get_output_value("value")))


class HighPassFilterNode(TimeTrackingNode):
    def __init__(self):
        TimeTrackingNode.__init__(self)
        self.__last_val = 0
    
    def procecss(self, dt):
        alpha = 1 / (2 * math.pi * self.get_input("cutoff") + 1)
        self.set_output("value", alpha * (self.get_output_value("value") + self.get_input("value") - self.__last_val))
        self.__last_val = self.get_input("value")