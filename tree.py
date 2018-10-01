TREE_ORDER = 3

class Leaf:
    def __init__(self, values=[], next_leaf=None):
        self.values = values
        self.next_leaf = next_leaf # Is this necessary/useful?

    def search(self, k):
        return self.values

    def __str__(self):
        return str(self.values)

class Node:
    def __init__(self, depth):
        """
        @TODO: keys and children need some initialization. To be done with
        insert...
        """

        self.depth = depth

        self.keys = []
        self.children = []  # Should always be one less key than children.

    def search(self, k):
        """
        From wikipedia. Maybe needs correcting to match book algorithm.
        @TODO.
        """

        for i in range(len(self.keys)):
            if k <= self.keys[0]:
                return self.children[i].search(k)
        # Not under all the above keys, so return last child.
        return self.children[-1].search(k)

    def insert(self, k):
        insertion_target = None
        splitted_node = None

        """
        @TODO: Handle initialization case. There is no children yet,
        """
        if len(self.children) == 0: # REMOVE THIS ONCE INIT HANDLED.
            return

        # Same as for search
        for i in range(len(self.keys)):
            if k <= self.keys[0]:
                insertion_target = self.children[i]
        if insertion_target is None:
            # Not under all the above keys, so target is the last child.
            insertion_target = self.children[-1]

        sub_splitted_node = insertion_target.insert(k)

        """
        @TODO: Handle the splitting.
        - If can handle the sub_splitted_node, then insert in the children with
          appropriate key.
        - Otherwise, split this node and:
          - Return the second part to the caller (via 'splitted_node') if this
            isn't the root.
          - However, if this the root, need to create new root (what's returned
            does not matter).
        """

        return splitted_node

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
