#first version; trouble when a == 0 or b == 0

from math import acos, pi

a = float(input('Please enter a: '))
b = eval(input('Please enter b: '))
c = eval(input('Please enter c: '))

gamma = acos( (a*a+b*b-c*c)/(2*a*b) ) \
            / pi * 180

print(gamma)
