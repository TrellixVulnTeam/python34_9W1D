
def trace(m):
    sum = 0
    for i in range(0, len(m)):
        sum += m[i][i]
    return(sum)    

def improve(lst):
    while(sum(lst) <= 0):
        if(len(lst) == 0):
            print("Sorry, but cannot be improved.")
            return
        lst.remove(min(lst))
    print("Transactions: {}. Value: {}".format(lst, sum(lst)))

def juggle(n):
    print(str(n))
    while(n != 1):
        if(n % 2 == 0):
            n = int(n**0.5)
        else:
            n = int(n**1.5)
        print(str(n))

def triangle1(n):
     for row in range(0, n):
         for column in range(0, n-row):
             print("*", end = "")
         print()
        

def triangle2(n):
    for row in range(0, n):
        for column in range(0, n):
            if(row > column):
                print(" ", end = "")
            else:
                print("*", end = "")
        print()        
    
        
