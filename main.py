#!/usr/bin/python3

from tree import *

DO_TEST = True

if DO_TEST:
    right_leaf = Leaf([4, 5])
    left_leaf = Leaf([1, 2], right_leaf)
    node = Node(0)
    node.keys = [3]
    node.children = [left_leaf, right_leaf]

    print("Node:\n{}\n".format(node))

    # To test node hierarchy.
    above_node = Node(0)
    child_node = node
    child_node.depth = 1
    above_node.keys = [5]
    above_node.children = [child_node]
    print("Above node:\n{}".format(above_node))
    # This above_node should not happen in real. Only one child node isn't
    # right.
