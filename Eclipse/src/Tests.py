# -*- coding: utf_8 -*-

import random
import unittest

import BinarySearchTree
import SplayTree
import SkipList
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



class TestSplayTree(unittest.TestCase):
    pass
    # creation_of_empty_tree
        # root == None
    # inserts to empty tree
        # one node: 1
        # two nodes
            # the first will be left child: 1,2
            # the first will be right child: 2,1
        # 3 nodes
            # 1,2,3
            # 1,3,2
            # 2,1,3
            # 2,3,1
            # 3,1,2
            # 3,2,1
            
    # Test search
    
#     def test_search(self):
#         st = SplayTree.SplayTree()
#         st.insert(1)
#         node = st.search(st.root, 1)
        
    
    # Test delete
        
    def test_delete__only_node(self):
        st = SplayTree.SplayTree()
        st.insert(1)
        node = st.search(st.root, 1)
        st.delete(node)
        self.assertTrue(st.root == None)
        
        # two node tree
        
    def test_delete__2_node_tree_with_parent_and_left_child__delete_child(self):
        st = SplayTree.SplayTree()
        st.insert(1)
        st.insert(2)
        node1 = st.search(st.root, 1)
        node2 = st.search(st.root, 2)
        st.delete(node1)
        self.assertTrue(st.root      == node2 and
                        node2.parent == None and
                        node2.left   == None and
                        node2.right  == None)
        
    def test_delete__2_node_tree_with_parent_and_left_child__delete_parent(self):
        st = SplayTree.SplayTree()
        st.insert(1)
        st.insert(2)
        node1 = st.search(st.root, 1)
        node2 = st.search(st.root, 2)
        st.delete(node2)
        self.assertTrue(st.root      == node1 and
                        node1.parent == None and
                        node1.left   == None and
                        node1.right  == None)
        
    def test_delete__2_node_tree_with_parent_and_right_child__delete_child(self):
        st = SplayTree.SplayTree()
        st.insert(2)
        st.insert(1)
        node1 = st.search(st.root, 1)
        node2 = st.search(st.root, 2)
        st.delete(node2)
        self.assertTrue(st.root      == node1 and
                        node1.parent == None and
                        node1.left   == None and
                        node1.right  == None)
        
    def test_delete__2_node_tree_with_parent_and_right_child__delete_parent(self):
        st = SplayTree.SplayTree()
        st.insert(2)
        st.insert(1)
        node1 = st.search(st.root, 1)
        node2 = st.search(st.root, 2)
        st.delete(node1)
        self.assertTrue(st.root      == node2 and
                        node2.parent == None and
                        node2.left   == None and
                        node2.right  == None)
        
        # three node tree
    def initialize_test_delete__3_node_tree_all_left(self):
        self.st = SplayTree.SplayTree()
        self.nodes = []
        for key in range(3):
            self.st.insert(key)
            self.nodes.append(self.st.search(self.st.root, key))
        
        
    def test_delete__3_node_tree_all_left__delete_middle(self):
        self.initialize_test_delete__3_node_tree_all_left()
        n0, n1, n2 = self.nodes
        self.st.delete(n1)
#         for n in range(3):
#             self.nodes[n].print_node()
#             print
        self.assertTrue(self.st.root == n2   and
                        n2.parent    == None and
                        n2.left      == n0   and
                        n2.right     == None and
                        n0.parent    == n2   and
                        n0.left      == None and
                        n0.right     == None)
        
        
        
    # splay
        
        



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
        


class TestSKipList(unittest.TestCase):
    
    def test_skip_list_as_list(self):
        sl = SkipList.SkipList()
        for key in range(10):
            sl.insert(key)
        self.assertEqual(range(10), sl.skip_list_as_list())

    def test_insert_between(self):
        even = range(0, 20, 2)
        odd = range(1, 20, 2)
        numbers = even + odd
        numbers.sort()
        sl = SkipList.SkipList()
        for number in even:
            sl.insert(number)
        for number in odd:
            sl.insert(number)
        self.assertEqual(numbers, sl.skip_list_as_list())
        
    def test_delete_between(self):
        even = range(0, 20, 2)
        odd = range(1, 20, 2)
        numbers = even + odd
        numbers.sort()
        sl = SkipList.SkipList()
        for number in numbers:
            sl.insert(number)
        for number in odd:
            sl.delete(number)
        self.assertEqual(even, sl.skip_list_as_list())
        
    def test_search_unsuccesful(self):
        sl = SkipList.SkipList()
        sl.insert(1)
        self.assertIsNone(sl.search(2))
        
    def test_search_succesful(self):
        sl = SkipList.SkipList()
        for number in range(100):
            sl.insert(number)
        for number in [0,11,17,27,99,50,11,17]:
            self.assertTrue(sl.search(number) == number)
        
        


for test_class in [TestBinarySearchTree, TestSplayTree, TestTreap, TestSKipList]:
    suite = unittest.TestLoader().loadTestsFromTestCase(test_class)
    unittest.TextTestRunner(verbosity=2).run(suite)
    
    
