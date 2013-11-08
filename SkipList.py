import random

max_level = 10
p = .5


class Node:
    def __init__(self, level=1, key=None, value=None):
        # self.forward = level * [None]
        self.forward = max_level * [None]
        self.key = key
        self.value = value



class SkipList:


    # def __init__(self, max_level=10):
    def __init__(self):
        self.header = Node()
        self.level = 1
        self.max_level = max_level
        
        
    def search(self, search_key):
    
        node = self.header
        
        for i in range(self.level-1, -1, -1):
        
            while (node.forward[i] != None) and (node.forward[i].key < search_key):
                node = node.forward[i]
                
        node = node.forward[0]
        
        if node != None  and  node.key == search_key:
            return node.key
            # alkuperäisessä palautetaan solun sisältämä arvo, tässä käytetään arvona avainta
        else:
            return None
            
            
    def insert(self, search_key, new_value=None):
    
        # local update[1..MaxLevel]
        update = self.max_level * [None]
        
        node = self.header
        
        for i in range(self.level-1, -1, -1):
        
            while (node.forward[i] != None) and (node.forward[i].key < search_key):
                node = node.forward[i]
            
            update[i] = node
            
        node = node.forward[0]
        
        if node != None  and  node.key == search_key:
            node.value = new_value
        else:
            lvl = random_level(self.max_level)
            if lvl > self.level:
                for i in range(self.level, lvl):
                    update[i] = self.header
                self.level = lvl
            node = Node(lvl, search_key, new_value)
            for i in range(lvl):    #
                node.forward[i] = update[i].forward[i]
                update[i].forward[i] = node

        
    def print_list(self):
        print 'tasoja: ', self.level
        node = self.header
        while node != None:
            print '\nkey:', node.key, '\nforward-linkit:'
            
            for i in range(len(node.forward)):
                print ' ',
                if node.forward[i] == None:
                    print None
                else:
                    print i, node.forward[i].key
                    
            print
            node = node.forward[0]
        # tulostetaan jokainen solmu ja kaikki sen linkit
        
    
    
def random_level(max_level):
    lvl = 1
    while random.random() < p and lvl < max_level:
        lvl += 1
    return lvl
    
    
        
skip_list = SkipList()
skip_list.print_list()
for i in range(10):
    skip_list.insert(i)
skip_list.print_list()