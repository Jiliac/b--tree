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

def key_test():
    dummy_course = Course(tid=0, number="301", size="21")
    key = Course_Key(dummy_course)
    print("key:", key)

def insert_test():
    root = Node()
    for i in range(15):
        new_data = Course(i, randint(0, 100), randint(0, 100))
        new_root = tree_insert(new_data, root)
        if new_root is not None:
            root = new_root
        print("(i:{} - new_val={}) inserted tree:\n{}\n".format(
            i, new_data, root))


DO_TEST = True
if DO_TEST:
    key_test()
    insert_test()
