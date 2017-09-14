#various ways to check prefix

def prefix(s,t):

    return t[:len(s)] == s

def prefix(s,t):

    return t.startswith(s)

def prefix(s,t):

    if len(s) > len(t):
        return False
    for i in range(len(s)):
        if s[i] != t[i]:
            return False
    return True

def occurs(name, word):
    'return occurrences of word in name with context'
    infile = open(name, 'r')
    text = infile.read()
    infile.close()

    words = text.split(' ')

    for i in range(len(words)):
        #print(i, words[i])
        if words[i] == word:
            #print(words[i-5:i+5])
            print(' '.join(words[i-5:i+5]))
            print('\n')


def strip(s):
    'remove all non-letter characters'
    t = ''
    for letter in s:
        if letter.isalpha():
            t += letter
    return t

#same, with join method and list comprehension
def strip(s):
    'remove all non-letter characters'
    return ''.join([letter for letter \
                    in s if letter.isalpha()])


def freq(name):
    infile = open(name, 'r')
    text = infile.read()
    infile.close()

    text = strip(text).lower()

    for i in range(ord('a'), ord('z')+1):
        letter = chr(i)
        print('{} has frequency {:.2f}'.\
              format(letter, text.count(letter)/len(text)*100))

#on the way to nested loops, 1st
def square(n):

    print('*****')
    print('*****')
    print('*****')
    print('*****')
    print('*****')

#2nd, abstract repeated prints
def square(n):

    for i in range(n):
        print('*****')

#3rd, abstract repeated asterisks
def line(n):

    for j in range(n):
        print('*', end = '')
    print()

#4th hidden nested loop
def square(n):

    for i in range(n):
        line(n)

#finally, nested loop
def square(n):

    for i in range(n):
        for j in range(n):
            print('*', end = '')
        print()

def square(n):

    for i in range(n):
        print(n*'*')

def triangle(n):
    'draw left-aligned triangle of side-length n'
    for i in range(n):
        for j in range(i+1):
            print('*', end = '')
        print()

def rtriangle(n):
    'draw right-aligned triangle of side-length n'
    for i in range(n):
        for j in range(n-i-1):
            print(' ', end = '')
        for j in range(i+1):
            print('*', end = '')
        print()

#really, only one loop needed
def rtriangle(n):
    'draw right-aligned triangle of side-length n'    

    for i in range(n):
        for j in range(n):
            if j < n-i-1:
                print(' ', end = '')
            else:
                print('*', end = '')
        print()

def comb(lst1, lst2):
    'create all combinations of list elements'
    results = []
    for item1 in lst1:
        for item2 in lst2:
            results.append(str(item1) + ' ' + str(item2))
            #print(str(item1) + ' ' + str(item2))
    return results

def subwords(w):
    'create all subwords of w'
    lst = ['']
    for i in range(len(w)):
        for j in range(i+1, len(w)+1):
            lst.append(w[i:j])
    return lst

def intersect(lst1, lst2):
    'intersection of lst1 and lst2'
    intersection = []
    for item1 in lst1:
        for item2 in lst2:
            if item1 == item2:
                intersection.append(item1)
    return intersection

def intersect(lst1, lst2):
    'intersection of lst1 and lst2'
    
    intersection = []
    for item1 in lst1:
        if item1 in lst2:
            intersection.append(item1)
    return intersection

def print2d(lst):
    'print 2-dimensional lst'

    for row in lst:
        for item in row:
            print(item, end = ', ')
        print()

def sumrow(lst):
    'sum each row of lst and return list of results'
    result = []
    #s = 0 #bad
    for row in lst:
        s = 0
        for item in row:
            #s = 0 #bad
            s += item
        result.append(s)
    return result

def sumall(lst):
    'sum all elements of 2-dimensional lst'
    #result = []
    s = 0 
    for row in lst:
        #s = 0 bad
        for item in row:
            #s = 0 #bad
            s += item
        #result.append(s)
    return s

def lower(w):
    return w[0].islower()

#first while loop, problem: range error if no upper case character
def firstup(lst):
    'return first upper case word in lst'

    i = 0
    while(lower(lst[i])):
        i += 1
    return lst[i]

#following fixes the problem, but won't work for all situations
def firstup(lst):
    'return first upper case word in lst'
    
    i = 0
    while(lower(lst[i])):
        i += 1
        if i >= len(lst):
            return # but what if we have more work to do
    return lst[i]

#adding a guarding statement, note that it's essential
#that Booleans expressions are short-circuit evaluated, and
#evaluated from left to right
def firstup(lst):

    i = 0
    while(i < len(lst) and lower(lst[i])):
        i += 1
    if i < len(lst): #so lower(lst[i]) failed
        return lst[i]
    else: # i < len(lst) fails, so i == len(lst)
        return

#proof: this version does not work
def firstup(lst):

    i = 0
    while(lower(lst[i]) and i < len(lst)):
        i += 1
    if i < len(lst): #so lower(lst[i]) failed
        return lst[i]
    else: # i < len(lst) fails, so i == len(lst)
        return    



def ltrim(w):
    'removes all spaces at the beginning of w'

    while(w[0] == ' '):
        w = w[1:]
    return w

def ltrim(w):
    'removes all spaces at the beginning of w'

    while(len(w) >= 1 and w[0] == ' '):
        w = w[1:]
    return w

def ltrim(w):
    'removes all spaces at the beginning of w'

    i = 0
    while(i < len(w) and w[i] == ' '):
        i += 1
    if i < len(w):
        return w[i:]
    else:
        return ''

            
def ulam(n):

    print(n, end = '->')
    while(n != 1):
        if n % 2 == 0:
            n = n//2
        else:
            n = 3*n+1
        print(n, end = '->')
    
