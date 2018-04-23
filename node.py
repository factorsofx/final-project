import pdb

class Output:
    """
    A representation of an output of a module. To prevent the sound differing based on the order
    that modules are processed in, the getter returns the previous value until update is called.
    """

    def __init__(self):
        self.__old_val = 0
        self.__val = 0

    @property
    def val(self):
        return self.__old_val
    
    @val.setter
    def val(self, val):
        self.__val = val

    def update(self):
        self.__old_val = self.__val


class GraphNode:
    def __init__(self):
        self.__inputs = {}
        self.__outputs = {}
    
    @property
    def inputs(self):
        return self.__inputs
    
    @property
    def outputs(self):
        return self.__outputs
    
    def get_input(self, name):
        if name in self.__inputs:
            return self.__inputs[name].val
        else:
            return 0
    
    def set_input(self, name, input):
        pdb.set_trace()
        self.__inputs[name] = input
    
    def set_output(self, name, val):
        if not name in self.__outputs:
            self.__outputs[name] = Output()
        
        self.__outputs[name].val = val

    def get_output_value(self, name):
        if name in self.__outputs:
            print(self.__outputs[name].val)
            return self.__outputs[name].val
        else:
            return 0
    
    def get_output(self, name):
        if not name in self.__outputs:
            self.__outputs[name] = Output()
        return self.__outputs[name]
    
    def update_outputs(self):
        for output in self.__outputs.values():
            output.update()

    def process(self, dt):
        """Update this node, with the given delta-t."""
        pass