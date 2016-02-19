'''
Implement a method to perform basic string compression using the counts of repeated characters. For example, the string aabcccccaaa would become a2blc5a3. If the "compressed" string would not become smaller than the orig- inal string, your method should return the original string.
'''

def compress(string):
    
    buff = []
    last = string[0]
    count = 0
    for char in string:
        if last == char:
            count += 1
        else:
            buff.append(last)
            buff.append(str(count))
            last = char
            count = 1

    buff.append(last)
    buff.append(str(count))

    buff = "".join(buff)
    if len(buff) < len(string):
        return buff

    return string


if __name__ == "__main__":
    assert "a2b1c5a3" == compress("aabcccccaaa")
    assert "a5" == compress("aaaaa")
    assert "abcdd" == compress("abcdd")
    assert "a1b1c1d6" == compress("abcdddddd")


