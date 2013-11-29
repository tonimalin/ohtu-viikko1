# -*- coding: utf_8 -*-
'''
Created on 27.11.2013

@author: Toni
'''
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
            elif new_node.key > x.key: 
                x = x.right
            else:
                raise ValueError('Attempted to insert duplicate key value.')
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

    
    def rotate(self, x):
        if x.parent == None:
            raise NameError('Node that will be rotated must have a parent.')
        if x == x.parent.left:
            self.rotate_right(x)
        else:
            self.rotate_left(x)


    def rotate_right(self, x):
        child = x.right
        parent = x.parent
        grandparent = x.parent.parent
        self.rotate_root_and_grandparent_operations(x, parent, grandparent)
        parent.left = child
        if child:
            child.parent = parent
        x.right = parent
        parent.parent = x
        
        
    def rotate_left(self, x):
        child = x.left
        parent = x.parent
        grandparent = x.parent.parent
        self.rotate_root_and_grandparent_operations(x, parent, grandparent)
        parent.right = child
        if child:
            child.parent = parent
        x.left = parent
        parent.parent = x
        
        
    def rotate_root_and_grandparent_operations(self, x, parent, grandparent):
        if parent == self.root:
            self.root = x
            x.parent = None
        else:
            x.parent = grandparent
            if parent == grandparent.left:
                grandparent.left = x
            else:
                grandparent.right = x

    
    def tree_as_list(self, x='root'):
        if x == 'root':
            x = self.root
        if x != None:
            return self.tree_as_list(x.left) + [x.key] + self.tree_as_list(x.right)
        else:
            return []
        
            
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
            
