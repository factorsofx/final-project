from node import *
import math
import pdb

class LowPassFilterNode(TimeTrackingNode):
    def process(self, dt):
        alpha = (2 * math.pi * dt * self.get_input("cutoff")) / (2 * math.pi * dt * self.get_input("cutoff") + 1)
        self.set_output("value", self.get_output_value("value") + alpha * (self.get_input("value") - self.get_output_value("value")))
