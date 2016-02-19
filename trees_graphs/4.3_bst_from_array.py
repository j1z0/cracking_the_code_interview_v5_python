

def create_bst(array):
    '''Given a sorted (increasin gorder) array with unique 
    integer elements, write an algorithm to create a binary 
    search tree with minimal height.
    ex: [1,2,3,4,5,6]
    '''
    mid = len(array) // 2

    t = Tree(array[mid])
    insert_child(t,array,mid,[mid])

def insert_child(t, array, mid, picked):

    idx = int(round(mid / 2.0)) 

    left = mid - idx
    right = mid + idx

    if (left >= 0) and (left not in picked):
        t.insert(array[left])
        picked.append(left)
        insert_child(t, array, left, picked)
    if (right < len(array)) and (right not in picked):
        t.insert(array[right])
        picked.append(right)
        insert_child(t, array, right, picked)



class Node(object):

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, data):
        print("data", data)
        if self.value == data: return None
        if data < self.value:
            if self.left:
                print("go left for data", data)
                self.left.insert(data)
            else:
                print("insert left data", data)
                self.left = Node(data)
        else:
            if self.right:
                print("go right for data", data)
                self.right.insert(data)
            else:
                print("insert right for data", data)
                self.right = Node(data)

class Tree(object):

    def __init__(self, root):
        self.root = Node(root)

    def insert(self, value):
        if not self.root:
            node = Node(value)
            self.root = node
        else:
            self.root.insert(value)

if __name__ == "__main__":
    create_bst([1,2,3,4,5,6,7])

    #start in middle
    #then add middle of left
    #then add middle of right
    #
