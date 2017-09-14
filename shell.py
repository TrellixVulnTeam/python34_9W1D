Python 3.3.0 (v3.3.0:bd8afb90ebf2, Sep 29 2012, 10:55:48) [MSC v.1600 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> 3+4*5
23
>>> 3-4*5
-17
>>> 3*4+5
17
>>> (3+4)*5
35
>>> 3/4
0.75
>>> 1/2
0.5
>>> 1/10
0.1
>>> 1/3
0.3333333333333333
>>> 10 % 2
0
>>> 100 % 3
1
>>> 100 / 3
33.333333333333336
>>> 100 // 3
33
>>> 100 % 7
2
>>> 10**3
1000
>>> 5**2
25
>>> 2**3*4
32
>>> 2**3**4
2417851639229258349412352
>>> (2**3)**4
4096
>>> 2**(3**4)
2417851639229258349412352
>>> abs(-10)
10
>>> abs(10)
10
>>> min(10,-13,-100,90)
-100
>>> min(100,90,23,54,1,10)
1
>>> max(100,2,1400)
1400
>>> x = 4
>>> y = 6
>>> x+y
10
>>> x = y+1
>>> x
7
>>> x = x+1
>>> x
8
>>> x = x+1
>>> x
9
>>> x = x+1
>>> x
10
>>> x = x+y
>>> x
16
>>> x = x*y
>>> x
96
>>> P = 1000
>>> r = 4/100
>>> n = 12
>>> t = 30
>>> A = P(1+r/n)**nt
Traceback (most recent call last):
  File "<pyshell#43>", line 1, in <module>
    A = P(1+r/n)**nt
TypeError: 'int' object is not callable
>>> A = P*(1+r/n)**nt
Traceback (most recent call last):
  File "<pyshell#44>", line 1, in <module>
    A = P*(1+r/n)**nt
NameError: name 'nt' is not defined
>>> A = P*(1+r/n)**n*t
>>> A
31222.24628759372
>>> A = P*(1+r/n)**(n*t)
>>> from math import sqrt
>>> sqrt(x**2 + y*y)
96.18731725128839
>>> (x,y)
(96, 6)
>>> (x,y)= (19,31)
>>> sqrt(x**2 + y*y)
36.359317925395686
>>> (x**2+y*y)**0.5
36.359317925395686
>>> (x**2+y*y)**1/2
661.0
>>> (x**2+y*y)**(1/2)
36.359317925395686
>>> (x,y,z) = (90,95,85)
>>> x+y+z/3*100
3018.333333333333
>>> x+y+z/(3*100)
185.28333333333333
>>> (x+y+z)/(3*100)
0.9
>>> (x+y+z)/3/100
0.9
>>> (90+95)/2
92.5
>>> (x+y)/2
92.5
>>> (x+y+z-min(x,y,z))
185
>>> (x+y+z-min(x,y,z))/2/100
0.925
>>> 3<2
False
>>> 3 == 3
True
>>> 3 != 2
True
>>> 3 != 3
False
>>> 3 < 4 or 5 < 7
True
>>> 3 < 2 or 5 < 7
True
>>> 3 < 2 or 5 < 3
False
>>> 3 < 2 and 5 < 3
False
>>> not(3<2)
True
>>> 3 >= 2
True
>>> x % 2 == 0
True
>>> x
90
>>> x = 91
>>> x % 2 == 0
False
>>> (x1,y1) = (15,3)
>>> (x2,y2) = (10,5)
>>> (x1*x1+y1*y1)**0.5 < (x2*x2+y2*y2)**0.5
False
>>> (x1*x1+y1*y1) < (x2*x2+y2*y2)
False
>>> not( (x1*x1+y1*y1) < (x2*x2+y2*y2) )
True
>>> (x1*x1+y1*y1) >= (x2*x2+y2*y2)
True
>>> x = 3
>>> y = -3
>>> x == abs(y)
True
>>> x == y or x == -y
True
>>> x = -3
>>> x == y or x == -y
True
>>> x == y or x == -y and x >= 0
True
>>> True or False and False
True
>>> (True or False) and False
False
>>> (x == y or x == -y) and x >= 0
False
>>> s = 'hello'
>>> t = 'world'
>>> s+t
'helloworld'
>>> s+' ' + t
'hello world'
>>> 'hel'+'lo' = 'hello'
SyntaxError: can't assign to operator
>>> 'hel'+'lo' == 'hello'
True
>>> 'one' < 'two'
True
>>> 'ten' < 'two'
True
>>> 3*'hello'
'hellohellohello'
>>> len(3*'hello')
15
>>> len(10000*'hello')
50000
>>> s[0]
'h'
>>> s[1]
'e'
>>> s[3]
'l'
>>> s[5]
Traceback (most recent call last):
  File "<pyshell#109>", line 1, in <module>
    s[5]
IndexError: string index out of range
>>> s[4]
'o'
>>> s[len(s)]
Traceback (most recent call last):
  File "<pyshell#111>", line 1, in <module>
    s[len(s)]
IndexError: string index out of range
>>> s[len(s)-1]
'o'
>>> s[-1]
'o'
>>> s = 'sdlkfjsldkfjslkdfjsdlkf'
>>> s[len(s)-1]
'f'
>>> s[-1]
'f'
>>> 
