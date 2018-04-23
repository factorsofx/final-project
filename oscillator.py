from node import *
import math


class SineOscillatorNode(TimeTrackingNode):
    def process(self, dt):
        TimeTrackingNode.process(self, dt)
        self.set_output("value", math.sin(self._t * 2 * math.pi * self.get_input("freq")))


class SquareOscillatorNode(TimeTrackingNode):
    def process(self, dt):
        TimeTrackingNode.process(self, dt)
        self.set_output("value", 1 if math.sin(self._t * 2 * math.pi * self.get_input("freq")) > 0 else -1)
