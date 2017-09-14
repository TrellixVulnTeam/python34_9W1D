import time

#recursive solution for fibonacci
def fib(n):
    #print(n)
    if n <= 1:
        return n
    else:
        return fib(n-1) + fib(n-2)


def timing(f, n):
    'time function f on input n'
    start = time.time()
    f(n)
    end = time.time()

    return end - start

#get fibonacci runtimes for inputs a to b
def test(a,b):
    times = {}
    for i in range(a,b):
        times[i] = timing(fib, i)
        print(times[i])


#a memoized solution for fibonacci, computed alues are stored
def fib_env(n, fibval):
    
    if n in fibval:
        return fibval[n]
    elif n <= 1:
        return n
    else:
        a = fib_env(n-2, fibval)
        fibval[n-2] = a
        b = fib_env(n-1, fibval)
        return a+b       

#using the memoized version
def fib(n):
    return fib_env(n, {})

#best version: using iteration
def fib(n):

    if n <= 1:
        return n
    else:
        a,b = 0,1
        for i in range(n-1):
            a,b = b,a+b
        return b


def find(lst, x):
    'find element x in lst using binary search'
    #print(lst)
    n = len(lst)
    if n == 0:
        print('Not Found')
        return
    mid = n//2
    y = lst[mid]
    if x < y:
        find(lst[:mid], x)
    elif x == y:
        print('Found')
        return
    else: # x > y
        find(lst[mid+1:], x)

from random import randrange

#test find using a lst of 5000 random elements, try changing values
def test_f():
    lst = [randrange(10000) for i in range(5000)]
    lst.sort()
    find(lst, 2370)

#recursive solution to merge; blows stack
def merge(lst1, lst2):
    if len(lst1) == 0:
        return lst2
    elif len(lst2) == 0:
        return lst1
    else:
        a = lst1[0]
        b = lst2[0]
        if a < b:
            return [a] + merge(lst1[1:], lst2)
        else:
            return [b] + merge(lst1, lst2[1:])

#iterative solution
def merge(lst1, lst2):
    lst3 = []
    while(len(lst1) > 0 and len(lst2) > 0):
        a = lst1[0] #pick first elements of lst1 and
        b = lst2[0] #lst2
        if a < b: #append whichever is smaller, and remove from that lst
            lst3.append(a)
            lst1 = lst1[1:]
        else:
            lst3.append(b)
            lst2 = lst2[1:]
    if len(lst1) == 0:
        lst3 += lst2 #add rest of lst2
    else:
        lst3 += lst1 #add rest of lst1
    return lst3
    
def mergesort(lst):
    'recusive mergesort'
    n = len(lst)
    if n <= 1:
        return lst
    mid = n//2
    lst1 = lst[:mid]
    lst2 = lst[mid:]
    return merge(mergesort(lst1), mergesort(lst2))

#testrunning mergesort on list of 10000 random elements
def test_f():
    lst = [randrange(100000) for i in range(10000)]
    return mergesort(lst)
