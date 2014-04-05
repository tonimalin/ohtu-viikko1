# -*- coding: utf_8 -*-

import time
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
    
def test_splay_tree_search():
    time_begin = time.time()
    st = SplayTree.SplayTree()
    for i in range(1000):
        st.insert(i)
    for s in range(1000):
        st.search(st.root, random.randint(0,1000))
    st.print_tree_vertical()
    print 'Time: ', time.time() - time_begin
        
    
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

    
    
def compare_insertion_and_search():
    rounds = int(raw_input('How many rounds of test? '))
    insertions = int(raw_input('How many insertions (nodes in the structure)? '))
    top_percent = float(raw_input('How many percent of the values are searched? '))
    repeat = int(raw_input('How many times those values are searched? '))
    
    values = random.sample(range(insertions*10), insertions)
    search_values = random.sample(values, int(top_percent * insertions / 100))
    searches = search_values * repeat
    random.shuffle(searches)
    
    for round in range(rounds):

        print '-' * 20
        sl = SkipList.SkipList()
        st = SplayTree.SplayTree()
        t  = Treap.Treap()
        structures = [(sl, 'Skip list'), (st, 'Splay tree'), (t, 'Treap')]
            
        print '\nInsertions:'
        for structure in structures:
            time_begin = time.time()
            for key in range(insertions):
                structure[0].insert(key)
            print ('Inserting ' + str(insertions) + ' values to empty ' +
                   structure[1] + ' took ' + str(time.time() - time_begin) +
                   ' seconds')
    
        print '\nSearches:'
        
        time_begin = time.time()
        for key in searches:
            sl.search(key)
        print ('Searching ' + str(len(searches)) + ' values from skip list took ' +
               str(time.time() - time_begin) + ' seconds')
         
        time_begin = time.time()
        for key in searches:
            st.search(st.root, key)
        print ('Searching ' + str(len(searches)) + ' values from splay tree took ' +
               str(time.time() - time_begin) + ' seconds')
        
        time_begin = time.time()       
        for key in searches:
            t.search(t.root, key)
        print ('Searching ' + str(len(searches)) + ' values from treap took ' +
               str(time.time() - time_begin) + ' seconds')
    

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
    20 test_splay_tree_search()
    
    52 compare_insertion_and_search()
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
    elif a == '20': test_splay_tree_search()
    elif a == '52': compare_insertion_and_search()
    