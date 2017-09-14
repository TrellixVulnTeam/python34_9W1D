#median function; uses brute-force to find median (trying all possible orderings)

def median(x,y,z):
    'return the median of x, y, and z'
    if x <= y <= z:
        return y
    elif x <= z <= y:
        return z
    elif y <= x <= z:
        return x
    elif y <= z <= x:
        return z
    elif z <= x <= y:
        return x
    else:
        return y
