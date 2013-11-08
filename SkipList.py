# Define a Node class. Every Node has a value and a pointer to the next node.
# When a node is first created, it's assigned a given value and does not point to any node.
# class Node:
    # """Defines a node."""
    # def __init__(self, data):
        # self.data = data
        # self.next = None


        
# Define a LinkedList class. In this example, LinkedList holds a pointer to the first (head)
# and last (tail) node in the list. It also contains functions to later add/remove nodes
# and display the list. A linked list is empty when created; thus there are no "head" or
# "tail" nodes at this point.
# class LinkedList:
    # def __init__(self):
        # self.head = None
        # self.tail = None

    # def AddNode(self, data):
        # new_node = Node(data)
        
        # if self.head == None:
            # self.head = new_node
            
        # if self.tail != None:
            # self.tail.next = new_node
            
        # self.tail = new_node
        

    # def RemoveNode(self, index):
    
        # prev = None
        # node = self.head
        # i = 0
        
        # while (node != None) and (i < index):
            # prev = node
            # node = node.next
            # i += 1
            
        # if prev == None:
            # self.head = node.next
        # else:
            # prev.next = node.next
  
  
    # def PrintList(self):
    
        # node = self.head
        
        # while node != None:
            # print node.data
            # node = node.next

            
            
class Node:
    def __init__(self):
        self.forward = [None]
        self.key = None

            
class SkipList:


    def __init__(self):
        self.header = Node()
        self.level = 1
        
        
    def search(self, search_key):
        node = self.header
        for i in range(self.level, 0, -1):
            while 1==1:
                pass
    
    
    def print_list(self):
        print 'tasoja: ', self.level
        node = self.header
        while node != None:
            print '\nkey:', node.key, 'forward-linkit:'
            for i in range(len(node.forward)):
                print '  '
                if node.forward[i] == None:
                    print None
                else:
                    print i, node.forward[i].key
            print
        # tulostetaan jokainen solmu ja kaikki sen linkit
        
        
skip_list = SkipList()
skip_list.print_list()