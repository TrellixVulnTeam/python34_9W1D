def word():
    'prompt user for words (stop by entering empty word)'
    lst = []
    w = input('Word: ')
    while( len(w) > 0):
        lst.append(w)
        w = input('Word: ')
    return(lst)

#following code doesn't work, since Python doesn't have repeat/until
#def word():
#
#    lst = []
#    repeat
#        w = input('Word: ')
#        if len(w) > 0:
#            lst.append(w)
#    until (len(w) == 0)
#    return(lst)


def numb():
    'prompt user until they enter an integer number'

    x = input('Number: ')

    while(not x.isdigit()):
        x = input('Number: ')
        
    return eval(x)

#same with infinite loop
def numb():
    'prompt user until they enter an integer number'

    while(True):
        x = input('Number: ')
        if x.isdigit():
            return eval(x)

#using break        
def numb():

    while(True):
        x = input('Number: ')
        if x.isdigit():
            break
    print('Good input')
    return eval(x)

def count(s,t):
    'how often does s occur in t'
    ct = 0
    for i in range(len(t)-len(s)+1):
        if t[i:i+len(s)] == s:
            ct += 1
    return ct

#using nested loop, with break and Boolean flag
def count(s,t):
    'how often does s occur in t'
    ct = 0
    for i in range(len(t)-len(s)+1):
        mismatch = False
        for j in range(0, len(s)):
            if t[i+j] != s[j]:
                mismatch = True
                break
        if mismatch:
            pass
        else:
            ct += 1
    return ct


#while loop for Newton iteration
def sqrt(x,k):

    delta = 10**(-k)

    s = 1
    while(abs(s*s - x) >= delta):
        s = (s + x/s)/2
    return s


#dictionary of counters
def freq(name):
    infile = open(name, 'r')
    s = infile.read()
    infile.close()

    words = s.split()

    cts = {}
    for word in words:
        if word not in cts:
            cts[word] = 1
        else:
            cts[word] += 1

    lst = sorted(cts.items(), \
                key = lambda x: x[1], reverse = True)
    
    return lst[:100] #return 100 most frequent words, can change number
            
        

