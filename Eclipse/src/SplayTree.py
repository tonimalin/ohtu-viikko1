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
            
