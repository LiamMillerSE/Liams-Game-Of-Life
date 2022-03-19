class Node:
    def __init__(self, in_count, out_count):
        self.inputs = []
        self.outputs = []
        self.in_count = in_count
        self.out_count = out_count

    def pushvalue(self, value):
        if len(self.inputs) <= self.in_count:
            self.inputs.append(value)

    def popvalue(self):
        return self.outputs.pop(0)

    def readytoprocess(self):
        return len(self.inputs) == self.in_count

    def process(self):
        # perform operation
        pass

    def outputcomplete(self):
        return len(self.outputs) == 0


class Negate(Node):
    def __init__(self):
        Node.__init__(self, 1, 1)

    def process(self):
        self.outputs.clear(self)
        self.outputs.append(-self.inputs.pop())


class StraightThrough(Node):
    def __init__(self):
        Node.__init__(self, 1, 1)

    def process(self):
        self.outputs.clear()
        self.outputs.append(self.inputs.pop())

class Maximize(Node):
    def __init__(self, value):
        self.value = value
        Node.__init__(self, 1, 1)

    def process(self):
        self.outputs.clear()
        self.inputs.pop(0)
        self.outputs.append(self.value)


class Creature(Node):
    def __init__(self, in_count, out_count, nodes):
        Node.__init__(self, in_count, out_count)
        self.nodes = nodes

    def process(self):
        # feed inputs into nodes then set outputs
        for n in self.nodes:
            while not n.readytoprocess():
                n.pushvalue(self.inputs.pop(0))
            n.process()
            while not n.outputcomplete():
                self.outputs.append(n.popvalue())
