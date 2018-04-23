from node import GraphNode
import math
import array

class ConstantNode(GraphNode):
    def __init__(self, value):
        self.__val = value
        GraphNode.__init__(self)

    def process(self, _):
        self.set_output("value", self.__val)


class MultiplicationNode(GraphNode):
    def process(self, _):
        self.set_output("value", self.get_input("a") * self.get_input("b"))


class AdditionNode(GraphNode):
    def process(self, _):
        self.set_output("value", self.get_input("a") + self.get_input("b"))

class TanHLimiterNode(GraphNode):
    def process(self, _):
        self.set_output("value", math.tanh(self.get_input("value")))

class RootMeanSquareNode(GraphNode):
    def __init__(self, size):
        GraphNode.__init__(self)
        self.__index = 0
        self.__buffer = [0] * size
    def process(self, dt):
        self.__buffer[self.__index % len(self.__buffer)] = self.get_input("value")
        accum = 0
        for num in self.__buffer:
            accum += num ** 2
        self.set_output("value", math.sqrt(accum / len(self.__buffer)))