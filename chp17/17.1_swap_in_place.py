'''make a function to swap a numbe rin place (that is, wihtout temporary variables)
'''


def swap(number):
    snum = list(str(number))
    snum[0],snum[1] = snum[1],snum[0]

    return int("".join(snum))

def harder_swap(a, b):
    if a != b:
        a = a - b
        b = b + a
        a = b - a

    print("a",a,"b",b)

def swapper(a,b):

    a = a ^ b
    b = a ^ b
    a = a ^ b

    return a,b

def swap_bitwise(a,b):

    a,b = swapper(a,b)

    print("a",a,"b",b)

def swap_chars(a,b):

    a = ord(a)
    b = ord(b)

    a,b = swapper(a,b)

    print("a",chr(a),"b",chr(b))

if __name__ == "__main__":
    assert 51 == swap(15)
    harder_swap(2.1,1.2)
    harder_swap(7898989,37897898.2)
    harder_swap(1,1)

    swap_bitwise(2432432,122222)
    swap_bitwise(7,3)
    swap_chars("a","c")

