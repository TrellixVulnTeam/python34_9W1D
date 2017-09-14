#better, more general solution (though doesn't work for empty list, try, why?
#also: had side effects; changes list that is being passed to it

def median(lst):
    'returns the median of a list'
    lst.sort()
    n = len(lst)
    #print(lst[n//2])
    return(lst[(n-1)//2])
    #the following will work for empty list:
    #return(lst[(max(n-1,0))//2])
