'''
Imp/emen t a function to check if a binary tree is a binary search tree
'''
from binary_tree import Node, Tree
import sys 
def is_bst(node, min_val=None, max_val=None):

    if min_val is None:
        min_val = -sys.maxint - 1
    if max_val is None:
        max_val = sys.maxint

    if node is None:
        return True

    if node.value <= min_val or node.value > max_val:
        return False

    if (not is_bst(node.leftChild, min_val, node.value) or
        not is_bst(node.rightChild, node.value, max_val)):
            return False

    return True

if __name__ == "__main__":

    bst = Tree()
    assert bst.insert(40)
    assert bst.insert(25)
    assert bst.insert(10)
    assert bst.insert(32)
    assert bst.insert(78)
    assert(is_bst(bst.root))

