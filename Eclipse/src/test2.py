# -*- coding: utf_8 -*-

import random

import BinarySearchTree
import SkipList
import SplayTree
    

def make_binary_tree(numbers=None):
    if not numbers:
        numbers = [5,2,7,1,3,6,8,0,4,9]
    tree = BinarySearchTree.BinarySearchTree()
    for i in numbers:
        tree.insert(i)
    return tree

def make_splay_tree(numbers=None):
    if not numbers:
        numbers = [5,2,7,1,3,6,8,0,4,9]
    tree = SplayTree.SplayTree()
    for i in numbers:
        tree.insert(i)
    return tree

def test_binary_tree():
    numbers = range(10)
    tree = make_binary_tree(numbers)
    tree.print_tree_vertical(tree.root)
    
    for _ in range(10):
        rnd = random.choice(numbers)
        node = tree.search(tree.root, rnd)
        if node.parent != None:
            tree.rotate(node)
            print rnd
            tree.print_tree_vertical(tree.root)
    
def test_binary_tree_rotate():
    tree = make_binary_tree([6,4,5,2,1,3])
    tree.print_tree_vertical(tree.root)
    node = tree.search(tree.root, 2)
    tree.rotate(node)
    tree.print_tree_vertical(tree.root)
    node = tree.search(tree.root, 4)
    tree.rotate(node)
    tree.print_tree_vertical(tree.root)
    
    
def test_binary_tree_rotate_1_branch():
    tree = make_binary_tree(range(10))
    tree.print_tree_vertical(tree.root)
    for i in range(1,9):
        node = tree.search(tree.root, i)
        tree.rotate(node)
    tree.print_tree_vertical(tree.root)

    
def test_skip_list():
    skip_list = SkipList.SkipList()
    i = 0
    for i in range(10):
        skip_list.insert(i)
        i += 1
    skip_list.print_list()
    skip_list.print_nice()
    print
    for i in range(10):
        skip_list.delete(i)
        skip_list.print_nice()
        print
    
def test_splay_tree_splay():
    numbers = range(50)
    tree = make_splay_tree(numbers)
    tree.print_tree_vertical(tree.root)
    for _ in range(100):
        rnd = random.choice(numbers)
        print 'splay', rnd
        node = tree.search(tree.root, rnd)
        tree.splay(node)
    tree.print_tree_vertical(tree.root)
    


while True:
    print '''
Mitä tehdään?
    
    x lopetetaan
    
    1 test_skip_list()
    2 test_binary_tree()
    4 test_binary_tree_rotate()
    5 test_binary_tree_rotate_1_branch()
    8 test_splay_tree_splay()
    '''
    a = raw_input('Valitse: ')
    print
    if   a == 'x': break
    elif a == '1': test_skip_list()
    elif a == '2': test_binary_tree()
    elif a == '4': test_binary_tree_rotate()
    elif a == '5': test_binary_tree_rotate_1_branch()
    elif a == '8': test_splay_tree_splay()
    