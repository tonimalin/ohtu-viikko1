# -*- coding: utf_8 -*-

class TreeNode:
    def __init__(self, key=None, parent=None, left=None, right=None):
        self.parent = parent
        self.key = key
        self.left = left
        self.right = right
        
    def print_node(self):
        links = []
        for link in [self.parent, self.left, self.right]:
            if link != None:
                links.append(link.key)
            else:
                links.append(None)
        print 'p:', links.pop(0)
        print 'k:', self.key
        print 'l:', links.pop(0), '| r:', links.pop(0)


class BinarySearchTree:
    
    def __init__(self, root=None):
        self.root = root
        
    def search(self, x, search_key):
        while x != None and x.key != search_key:
            if search_key < x.key:
                x = x.left
            else:
                x = x.right
        return x
        
    def insert(self, key):
        new_node = TreeNode(key)
        if self.root == None:
            self.root = new_node
            return
        x = self.root
        while x != None: # etsitään kohta, johon uusi alkio kuuluu
            p = x
            if new_node.key < x.key:
                x = x.left
            else:
                x = x.right
        new_node.parent = p # viitteet uuden alkion ja sen vanhemman välille
        if new_node.key < p.key:
            p.left = new_node
        else:
            p.right = new_node
            
    def min(self, x):
        while x.left != None:
            x = x.left
        return x
    
    def max(self, x):
        while x.right != None:
            x = x.right
        return x
    
    def succ(self, x):
        if x.right != None:
            return self.min(x.right)
        y = x.parent
        while y != None  and  x == y.right:
            x = y
            y = x.parent
        return y
    
    
    def delete(self, remove):
        
        # tapaus 1: poistettavalla ei lapsia
        if remove.left == None  and  remove.right == None:
            parent = remove.parent
            if parent == None: # poistettava on puun ainoa solmu
                self.root = None
                return remove
            if remove == parent.left:
                parent.left = None
            else:
                parent.right = None
            return remove
        
        # tapaus 2: poistettavalla on yksi lapsi
        if remove.left == None  or  remove.right == None:
            if remove.left != None:
                child = remove.left
            else:
                child = remove.right
            parent = remove.parent
            child.parent = parent
            if parent == None: # poistettava on juuri
                self.root = child
                return remove
            if remove == parent.left:
                parent.left = child
            else:
                parent.right = child
            return remove
            
        # tapaus 3: poistettavalla kaksi lasta
        successor = self.min(remove.right)
        remove.key = successor.key # korvataan poistettavan avain seuraajan avaimella
        child = successor.right
        parent = successor.parent # korvataan solmu successor sen lapsella
        if parent.left == successor:
            parent.left = child
        else:
            parent.right = child
        if child != None:
            child.parent = parent
        return successor
    
    
    def move(self, x, target=None, side=None):
        """Moves node to another place.
        
        Target link will be overwritten.
        Doesn't check binary search tree condition"""
        
        if x != None:
            if x.parent != None:
                if x.parent.left == x:
                    x.parent.left = None
                else:
                    x.parent.right = None
            x.parent = target
            
                
        if target != None:
            if side == 'left':
                if target.left != None:
                    target.left.parent = None
                target.left = x
            else:
                if target.right != None:
                    target.right.parent = None
                target.right = x
            
            
    
    def rotate(self, x):
        if x.parent == None:
            raise NameError('Node that will be rotated must have a parent.')
        
        # Save links to all nodes that will be changed and
        # deduce the direction of rotation.
        parent = x.parent
        grandparent = parent.parent
        if parent.left == x:
            child = x.right
            direction = 'right'
        else: 
            child = x.left
            direction = 'left'

        if parent == self.root:
            self.root = x

        # Move x:
        if grandparent != None:
            if grandparent.left == parent:
                self.move(x, grandparent, 'left')
            else:
                self.move(x, grandparent, 'right')
        else:
            self.move(x, None)

        # Move x's child and parent: 
        if direction == 'right':
            self.move(child, parent, 'left')
            self.move(parent, x, 'right')
        else:
            self.move(child, parent, 'right')
            self.move(parent, x, 'left')


    def zig_zig(self, x):
        #  Structure of the tree in zig-zig, zag-zag is a mirror image of this.
        #
        #   greatgrandparent
        #          |
        #     grandparent
        #       /     \
        #    parent    D
        #     /  \
        #    x    sibling
        #   / \
        #  A   child
        
        if x.parent == None  or  x.parent.parent == None:
            raise NameError('Zig-zigged or zag-zagged node must have parent and grandparent')
        
        # Save links to all nodes that will be changed and
        # deduce the direction of rotation (zig-zig or zag-zag).
        parent = x.parent
        grandparent = x.parent.parent
        greatgrandparent = x.parent.parent.parent
        if x == parent.left  and  parent == grandparent.left:
            operation = 'zig-zig'
            child = x.right
            sibling = parent.right
        elif x == parent.right  and  parent == grandparent.right:
            operation = 'zag-zag'
            child = x.left
            sibling = parent.left
        else:
            raise NameError('Path from grandparent to node is not left.left or right.right')  
        
        if grandparent == self.root:
            self.root = x

        # Move x:
        if greatgrandparent != None:
            if greatgrandparent.left == grandparent:
                self.move(x, greatgrandparent, 'left')
            else:
                self.move(x, greatgrandparent, 'right')
        else:
            self.move(x, None)
        
        # Move other nodes:
        if operation == 'zig-zig':
            self.move(parent, x, 'right')
            self.move(grandparent, parent, 'right')
            self.move(child, parent, 'left')
            self.move(sibling, grandparent, 'left')
        else:
            self.move(parent, x, 'left')
            self.move(grandparent, parent, 'left')
            self.move(child, parent, 'right')
            self.move(sibling, grandparent, 'right')
    
    
    def print_tree(self, x):
        if x != None:
            self.print_tree(x.left)
            print x.key
            self.print_tree(x.right)
    
            
    def print_tree_vertical(self, x, depth=0, between=[]):
        SPACE = 4
        if len(between) <= depth:
            between.append(0)
        if x != None:
            for i in range(depth):
                if between[i] == 1:
                    print '│ ',
                else:
                    print '  ', 
                print SPACE * ' ',
            if x.parent != None:
                if x.parent.left == x:
                    if x.parent.right == None:
                        print '└─',
                    else:
                        print '├─',
                        between[depth] = 1
                else:
                    print '└─',
                    if between[depth] == 1:
                        between[depth] = 0
            else:
                print '  ',
            print str(x.key),
            if x.left != None  or  x.right != None:
                print (SPACE - len(str(x.key))) * '─' + '┐',
            print
            self.print_tree_vertical(x.left, depth+1, between)
            self.print_tree_vertical(x.right, depth+1, between)
