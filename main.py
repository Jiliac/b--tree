#!/usr/bin/python3

from random import randint # For insert testing.

from tree import *

import csv

L1 = [] # course number
L2 = [] # course title
L3 = [] # instructor
L4 = [] # class size


data_table = []

with open('CoursesOffered_2018Spring.csv', newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
    for row in spamreader:
        L1.append(int(row[0].replace("CS","")))
        L2.append(row[1])
        L3.append(row[2])
        L4.append(int(row[3]))

# collecting all tuple into list 'data_table'
for i in range(len(L1)):
    temp_tuplelist = []
    temp_tuplelist.append(i+1) # tuple id starting from 1
    temp_tuplelist.append(L1[i])
    temp_tuplelist.append(L2[i])
    temp_tuplelist.append(L3[i])
    temp_tuplelist.append(L4[i])
    data_table.append(temp_tuplelist)

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
        new_root = tree_insert(randint(0, 100), root)
        if new_root is not None:
            root = new_root
        print("(i:{}) inserted tree:\n{}\n".format(i, root))


DO_TEST = True
if DO_TEST:
    basic_tree_test()
    key_test()
    insert_test()
