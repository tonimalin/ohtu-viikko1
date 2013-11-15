import SkipList
import SplayTree

skip_list = SkipList.SkipList()
i = 0
for i in range(40):
    skip_list.insert(i)
    i += 1
skip_list.print_list()
skip_list.print_nice()
print
for i in range(40):
    skip_list.delete(i)
    skip_list.print_nice()
    print
    
# treenode = SplayTree.TreeNode()
# treenode.key = 'avain'
# treenode.left = SplayTree.TreeNode('Uusi solmu')
# print treenode.key
# print treenode.left.key