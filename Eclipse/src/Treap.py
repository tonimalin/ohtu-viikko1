# -*- coding: utf_8 -*-
import random

# import BinarySearchTree
# import TreeNode
from BinarySearchTree import BinarySearchTree, TreeNode

class TreapNode(TreeNode):
    
    def __init__(self, key=None, parent=None, left=None, right=None):
        TreeNode.__init__(self, key, parent, left, right)
        self.priority = random.random()
        
    def print_node(self):
        links = []
        for link in [self.parent, self.left, self.right]:
            if link != None:
                links.append(link.key)
            else:
                links.append(None)
        print 'parent:  ', links.pop(0)
        print 'key:     ', self.key
        print 'priority:', self.priority
        print 'left:    ', links.pop(0), '| right:  ', links.pop(0)
        

class Treap(BinarySearchTree):
        
    def insert(self, key):
        node = TreapNode()
        new_node = BinarySearchTree.insert(self, key, node)
        
        # tee: heap järjestyksen tarkistaminen ja muuttaminen
        while (new_node != self.root and
               new_node.priority < new_node.parent.priority):
            self.rotate(new_node)  
        