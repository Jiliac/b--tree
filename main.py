#!/usr/bin/python3

from tree import *

DO_TEST = True

if DO_TEST:
    right_leaf = Leaf([4, 5])
    left_leaf = Leaf([1, 2], right_leaf)
    node = Node(0)
    node.keys = [3]
    node.children = [left_leaf, right_leaf]

    print("Node:\n{}".format(node))
