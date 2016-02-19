'''
Given two strings, write a method to decide if one is a permutation of the other.
'''
from collections import defaultdict

def is_perm(str1, str2):
    if len(str1) != len(str2): return False

    str1_chars = defaultdict(int)  
    str2_chars = defaultdict(int) 


    for i in range(len(str1)):
        str1_chars[str1[i]] += 1
        str2_chars[str2[i]] += 1


    return str1_chars == str2_chars

def sort(string):
    temp = list(string)
    temp.sort()
    return "".join(temp)

def is_perm_with_sort(str1,str2):
    if len(str1) != len(str2): return False

    return sort(str1) == sort(str2)



if __name__ == "__main__":
    assert is_perm("1234", "4321")
    assert not is_perm("124", "4321")
    assert is_perm("aaaaaa", "aaaaaa")
    assert not is_perm("1224", "4321")
    print("All good!")
    assert is_perm_with_sort("1234", "4321")
    assert not is_perm_with_sort("124", "4321")
    assert is_perm_with_sort("aaaaaa", "aaaaaa")
    assert not is_perm_with_sort("1224", "4321")
    print("All good with sort!")
