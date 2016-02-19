'''
Implement a function void reverse(char* str) in C or C++ which reverses a null- terminated string.
'''

def reverse(string):
    '''reverse in place'''

    string_len = len(string)
    if string_len <= 1 : return string
    last = string_len - 1
    string = list(string)

    for i in range(string_len / 2):
        string[i], string[last - i] = string[last -i], string[i]

    return "".join(string)

def reverse_words(string):
    '''reverse words in a string'''

    r = []
    for words in string.split():
        r.insert(0, words)

    return [r for r in reversed(string.split())]



if __name__ == "__main__":
    print reverse_words("see the dog jump")
    print reverse('abcdefghijk')
    print reverse('abcdefghij')
    print reverse('ab')
    print reverse('aaaabbb')



