import random

MAX_LEVEL = 20
p = .5


class Node:
    def __init__(self, level=1, key=None, value=None):
        self.forward = level * [None]
        self.key = key
        self.value = value



class SkipList:

    def __init__(self):
        self.header = Node(MAX_LEVEL)
        self.level = 1
        self.max_level = MAX_LEVEL
        
    def search(self, search_key):
        node = self.basic_search(search_key)[0]
        if node != None  and  node.key == search_key:
            return node.key
            # here node's value is the key
        else:
            return None
                    
    def basic_search(self, search_key):
        """Makes a search for insert, delete and search operations."""
        update = self.max_level * [None]
        node = self.header
        for i in range(self.level-1, -1, -1):
            while (node.forward[i] != None) and (node.forward[i].key < search_key):
                node = node.forward[i]
            update[i] = node
        node = node.forward[0]
        return [node, update]
            
    def insert(self, search_key, new_value=None):
        [node, update] = self.basic_search(search_key)
        if node != None  and  node.key == search_key:
            node.value = new_value
        else:
            lvl = random_level(self.max_level)
            if lvl > self.level:
                for i in range(self.level, lvl):
                    update[i] = self.header
                self.level = lvl
            node = Node(lvl, search_key, new_value)
            for i in range(lvl):    
                node.forward[i] = update[i].forward[i]
                update[i].forward[i] = node

    def delete(self, search_key):
        [node, update] = self.basic_search(search_key)
        if node != None  and  node.key == search_key:
            for i in range(self.level):
                if update[i].forward[i] != node: break
                update[i].forward[i] = node.forward[i]
            while self.level > 1 and self.header.forward[self.level-1] == None:
                self.level -= 1
        
    def skip_list_as_list(self):
        values = []
        node = self.header.forward[0]
        while node != None:
            values.append(node.key)    
            node = node.forward[0]
        return values
        
    def print_list(self):
        print 'levels: ', self.level
        node = self.header
        while node != None:
            print '\nkey:', node.key, '\tforward-links:',
            
            for i in range(len(node.forward)):
                if node.forward[i] == None:
                    print None,
                else:
                    print node.forward[i].key,
                    
            node = node.forward[0]
        print
        
    def print_nice(self):
        """ Print a vertical diagram of the structure."""
        width = 7
        print width * ' ' + self.level * (' * ')
        node = self.header.forward[0]
        while node != None:
            row = key_str = str(node.key)
            row += (width - len(key_str)) * ' '
            row += len(node.forward) * '---'
            row += (self.level - len(node.forward)) * ' | '
            print row 
            node = node.forward[0]
        print 'NIL' + (width - 3) * ' ' + self.level * '---' 
        
    def height(self):
        h = 0;
        node = self.header
        while node.forward[0] != None:
            h += 1
            node = node.forward[0]
        return h
        
    
    
def random_level(MAX_LEVEL):
    lvl = 1
    while random.random() < p and lvl < MAX_LEVEL:
        lvl += 1
    return lvl
    
