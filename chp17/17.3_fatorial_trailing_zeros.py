'''
Write an algorithm which computes the number of trailing zeros in n factorial
'''
import math

def get_trailing_zeros_expensive(number):

    fact = math.factorial(number)

    fact = str(fact)

    for idx,char in enumerate(reversed(fact)):
        if char != "0":
            return idx


def get_trailing_zeros(number):

    if number < 5: return 0
  
    count = 0
    i = 5
    #zeros euqal number of times divisible
    #by multiples of five
    while (number / i > 0):
        count += number / i
        i *= 5

    return count



if __name__ == "__main__":
   
    print(math.factorial(1))
    print(get_trailing_zeros(1))
    print(math.factorial(5))
    print(get_trailing_zeros(5))
    print(math.factorial(10))
    print(get_trailing_zeros(10))
    print(math.factorial(15))
    print(get_trailing_zeros(15))
    print(math.factorial(150))
    print(get_trailing_zeros(150))



