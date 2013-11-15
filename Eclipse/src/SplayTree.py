class TreeNode:
    def __init__(self, key=None, node_parent=None, left=None, right=None):
        self.node_parent = node_parent
        self.key = key
        self.left = left
        self.right = right


class BinarySearchTree:
    
    def __init__(self, root=None):
        self.root = root
        
    def search(self, search_key):
        x = self.root
        if x == None or x.key == search_key:
            return x
        if search_key < x.key:
            return self.search(x.left, search_key)
        else:
            return self.search(x.right, search_key)