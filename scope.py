def add(y):
    x = 1
    print(y)
    return x + y

def add(y):
    print(y)
    return x + y

def h(n):
    print('Start h')
    print(1/n)
    print(n)

def g(n):
    print('Start g')
    h(n-1)
    print(n)

def f(n):
    print('Start f')
    g(n-1)
    print(n)

def add(y):
    global x
    x = 1
    print(y)
    return x + y


    
