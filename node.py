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

    @val.getter
    def val(self):
        return self.__val

    def update(self):
        self.__val = self.__old_val


class GraphNode:
    def __init__(self):
        self.__inputs = {}
        self.__outputs = {}

    def process(self):
        pass