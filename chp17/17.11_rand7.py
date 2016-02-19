'''Implement a method rand70 given randSQ- That is,given a method that generates a random number between 0 and 4 (inclusive), write a method that generates a random number between 0 and 6 (inclusive).
'''
from random import randint

def rand5():
    return randint(0,5)


def rand7():
    '''
    assume we only have rand5()
    '''

    #rand5() + 2  # that doesnt give us 0 or 1
    while True:
        val = 5 * rand5() + rand5()
        if val < 21:
            return val % 7



if __name__ == "__main__":
    for i in range(10):
        print(rand7())
