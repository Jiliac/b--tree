from bisect import insort

TREE_ORDER = 3

class Course():
    def __init__(self, tid, number, size, title="", instructor=""):
        self.tid = tid
        self.number = number
        self.size = size
        self.title = title
        self.instructor = instructor

class Course_Key():
    def __init__(self, course):
        self.number = course.number
        self.size = course.size

    def is_less(self, other):
        if self.number > other.number:
            return False
        if self.size > other.size:
            return False
        return True

    def is_equal(self, other):
        if self.number != other.number:
            return False
        if self.size != other.size:
            return False

    def __str__(self):
        return "(CS{}, size={})".format(self.number, self.size)

class Leaf:
    def __init__(self, values=[], next_leaf=None):
        self.values = values
        self.next_leaf = next_leaf # Is this necessary/useful?

    def search(self, k):
        return self.values

    def insert(self, k):
        # @TODO
        return None

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
        # Children can be internal nodes or leaf node.
        return self.children[-1].search(k)

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


def tree_insert(data, root):
    # Initialize variables
    n = root
    stack = []

    # Search where blocks belong.
    # As a result n is the proper leaf to insert and stack are the parent nodes in case of a split.
    while type(n) is not Leaf:
        stack.append(n)
        q = len(n.children)
        if data <= n.keys[0]:
            n = n.children[0]
        elif data > n.keys[-1]: # -1 = q-2
            n = n.children[-1] # -1 = q-1
        else:
            for i in range(1, len(n.keys)):
                if data <= n.keys[i]:
                    n = n.children[i]
                    break

    # Make sure k is not already inserted in the tree.
    for leaf_value in n.values:
        if leaf_value == data:
            return

    if len(n.values) < TREE_ORDER: # not full
        insort(n.values, data)
        return

    # Leaf is full
    temp = Leaf(values=n.values)
    insort(temp.values, data)
    new = Leaf(next_leaf=n.next_leaf)
    j = len(temp.values) # = p_leaf + 1
    if j % 2 == 0:
        j /= 2
    else:
        j = (j/2) + 1
    n = Leaf(values=temp.values[:j], next_leaf=new)
    new.values = temp.values[j:]

    k = temp.values[j]
