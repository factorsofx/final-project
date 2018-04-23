from node import GraphNode

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