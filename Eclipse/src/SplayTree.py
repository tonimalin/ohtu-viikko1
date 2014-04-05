# -*- coding: utf_8 -*-
from BinarySearchTree import BinarySearchTree

class SplayTree(BinarySearchTree):


    def splay(self, x):
        while x != self.root:
            if x.parent == self.root:
                if x.parent.left == x:
                    self.rotate_right(x)
                else:
                    self.rotate_left(x)
            else: # distance from the root is at least 2
                if x.parent == x.parent.parent.left:
                    if x == x.parent.left: # zig-zig
                        self.rotate_right(x.parent)
                        self.rotate_right(x)
                    else: # zig-zag
                        self.rotate_left(x)
                        self.rotate_right(x)
                else:
                    if x == x.parent.left: # zag-zig
                        self.rotate_right(x)
                        self.rotate_left(x)
                    else: # zag-zag
                        self.rotate_left(x.parent)
                        self.rotate_left(x)


    def search(self, x, search_key):
        last_accessed = None
        
        while x != None:
            if x.key == search_key:
                self.splay(x)
                return x
            else:
                last_accessed = x
                if search_key < x.key:
                    x = x.left
                else:
                    x = x.right
                
        # if the tree is not empty splay last accessed node prior to None link:
        if last_accessed != None:
            self.splay(last_accessed)
            
        return None

                        
    def insert(self, key):
        new_node = BinarySearchTree.insert(self, key)
        self.splay(new_node)
        return new_node
        

    def min(self, x):
        min_node = BinarySearchTree.min(self, x)
        self.splay(min_node)
        return min_node

            
    def max(self, x):
        max_node = BinarySearchTree.max(self, x)
        self.splay(max_node)
        return max_node


    def succ(self, x):
        succ_node = BinarySearchTree.succ(self, x)
        self.splay(succ_node)
        return succ_node        

    
    def delete(self, remove):
        parent = None
        if remove.parent != None:
            parent = remove.parent
        self.splay(remove)
        BinarySearchTree.delete(self, remove)
        if parent:
            self.splay(parent)
            
