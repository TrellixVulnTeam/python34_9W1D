from math import acos, pi

a = float(input('Please enter a: '))
b = eval(input('Please enter b: '))
c = eval(input('Please enter c: '))

#two-sided decision
if a > 0 and b > 0:
    gamma = acos( (a*a+b*b-c*c)/(2*a*b) ) \
            / pi * 180

    print(gamma)
else:
    print('One of a or b is negative')
print('The program is done')
