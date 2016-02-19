'''
In the classic problem of the Towers of Hanoi, you have 3 towers and Ndisks of different sizes which can slide onto any tower. The puzzle starts with disks sorted in ascending order of size from top to bottom (i.e., each disk sits on top of an even larger one). You have the following constraints:
(1) Only one disk can be moved at a time.
(2) A disk is slid off the top of one tower onto the next tower.
(3) A disk can only be placed on top of a larger disk.
Write a program to move the disksfrom the first tower to the last using stacks.
'''

from stack import Stack
import sys

class Tower(object):

    def __init__(self, index):
        self.disks = Stack()
        self.index = index

    def add(self, data):
        if (not self.disks.empty and self.disks.peek() <= data):
            print("Error placing disk " + data)
        else:
            self.disks.push(data)

    def moveTopTo(self, tower):
        top = self.disks.pop()
        tower.add(top)
        print("Move disk %s from %s to %s" % (top, self.index, tower.index))

    def moveDisks(self, num_disks, dest_tower, buff_tower):
        if num_disks > 0:
            self.moveDisks(num_disks - 1, buff_tower, dest_tower)
            self.moveTopTo(dest_tower);
            buff_tower.moveDisks(num_disks - 1, dest_tower, self)
    

if __name__ == "__main__":
    num_disks = 5
    num_towers = 3
    towers = []
    for i in range(num_towers):
        towers.append(Tower(i))

    for i in range(num_disks, 0, -1):
        towers[0].add(i)

    towers[0].moveDisks(num_disks, towers[2], towers[1])



