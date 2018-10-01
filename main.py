#!/usr/bin/python3

from random import randint # For insert testing.

from tree import *

def basic_tree_test():
    # Test very simple tree printing.
    right_leaf = Leaf([4, 5])
    left_leaf = Leaf([1, 2], right_leaf)
    node = Node()
    node.keys = [3]
    node.children = [left_leaf, right_leaf]
    print("Node:\n{}\n".format(node))

    # Test search
    SEARCH_VAL = 4
    print("Search {}: {}\n".format(SEARCH_VAL, node.search(SEARCH_VAL)))

    # Test printing tree with more hierarchy.
    above_node = Node()
    child_node = node
    child_node.depth = 1
    above_node.keys = [5]
    above_node.children = [child_node]
    print("Above node:\n{}\n".format(above_node))
    # This above_node should not happen in real. Only one child node isn't
    # right.

def key_test():
    dummy_course = Course(tid=0, number="301", size="21")
    key = Course_Key(dummy_course)
    print("key:", key)

def insert_test():
    root = Node()
    for i in range(10):
        tree_insert(randint(0, 100), root)
        print("(i:{}) inserted tree:\n{}\n".format(i, root))


DO_TEST = True
if DO_TEST:
    basic_tree_test()
    key_test()
    insert_test()
