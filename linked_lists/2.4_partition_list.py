'''
Write code to partition a linked list around a value x, such that all nodes 
less than x come before all nodes greater than or equal to x.
'''
from linked_list import LinkedList

def partition_list(lst, x):
    node = lst.root

    while node:
        if node.data < x:
            data = node.data
            lst.delete(node.data)
            lst.add(data)

        node = node.next

    #test
    n = lst.root
    line = ""
    while n:
        line += str(n.data) + ","
        n = n.next

    print(line)


if __name__ == "__main__":
    l = LinkedList(1)
    l.add(4)
    l.add(2)
    l.add(7)
    l.add(5)
    
    partition_list(l,4)
    #shold return
    #4,2,1,5,7

    

