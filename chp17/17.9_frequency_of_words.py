'''
Design a method to find the frequency of occurrences of any given word in a book.'''
from collections import defaultdict

def count_words(text):
    '''
    do this for repetitive queries so we only have to parse the file once
    '''

    wc = defaultdict(int)

    for w in text.split():
        wc[w.lower()] += 1

    return wc

def count_words_quick(text, word):
    '''
    do this if on a single query through the text
    '''
    count = 0
    word = word.lower()
    for w in text.split():
        if w.lower() == word:
            count += 1

    return count

if __name__ == "__main__":
    text = '''one dark day in The middle of the night two dead boys got up to fight back to back they
    faced each other drew thier spears and shot each other.'''

    wc = count_words(text)

    assert 1 == wc["middle"]
    assert 2 == wc["the"]
    assert 0 == wc["super"]


    assert 1 == count_words_quick(text, "middle")
    assert 2 == count_words_quick(text, "the")
    assert 0 == count_words_quick(text, "super")


