# -*- coding: utf_8 -*-

import random
import SkipList
import SplayTree


    
# treenode = SplayTree.TreeNode()
# treenode.key = 'avain'
# treenode.left = SplayTree.TreeNode('Uusi solmu')
# print treenode.key
# print treenode.left.key

# tree = SplayTree.BinarySearchTree()
# numbers = range(30)
# random.shuffle(numbers)
# for i in numbers:
#     tree.insert(i)
# tree.print_tree_vertical(tree.root)
# searched = tree.search(tree.root, numbers[5])
# print
# print 'min:', tree.min(tree.root).key
# print 'max:', tree.max(tree.root).key
# print 'searched:', searched.key
# successor = tree.succ(searched)
# if successor == None:
#     print "ei seuraajaa"
# else:
#     print 'succ:', tree.succ(searched).key
# print numbers
# print
# 
# random.shuffle(numbers)
# numbers[10:] = []
# print 'poistetaan solut', sorted(numbers)
# while numbers:
#     node = tree.search(tree.root, numbers.pop())
#     tree.delete(node)
# tree.print_tree_vertical(tree.root)

def make_binary_tree(numbers=None):
    if not numbers:
        numbers = [5,2,7,1,3,6,8,0,4,9]
    tree = SplayTree.BinarySearchTree()
    for i in numbers:
        tree.insert(i)
    return tree

def test_binary_tree():
    tree = SplayTree.BinarySearchTree()
    numbers = range(10)
    for i in numbers:
        tree.insert(i)
    tree.print_tree_vertical(tree.root)
    
    for i in range(10):
        rnd = random.choice(numbers)
        node = tree.search(tree.root, rnd)
        if node.parent != None:
            tree.rotate(node)
            print rnd
            tree.print_tree_vertical(tree.root)
            
def test_binary_tree_node_move():
    tree = make_binary_tree()
    tree.print_tree_vertical(tree.root)
    
    move = tree.search(tree.root, 0)
    move_parent = move.parent
    target = tree.search(tree.root, 4)
    print 'Siirretään lehti toisen lehden vasemmaksi lapseksi: 0 --> 4'
    
    print '\nSolmujen arvot ennen siirtoa: '
    print '\nSiirrettävä:'
    move.print_node()
    print '\nSiirrettävän vanhempi:'
    move_parent.print_node()
    print '\nKohde'
    target.print_node()
    # kohteen lapset puuttuu!

    tree.move(move, target, 'left')
    print
    tree.print_tree_vertical(tree.root)
    
    print '\n\nSolmujen arvot siirron jälkeen: '
    print '\nSiirretty:'
    move.print_node()
    print '\nSiirretyn entinen vanhempi:'
    move_parent.print_node()
    print '\nKohde'
    target.print_node()
    
    
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

def test_splay_tree_zig_zig():
    tree = make_binary_tree(range(10))
    tree.print_tree_vertical(tree.root)
    node = tree.search(tree.root, 5)
    print 'zag-zag 5'
    tree.zig_zig(node)
    tree.print_tree_vertical(tree.root)

#     rnd = random.choice(numbers)
#     print rnd, '-->',
#     node1 = tree.search(tree.root, rnd)
#     rnd = random.choice(numbers)
#     print rnd
#     node2 = tree.search(tree.root, rnd)
#     tree.move(node1, node2, 'left')
    
#     tree.print_tree_vertical(tree.root)
    


while True:
    print '''\nMitä tehdään?\n
    x lopetetaan\n
    1 test_skip_list()
    2 test_binary_tree()
    3 test_binary_tree_node_move()
    4 test_binary_tree_rotate()
    5 test_binary_tree_rotate_1_branch()
    6 test_splay_tree_zig_zig()\n'''
    a = raw_input('Valitse: ')
    print
    if a == 'x': break
    elif a == '1': test_skip_list()
    elif a == '2': test_binary_tree()
    elif a == '3': test_binary_tree_node_move()
    elif a == '4': test_binary_tree_rotate()
    elif a == '5': test_binary_tree_rotate_1_branch()
    elif a == '6': test_splay_tree_zig_zig()
    