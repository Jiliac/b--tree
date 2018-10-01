TREE_ORDER = 3

class Leaf:
    def __init__(self, values=[], next_leaf=None):
        self.values = values
        self.next_leaf = next_leaf

    def __str__(self):
        return str(self.values)

class Node:
    def __init__(self, depth):
        self.depth = depth

        self.keys = []
        self.children = []  # Should always be one less key than children.

    def __str__(self):
        ret = ""

        for i in range(len(self.children)):
            child = self.children[i]
            ret += "| " * self.depth
            ret += "child {}:\n".format(i)
            if type(child) is Leaf:
                ret += "| " * (self.depth+1) + "{}\n".format(child) 
            else:
                ret += "{}\n".format(child)

            if i == len(self.children) - 1: # We are at the end. No more key.
                continue
            ret += "| " * self.depth
            ret += "key {}={}\n".format(i, self.keys[i])

        return ret
