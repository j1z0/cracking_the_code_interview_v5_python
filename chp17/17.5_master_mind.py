'''
TheCameof Master Mind isplayed asfollows:
The computer has four slots, and each slot will contain a ball that is red (R), yellow (Y), green (C) or blue (B). For example, the computer might have RGGB (Slot # 1 isred, Slots #2 and #3 are green, Slot #4 is blue).
You, the user, are trying to guess the solution. Youmight, for example, guess YRGB.
When you guess the correct color for the correct slot, you get a "hit." If you guess a color that exists but is in the wrong slot, you get a "pseudo-hit." Note that a slot that is a hit can never count as a pseudo-hit.
For example,if the actual solution is RGBYandyou guess GGRR, you have one hit and onepseudo-hit.
Write a method that, given a guess and a solution, returns the number of hits and pseudo-hits
'''


def how_many_hits(guess, solution):
    '''
    guess = [YRGB]
    solu = [YRGB]
    '''

    hits, pseudos = 0, 0
   
    possible_pseudos = []
    guess_pseudos = []
    for idx, val in enumerate(solution):
        if guess[idx] == val:
            hits += 1
        else:
            possible_pseudos.append(val)
            guess_pseudos.append(guess[idx])

    for val in guess_pseudos:
        if val in possible_pseudos:
            pseudos += 1

    return hits, pseudos


if __name__ == "__main__":

    y = 'Y'
    r = 'R'
    g = 'G'
    b = 'B'

    print(how_many_hits([y,r,g,b],[y,r,g,b]))
    print(how_many_hits([y,r,b,g],[y,r,g,b]))
    print(how_many_hits([y,r,r,g],[y,r,g,b]))



