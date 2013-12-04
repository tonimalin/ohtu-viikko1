# -*- coding: utf_8 -*-

import random
import unittest

import BinarySearchTree
import Treap
#from BinarySearchTree import BinarySearchTree


class TestBinarySearchTree(unittest.TestCase):
    
    def setUp(self):
        self.bst = BinarySearchTree.BinarySearchTree()
        self.numbers = [5,3,8,4,1,7,6,9,0,2]
        for number in self.numbers:
            self.bst.insert(number)
        self.numbers.sort()
            
        # Initially tree will be like this:
        #
        #          5
        #        /   \
        #       /     \
        #      3       8          
        #     / \     / \
        #    1   4   7   9
        #   / \     /
        #  0   2   6
        
    
    def test_correct_order(self):
        self.assertEqual(self.numbers, self.bst.tree_as_list(),
                         'Number sequences are not the same')
    
    # Should deletion attempt of non-existent node raise an exception?
    
    def test_delete(self):
        deleted = random.sample(self.numbers, 5)
        for number in deleted:
            node = self.bst.search(self.bst.root, number)
            self.bst.delete(node)
        not_deleted = [x for x in self.numbers if x not in deleted]
        not_deleted.sort()
        self.assertEqual(not_deleted, self.bst.tree_as_list())
        
    def test_delete_node_with_two_childs(self):
        self.bst.delete(self.bst.get_node(3))
        self.numbers.remove(3)
        # self.numbers.sort()
        self.assertEqual(sorted(self.numbers), self.bst.tree_as_list())
        
    def test_delete_until_tree_is_empty(self):  # bad test: deleted node has never two childs
        for number in range(10):
            node = self.bst.search(self.bst.root, number)
            self.bst.delete(node)
            self.numbers.remove(number)
        self.assertEqual(self.numbers, self.bst.tree_as_list())
     
    def test_insert_same_key(self):
        self.assertRaises(ValueError, self.bst.insert, 5 )

    def test_rotate_root(self):
        self.assertRaises(ValueError, self.bst.rotate, self.bst.root)

    def test_rotate_root_left(self):
        self.assertRaises(ValueError, self.bst.rotate_left, self.bst.root)
        
    def test_rotate_root_right(self):
        self.assertRaises(ValueError, self.bst.rotate_right, self.bst.root)

    def test_rotate_roots_right_child_to_left(self):
        self.bst = BinarySearchTree.BinarySearchTree()
        self.bst.insert(1)
        self.bst.insert(2)
        node1 = self.bst.get_node(1)
        node2 = self.bst.get_node(2)
        self.bst.rotate(node2)
        self.assertTrue(self.bst.root == node2  and  node2.left == node1)
        
    def test_rotate_roots_left_child_to_right(self):
        self.bst = BinarySearchTree.BinarySearchTree()
        self.bst.insert(2)
        self.bst.insert(1)
        node1 = self.bst.get_node(1)
        node2 = self.bst.get_node(2)
        self.bst.rotate(node1)
        self.assertTrue(self.bst.root == node1  and  node1.right == node2)
         
    def test_rotate_to_right_with_all_links(self):
        nodes = [self.bst.get_node(x) for x in range(6)]
        self.bst.rotate(nodes[1])
        self.assertTrue(nodes[5].left   == nodes[1] and
                        nodes[1].parent == nodes[5] and
                        nodes[1].left   == nodes[0] and
                        nodes[0].parent == nodes[1] and
                        nodes[1].right  == nodes[3] and
                        nodes[3].parent == nodes[1] and
                        nodes[3].left   == nodes[2] and
                        nodes[2].parent == nodes[3] and
                        nodes[3].right  == nodes[4] and
                        nodes[4].parent == nodes[3]     )
        
    def test_rotate_to_left_with_all_links(self):
        nodes = [self.bst.get_node(x) for x in range(6)]
        self.bst.rotate(nodes[1])
        self.bst.rotate(nodes[3])
        self.assertTrue(nodes[5].left   == nodes[3] and
                        nodes[3].parent == nodes[5] and
                        nodes[3].left   == nodes[1] and
                        nodes[1].parent == nodes[3] and
                        nodes[3].right  == nodes[4] and
                        nodes[4].parent == nodes[3] and
                        nodes[1].left   == nodes[0] and
                        nodes[0].parent == nodes[1] and
                        nodes[1].right  == nodes[2] and
                        nodes[2].parent == nodes[1]     )
        

    def test_rotate_node_with_only_left_child(self):
        self.bst = BinarySearchTree.BinarySearchTree()
        for i in range(3, -1, -1):
            self.bst.insert(i)
        nodes = [self.bst.get_node(x) for x in range(4)]
        self.bst.rotate(nodes[1])
        self.assertTrue(nodes[3].left   == nodes[1] and
                        nodes[1].parent == nodes[3] and
                        nodes[1].left   == nodes[0] and
                        nodes[0].parent == nodes[1] and
                        nodes[1].right  == nodes[2] and
                        nodes[2].parent == nodes[1]     )
        
    # ehkä rotate testaukset pitäisi jakaa pienempiin osiin,
    # jossa katsottaisiin onko kaikki linkit oikein




class TestTreap(unittest.TestCase):
    
    def setUp(self):
        self.treap = Treap.Treap()
        self.numbers = [5,3,8,4,1,7,6,9,0,2]
        for number in self.numbers:
            self.treap.insert(number)
        
    def test_nodes_have_priority_values(self):
        nodes = [self.treap.root]
        while nodes:
            node = nodes.pop(0)
            for n in [node.left, node.right]:
                if n != None:
                    nodes.append(n)
            self.assertTrue(node.priority != None and
                            node.priority >= 0 and
                            node.priority <= 1)
            
    def test_node_keys_are_in_binary_search_tree_order(self):
        nodes = [self.treap.root]
        while nodes:
            node = nodes.pop(0)
            if node.left != None:
                nodes.append(node.left)
                self.assertTrue(node.left.key < node.key)
            if node.right != None:
                nodes.append(node.right)
                self.assertTrue(node.right.key > node.key)
                
    def test_node_priorities_are_in_min_heap_order(self):
        nodes = [self.treap.root]
        while nodes:
            node = nodes.pop(0)
            for n in [node.left, node.right]:
                if n != None:
                    nodes.append(n)
                    self.assertTrue(node.priority < n.priority)
        

suite = unittest.TestLoader().loadTestsFromTestCase(TestBinarySearchTree)
unittest.TextTestRunner(verbosity=2).run(suite)

suite = unittest.TestLoader().loadTestsFromTestCase(TestTreap)
unittest.TextTestRunner(verbosity=2).run(suite)
