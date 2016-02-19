'''
 Write a method to count the number of 2s between0 and 
 '''


def num_2s_brute_force(n):
     twos = 0
     for i in range(2, n+1):
         x = str(i)
         for j in range(len(x)):
             if x[j] == "2":
                twos += 1
    
     return twos


def num_2s(n):
    if n < 2: return 0
    twos = 0

    #get 2s at the end
    for i in range(2, n+1, 10):
        if i <= n:
            twos += 1

    #20s,200s,2000
    twenties = 20
    multiplier = 10

    #needs some recursive action here I think
    #to get stuff like 120,220,2220
    while n > twenties:
        for j in range(multiplier):
            if j + twenties < n:
                twos += 1

        twenties *= multiplier
        multiplier *= multiplier
    
    return twos

if __name__ == "__main__":
     print num_2s(10)
     print num_2s(30)
     print num_2s(100)
     print num_2s(230)
