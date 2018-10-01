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
    def to_str(self, depth):
        return str(self)

class Node:
    def __init__(self):
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

    def insert(self, key, new_child):
        #print("NODE INSERT: {} (key: {})".format(new_child, key))
        for i in range(len(self.keys)):
            if key < self.keys[i]:
                self.keys.insert(i, key)
                self.children.insert(i+1, new_child)
                return

        # Not under any key, so above all of them.
        self.keys.append(key)
        self.children.append(new_child)

    def __str__(self):
        return self.to_str()
    def to_str(self, depth=0):
        ret = ""

        for i in range(len(self.children)):
            child = self.children[i]
            ret += "| " * depth
            ret += "child {}:\n".format(i)
            if type(child) is Leaf:
                ret += "| " * (depth+1) + "{}\n".format(child.to_str(depth+1))
            else:
                ret += "{}\n".format(child.to_str(depth+1))

            if i == len(self.children) - 1: # We are at the end. No more key.
                continue
            ret += "| " * depth
            ret += "key {}={}\n".format(i, self.keys[i])

        return ret[:-1]

def tree_insert(data, root):
    # Initialize variables
    n = root
    stack = []
    new_root = None

    # Handle init case when root is empty
    if len(root.children) == 0:
        first_leaf = Leaf(values=[data])
        root.children = [first_leaf]
        return new_root
    elif len(root.children) == 1:
        second_leaf = Leaf(values=[data])
        child = root.children[0]
        if data < child.values[0]:
            root.children = [second_leaf, child]
            root.keys = [data]
        else:
            root.children.append(second_leaf)
            root.keys = [child.values[0]]
        return new_root

    # Search where blocks belong.
    # As a result n is the proper leaf to insert and stack are the parent nodes
    # in case of a split.
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
            return new_root

    if len(n.values) < TREE_ORDER: # not full
        insort(n.values, data)
        return new_root

    # Leaf is full
    temp = Leaf(values=cpy(n.values))
    insort(temp.values, data)
    new = Leaf(next_leaf=n.next_leaf)
    j = len(temp.values) # = p_leaf + 1
    if j % 2 == 0:
        j = j // 2
    else: # Ceiling
        j = (j//2) + 1
    n.values = temp.values[:j]
    n.next_leaf = new
    new.values = temp.values[j:]
    print("n: {}\tnew: {}".format(n, new))

    key = temp.values[j-1]

    while True:
        if len(stack) == 0:
            new_root = Node()
            new_root.keys = [key]
            new_root.children = [n, new]
            return new_root

        n = stack.pop()
        if len(n.children) < TREE_ORDER:
            n.insert(key, new)
            return new_root

        temp = Node()
        temp.keys = cpy(n.keys)
        temp.children = cpy(n.children)
        temp.insert(key, new)
        new = Node()

        j = (TREE_ORDER+1)//2
        n.keys = temp.keys[:j-1]
        n.children = temp.children[:j]
        new.keys = temp.keys[j:]
        new.children = temp.children[j:]

        key = temp.keys[j-1]

# Util: "deep" list copy
def cpy(old_list):
    return [i for i in old_list]
