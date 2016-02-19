'''
Write a method to replace all spaces in a string with'%20'. You may assume that the string has sufficient space at the end of the string to hold the additional characters, and that you are given the "true" length of the string. (Note: if imple- menting in Java, please use a character array so that you can perform this opera- tion in place.)
EXAMPLE
Input: "Mr John Smith Output: "Mr%20Dohn%20Smith"
'''

def replace_space(string):
    '''this is too easy with python insert'''

    string = list(string)
    for x,char in enumerate(string):
        if char == " ":
            string.pop(x)
            string.insert(x, "0")
            string.insert(x, "2")
            string.insert(x, "%")

    return "".join(string)

def shift(shift_by, string, start, length):

    for x in range(length-1, start, -1): 
        string[x+shift_by] = string[x]

    print("shifted string is", string)
    return string


def replace_string_with_shift(string, length):
    '''assume we have to shift like in java'''
    string = list(string)
    for x in range(length):
        if string[x] == " ":
            string = shift(2, string,x,length)
            string[x] = '%'
            string[x+1] = '2'
            string[x+2] = '0'

    return string



if __name__ == "__main__":
    #print(replace_space("hello john"))
    print(replace_string_with_shift("hello john   ",10))


