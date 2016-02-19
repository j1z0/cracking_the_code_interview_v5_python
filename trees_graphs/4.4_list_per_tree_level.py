'''
Given a binary tree, design an algorithm which creates a linked list of all the nodes at each depth (e.g., if you have a tree with depth D, you'll have D linked lists).
'''

def make_lists(nodes, lists=None):
    if not nodes: return

    if not type(nodes) is list:
        nodes = [nodes]

    if lists is None:
        lists = [nodes]

    next_level = []
    for c in nodes:
        if c.leftChild:
            next_level.append(c.leftChild)
        if c.rightChild:
            next_level.append(c.rightChild)

    if next_level:
        lists.append(next_level)
        make_lists(next_level, lists)

    return lists


if __name__ == "__main__":
    from binary_tree import Tree, Node
    bst = Tree()
    assert bst.insert(40)
    assert bst.insert(25)
    assert bst.insert(10)
    assert bst.insert(32)
    assert bst.insert(78)
    assert bst.insert(77)
    assert bst.insert(7)
    lists = make_lists([bst.root])
    for lst in lists:
        x = " ".join([str(l.value) for l in lst])
        print(x)
    






