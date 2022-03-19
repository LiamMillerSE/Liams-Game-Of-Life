class Node:
    def __init__(self, in_count, out_count):
        self.inputs = []
        self.outputs = []
        self.in_count = in_count
        self.out_count = out_count

    def pushvalue(self, value):
        if self.inputs.count <= self.in_count:
            self.inputs.append(value)

    def popvalue(self):
        return self.outputs.pop()

    def readytoprocess(self):
        return self.inputs.count() == self.in_count

    def process(self):
        # perform operation
        pass

    def processingfinished(self):
        return self.outputs.count() == self.out_count


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
        self.outputs.clear(self)
        self.outputs.append(self.inputs.pop())


class Creature(Node):
    def __init__(self, in_count, out_count, nodes):
        Node.__init__(self, in_count, out_count)
        self.nodes = nodes

    def process(self):
        # feed inputs into nodes then set outputs
        for n in self.nodes:
            while not n.readytoprocess():
                n.pushvalue(self.inputs.pop())
            n.process()
