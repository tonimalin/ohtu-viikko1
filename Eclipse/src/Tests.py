import random
import unittest

import BinarySearchTree


class TestBinarySearchTree(unittest.TestCase):
    
    def setUp(self):
        self.bst = BinarySearchTree.BinarySearchTree()
        self.numbers = range(10)
        random.shuffle(self.numbers)  
    
    def test_insert_and_correct_order(self):
        for key in self.numbers:
            self.bst.insert(key)
        self.numbers.sort()
        self.assertEqual(self.numbers, self.bst.tree_as_list(), 'Number sequences are not the same')
    
    def test_deletion(self):
        deleted = random.sample(self.numbers, 5)
        print 'deleted', deleted
        for key in deleted:
            node = self.bst.search(self.bst.root, key)
            self.bst.delete(node)
        not_deleted = [x for x in self.numbers if x not in deleted]
        print 'not_deleted', not_deleted
        self.numbers.sort()
        self.assertEqual(self.numbers, self.bst.tree_as_list(x))
    
    def test_insert_same_key(self):
        self.assertRaises(ValueError, self.bst.insert(5) )

    def test_tree_as_list(self):
        for key in self.numbers:
            self.bst.insert(key)
        list_from_tree = self.bst.tree_as_list() 
        self.numbers.sort()
        self.assertEqual(self.numbers, list_from_tree)
        

suite = unittest.TestLoader().loadTestsFromTestCase(TestBinarySearchTree)
unittest.TextTestRunner(verbosity=2).run(suite)
