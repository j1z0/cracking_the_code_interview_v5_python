'''
Write a method to randomly generate a set of m integers from an array of size n.
Each element must have equal probability of being chosen
'''
import random

def gen(array, set_size):
    arr_len = len(array)

    retval = []
    #get random number between 0 - arr_len - 1
    for i in range(set_size):
        idx = random.randint(0, arr_len -1)
        retval.append(array[idx])


    return retval


if __name__ == "__main__":
    print(gen([1,4,5,6,7,2,3,8,9], 6))
    print(gen([1,4,5,6,7,2,3,8,9], 6))
    print(gen([1,4,5,6,7,2,3,8,9], 6))
