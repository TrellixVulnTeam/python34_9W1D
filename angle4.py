from math import acos, pi

a = float(input('Please enter a: '))
b = eval(input('Please enter b: '))
c = eval(input('Please enter c: '))

if a > 0 and b > 0: #good inputs
    gamma = acos( (a*a+b*b-c*c)/(2*a*b) ) \
            / pi * 180

    print(gamma)
else: #bad inputs
    if a < 0: #a is bad
        print('a has to be positive')
    else: #if a is good, then b has to be bad
        print('b has to be positive')
print('The program is done')
