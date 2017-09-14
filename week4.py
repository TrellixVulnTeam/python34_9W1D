def test():
    lst = [1,4,6,78]
    for x in lst:
        if x % 2 == 0:
            print(x)


    for x in range(1,15,3):
        print(x)

#following implementation BAD
        #fails for lst = [1,2,2,1]
def asc(lst):

    for e in lst[:-1]:
        nexte = lst[lst.index(e) + 1]
        print(e,nexte)
        if e > nexte:
            return False
    return True

#good implementation
def asc(lst):

    for index in range(0, len(lst)-1):
        e = lst[index]
        nexte = lst[index+1]
        if e > nexte:
            return False
    return True

#check for list being arithmetical
def arithmetical(lst):
    'lst contains numbers in arithmetical sequence'

    if len(lst) < 2:
        return True
    diff = lst[1] - lst[0]
    for index in range(0, len(lst)-1):
        e = lst[index]
        nexte = lst[index+1]
        if nexte - e != diff:
            return False
    return True

def four(w):
    'print all consecutive four-letter subwords of w'

    if len(w) <= 3:
        return
    
    for i in range(0,len(w)-3):
        print(w[i:i+4])

def palindrome(w):
    'is w a palindrome'
    for i in range(len(w)):
        print(w[i], w[-i-1])

#slightly more efficient version
def palindrome(w):
    'is w a palindrome'
    for i in range(len(w)//2):
        if w[i] != w[-i-1]:
            return False
        #print(w[i], w[-i-1])
    return True

#def sum(lst):
#
#    s = 0
#    for e in lst:
#        s += e
#    return s

def sump(lst):
    'sum positive values in lst'
    
    s = 0
    for e in lst:
        if e >= 0:
            s += e
    return s

def count(s,t):
    'how often does s occur in t'

    s == t[:len(s)]

#1st step
def count(s,t):
    'how often does s occur in t'

    i = 0
    s == t[i:len(s)+i]
    
def count(s,t):
    'how often does s occur in t'

    ctr = 0
    for i in range(0, len(t) - len(s) + 1):
        if s == t[i:len(s)+i]:
            ctr += 1
    return ctr

def divisors(n):
    'return list of all divisors of n'
    
    divs = []

    for i in range(1, n+1):
        if n % i == 0: #i is a divsor of n
            #divs = divs + [i]
            divs += [i]
            #divs.append(i)
    return divs

#slightly more efficient version
def divisors(n):
    'return list of all divisors of n'

    divs = []

    for i in range(1, n//2+1):
        if n % i == 0: #i is a divsor of n
            #divs = divs + [i]
            divs += [i]
            #divs.append(i)
    divs += [n]
    return divs

#average score of student sname in file fname
def avg_score(fname, sname):
    'read fname, and find average score for sname'

    infile = open(fname, 'r')
    records = infile.readlines()
    infile.close()

    for record in records:
        lst = record.split(',')
        lname = lst[0]
        print(lname)

#some helper functions for following
def average(lst):
    return sum(lst)/len(lst)

def clean(lst):
    'convert list lst of strings into list of integers'
    intlst = []

    for e in lst:
        intlst.append(eval(e))

    return intlst

#1st step
def avg_score(fname, sname):
    'read fname, and find average score for sname'

    infile = open(fname, 'r')
    records = infile.readlines()
    infile.close()

    for record in records[2:]:
        lst = record.split(',')
        lname = lst[0]
        scores = clean(lst[1:])
        #print(scores)
        print(lname, average(scores))
        
#final version
def avg_score(fname, sname):
    'read fname, and find average score for sname'

    infile = open(fname, 'r')
    records = infile.readlines()
    infile.close()

    for record in records[2:]:
        lst = record.split(',')
        lname = lst[0]
        scores = clean(lst[1:])
        if lname == sname.upper():
            print('{} has average score {:.2f}'.\
                  format(lname, average(scores)))
            return
    print('{} not found.'.format(sname))

#calculate median
def median(lst):

    if len(lst) == 0:
        return
    lst.sort()
    return lst[(len(lst)-1)//2]

#median class score
def med_score(fname):
    'read fname, and find median class score'

    infile = open(fname, 'r')
    records = infile.readlines()
    infile.close()

    averages = []

    for record in records[2:]:
        lst = record.split(',')
        lname = lst[0]
        scores = clean(lst[1:])
        averages.append(average(scores))

    averages.sort()
    print( averages )
    return median(averages)



       
