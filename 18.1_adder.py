'''
Write a function that adds two numbers. You should not use + or any arithmetic
operators
'''


def add(a, b):
    if (b == 0): return a
    sum = a ^ b #binary add don't carry
    carry = (a & b) << 1 #carry but dont add
    return add(sum, carry)


if __name__ == "__main__":
    assert 5 == add(1,4)
    assert 5 == add(4,1)
    assert 541 == add(41,500)
    



