#print('2**2 = 4')
#print('2**3 = 8')

lower = eval(input('Please enter a lower bound: '))
upper = eval(input('Please enter a upper bound: '))

for i in range(lower,upper+1):
    message = '2**{} == {}'.format(i,2**i)
    print(message)
