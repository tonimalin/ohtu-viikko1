# -*- coding: utf_8 -*-

import random
import timeit

import BinarySearchTree
import SkipList
import SplayTree
import Treap
    

def make_binary_tree(numbers=None):
    if not numbers:
        numbers = [5,2,7,1,3,6,8,0,9,4]
    tree = BinarySearchTree.BinarySearchTree()
    for i in numbers:
        tree.insert(i)
    return tree

def make_splay_tree(numbers=None):
    if not numbers:
        numbers = [5,2,7,1,3,6,8,0,9,4]
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
    print 'Lisätään 50 alkiota. Tehdään splay-operaatio 100 kertaa.'
    numbers = range(50)
    tree = make_splay_tree(numbers)
    tree.print_tree_vertical(tree.root)
    for _ in range(100):
        rnd = random.choice(numbers)
        print 'splay', rnd
        node = tree.search(tree.root, rnd)
        tree.splay(node)
    tree.print_tree_vertical(tree.root)
    
def test_splay_tree_insert():
    tree = make_splay_tree()
    tree.print_tree_vertical()
    tree.insert(10)
    tree.print_tree_vertical()

def test_splay_tree_insert_10():    
    tree = make_splay_tree()
    tree.print_tree_vertical()
    for i in range(10, 20):
        tree.insert(i)
    tree.print_tree_vertical()
    
def test_splay_tree_min():
    tree = make_splay_tree()
    tree.print_tree_vertical()
    min = tree.min(tree.root)
    print 'min node:'
    min.print_node()
    tree.print_tree_vertical()
    
def test_splay_tree_max():
    tree = make_splay_tree()
    tree.print_tree_vertical()
    tree.max(tree.root)
    tree.print_tree_vertical()
    
def test_splay_tree_succ():
    tree = make_splay_tree()
    tree.print_tree_vertical()
    successor = tree.succ(tree.get_node(5))
    print 'successor of 5:'
    successor.print_node()
    print
    tree.print_tree_vertical()
    
def test_splay_tree_search_succesful():
    tree = make_splay_tree()
    tree.print_tree_vertical()
    print "Search 5 \n"
    tree.search(tree.root, 5)
    tree.print_tree_vertical()
    
def test_splay_tree_search_unsuccesful():
    tree = make_splay_tree()
    tree.print_tree_vertical()
    print "Search 3.3 \n"
    tree.search(tree.root, 3.3)
    tree.print_tree_vertical()
    
def test_splay_tree_delete():
    tree = make_splay_tree()
    tree.print_tree_vertical()
    print "delete 5 \n"
    node = tree.get_node(5)
    tree.delete(tree.get_node(5))
    tree.print_tree_vertical()
    
def test_splay_tree_delete_4():
    tree = make_splay_tree()
    tree.print_tree_vertical()
    for i in [0,8,4,2]:
        print "delete", i
        node = tree.get_node(i)
        node.print_node()
        tree.delete(node)
        tree.print_tree_vertical()

    

def skip_list_insert(number=1000):
    skip_list = SkipList.SkipList()
    for i in range(number):
        skip_list.insert(i)
        
def splay_tree_insert(number=1000):
    splay_tree = SplayTree.SplayTree()
    for i in range(number):
        splay_tree.insert(i)


def skip_list_search(keys, search_keys, repeat_search):
    skip_list = SkipList.SkipList()
    for n in keys:
        skip_list.insert(n)
    for _ in range(repeat_search):
        for s in search_keys:
            skip_list.search(s)
            
def splay_tree_search(keys, search_keys, repeat_search):
    splay_tree = SplayTree.SplayTree()
    for n in keys:
        splay_tree_insert(n)
    for _ in range(repeat_search):
        for s in search_keys:
            splay_tree.search(splay_tree.root, s)
            
def treap_search(keys, search_keys, repeat_search):
    treap = Treap.Treap()
    for n in keys:
        treap.insert(n)
    for _ in range(repeat_search):
        for s in search_keys:
            treap.search(treap.root, s)
    
    
def initialize_compare_search():
    all = random.sample(range(10000), 20)
    search = random.sample(all, 10)
    return all, search


def compare_insert_skip_list_and_splay_tree():
    actions = raw_input('How many actions? ')
    
    timer_sl = timeit.Timer('skip_list_insert(' + actions + ')',
                            'from __main__ import skip_list_insert')
    print 'Skip list insert ' + actions + ':', timer_sl.timeit(number=1)
    
    timer_st = timeit.Timer('splay_tree_insert(' + actions + ')',
                            'from __main__ import splay_tree_insert')
    print 'Splay tree insert ' + actions + ':', timer_st.timeit(number=1)
    
    # call timeit a few times and returns a list of results
    # print bar.repeat(3, numbers=1)


def compare_search():
    repeat_search = '1'
    print 'Lisätään rakenteeseen 20 alkiota.'
    print 'Etsitään niistä 10 alkioita ' + repeat_search + ' kertaa.'
    timer1 = timeit.Timer('skip_list_search(keys, search_keys, ' + repeat_search + ')',
                          'from __main__ import skip_list_search, initialize_compare_search\n'
                          'keys, search_keys = initialize_compare_search()')
    print 'Skip list:', timer1.timeit(number=1)
    timer1 = timeit.Timer('splay_tree_search(keys, search_keys, ' + repeat_search + ')',
                          'from __main__ import splay_tree_search, initialize_compare_search\n'
                          'keys, search_keys = initialize_compare_search()')
    print 'Splay tree:', timer1.timeit(number=1)
    timer1 = timeit.Timer('treap_search(keys, search_keys, ' + repeat_search + ')',
                          'from __main__ import treap_search, initialize_compare_search\n'
                          'keys, search_keys = initialize_compare_search()')
    print 'Treap:', timer1.timeit(number=1)
    

while True:
    print '''
    x  exit
    
    1  test_skip_list()
    
    2  test_binary_tree()
    4  test_binary_tree_rotate()
    5  test_binary_tree_rotate_1_branch()
    
    10 test_splay_tree_splay()
    11 test_splay_tree_insert()
    12 test_splay_tree_insert_10()
    13 test_splay_tree_min()
    14 test_splay_tree_max()
    15 test_splay_tree_succ()
    16 test_splay_tree_search_succesful()
    17 test_splay_tree_search_unsuccesful()
    18 test_splay_tree_delete()
    19 test_splay_tree_delete_4()
    
    50 compare_insert_skip_list_and_splay_tree()
    51 compare_search()
    '''
    a = raw_input('Choose: ')
    print
    if   a == 'x' : break
    elif a == '1' : test_skip_list()
    elif a == '2' : test_binary_tree()
    elif a == '4' : test_binary_tree_rotate()
    elif a == '5' : test_binary_tree_rotate_1_branch()
    elif a == '10': test_splay_tree_splay()
    elif a == '11': test_splay_tree_insert()
    elif a == '12': test_splay_tree_insert_10()
    elif a == '13': test_splay_tree_min()
    elif a == '14': test_splay_tree_max()
    elif a == '15': test_splay_tree_succ()
    elif a == '16': test_splay_tree_search_succesful()
    elif a == '17': test_splay_tree_search_unsuccesful()
    elif a == '18': test_splay_tree_delete()
    elif a == '19': test_splay_tree_delete_4()
    elif a == '50': compare_insert_skip_list_and_splay_tree()
    elif a == '51': compare_search()
    