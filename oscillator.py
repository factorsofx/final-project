class OscillatorNode(GraphNode):
    def __init__(self):
        self.t = 0
        GraphNode.__init__(self)
    
    def process(self):
