'''
Implement an algorithm to determine if a string has all unique characters. 
What if you cannot use additional data structures?
'''
from collections import defaultdict

def has_only_unique_chars(string):
    counter = defaultdict(int)
    for s in string:
        counter[s] +=1
        if counter[s] > 1:
            return False

    return True

def has_only_unique_chars_with_array(string):

    #asci only has 255 unique characters
    if len(string) > 256: return False

    found_chars = [False] * 255
    for s in string:
        if found_chars[ord(s)]:
            return False
        found_chars[ord(s)] = True

    return True





if __name__ == "__main__":
    assert has_only_unique_chars("abcdefghijklmnop")
    assert not has_only_unique_chars("aa")
    assert has_only_unique_chars("1234ufklebomn &*(^%$")
    assert not has_only_unique_chars("1234ufklebomn &*(^%$b")

    print("All good")

    assert has_only_unique_chars_with_array("abcdefghijklmnop")
    assert not has_only_unique_chars_with_array("aa")
    assert has_only_unique_chars_with_array("1234ufklebomn &*(^%$")
    assert not has_only_unique_chars_with_array("1234ufklebomn &*(^%$b")

    print("All good with array")

