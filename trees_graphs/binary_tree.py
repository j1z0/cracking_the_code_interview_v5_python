'''a simple binary search tree implement preorder, postorder and inorder
traversal'''

class Node(object):

    def __init__(self, val):
        self.value = val
        self.leftChild = None
        self.rightChild = None

    def __str__(self):
        lval, rval = "-", "-"
        if self.leftChild:
            lval = self.leftChild.value
        if self.rightChild:
            rval = self.rightChild.value

        return "  %s \n / \\ \n%s   %s\n" % (self.value, lval, rval) 

    def insert(self, data):
        if self.value == data:
            return False
        elif self.value > data:
            if self.leftChild:
                return self.leftChild.insert(data)
            else:
                self.leftChild = Node(data)
                return True
        else:
            if self.rightChild:
                return self.rightChild.insert(data)
            else:
                self.rightChild = Node(data)
                return True

    def find(self, data):
        if (self.value == data):
            return True
        elif self.value > data:
            if self.leftChild:
                return self.leftChild.find(data)
            else:
                return False
        else:
            if self.rightChild:
                return self.rightChild.find(data)
            else:
                return False

    def preorder(self):
        print (str(self.value))
        if self.leftChild:
            self.leftChild.preorder()
        if self.rightChild:
            self.rightChild.preorder()

    def postorder(self):
        if self.leftChild:
            self.leftChild.postorder()
        if self.rightChild:
            self.rightChild.postorder()
        print(str(self.value))

    def inorder(self):
        if self.leftChild:
            self.leftChild.inorder()
        print (str(self.value))
        if self.rightChild:
            self.rightChild.inorder()


class Tree(object):

    def __init__(self):
        self.root = None

    def insert(self, data):
        if self.root:
            return self.root.insert(data)
        else:
            self.root = Node(data)
            return True

    def find(self, data):
        if self.root:
            return self.root.find(data)
        else:
            return False

    def preorder(self):
        print ("PreOrder")
        self.root.preorder()

    def postorder(self):
        print ("PostOrder")
        self.root.postorder()

    def inorder(self):
        print ("InOrder")
        self.root.inorder()

if __name__ == "__main__":
    print("running tests")
    bst = Tree()
    assert bst.insert(40)
    assert bst.insert(25)
    assert bst.insert(10)
    assert bst.insert(32)
    assert bst.insert(78)
    bst.preorder()
    bst.postorder()
    bst.inorder()
    print("all good")

