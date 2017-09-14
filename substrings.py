#function evolves step by step, until we have nested loop

#fix starting position (0), and try different values for j
def substrings(s):
    for j in range(1, len(s)+1):
        print(s[0:j])

#make starting position a variable (try i = 2, 3, ...
        #need to change range(1, ...) to range(i+1, ...)
def substrings(s):
    i = 1
    for j in range(i+1, len(s)+1):
        print(s[i:j])

#or, for easier testing, pass i as parameter
def substrings(s,i):
    for j in range(i+1, len(s)+1):
        print(s[i:j])

#finally, let i range over all possible values
def substrings(s):
    for i in range(0, len(s)):
        for j in range(i+1, len(s)+1):
            print(s[i:j])
