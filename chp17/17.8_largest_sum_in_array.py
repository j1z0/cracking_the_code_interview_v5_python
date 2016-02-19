'''
You are given an array of integers (both positive and negative). Find the contiguous sequence with the largest sum. Return the sum
'''


def largest_sum(array):
    '''
    [4,7,-6,9,-4,-2,3]
    '''

    max_sum = 0
    summ = 0

    for val in array:
        summ += val
        if summ > max_sum:
            max_sum = summ
        elif summ < 0:
            summ = 0


    return max_sum

if __name__ == "__main__":
    print largest_sum([4,7,-2,19,-32,8])

