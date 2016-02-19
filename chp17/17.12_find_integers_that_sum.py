'''
Design an algorithm to find all pairs of integers within an array which sum 
to a specified value
'''


def find_pairs(array, value):
    sums = {}

    for x in array:
        if sums.get(value - x):
            print(x, value - x)
        sums[x] = x





if __name__ == "__main__":
    find_pairs([1,2,3,4,5,], 6)
