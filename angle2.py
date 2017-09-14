from math import acos, pi

a = float(input('Please enter a: '))
b = eval(input('Please enter b: '))
c = eval(input('Please enter c: '))

#BAD code: if a and b > 0:

#catch bad inputs (zero or negative)
if a > 0 and b > 0:
    gamma = acos( (a*a+b*b-c*c)/(2*a*b) ) \
            / pi * 180

    print(gamma)
print('The program is done')
