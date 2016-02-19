from binary_tree import Tree, Node

'''The following is simple but O(n^2)'''
def getHeight1(node):
    if node is None: return 0

    return max(getHeight(node.leftChild), getHeight(node.rightChild)) + 1


def is_balanced1(root):
    if root is None: return True

    hDiff = getHeight(root.leftChild) - getHeight(root.rightChild)

    if abs(hDiff) > 1:
        return False
    else:
        return is_balanced(root.leftChild) and is_balanced(root.rightChild)

'''improve it by having getHeight check if balanced runs in O(n)'''
def getHeight(node):
    if node is None: return 0

    #check if sub trees are not balanced
    leftHeight = getHeight(node.leftChild)
    if leftHeight == -1:
        return -1
    
    rightHeight = getHeight(node.rightChild)
    if rightHeight == -1:
        return -1

    if abs(leftHeight - rightHeight) > 1:
        return -1 
    else:
        return max(leftHeight, rightHeight) + 1


def is_balanced(root):
    if root is None: return True

    if getHeight(root) == -1:
        return False
    else:
        return True



if __name__ == "__main__":
    bst = Tree()
    bst.insert(10)
    assert is_balanced(bst.root)
    bst.insert(8)
    assert is_balanced(bst.root)
    bst.insert(12)
    assert is_balanced(bst.root)
    bst.insert(5)
    bst.insert(6)
    assert not is_balanced(bst.root)
    print("all good")






