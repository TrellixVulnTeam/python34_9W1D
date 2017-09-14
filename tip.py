total = eval(input('Please enter total: '))
tip = eval(input('Please enter tip: '))

#original solution
#   if tip/total > 20/100:
#not as good, since it involves division by user-enetered variable (could be 0)
if tip > 0.2*total:
    print('Good tip')
else:
    print('Bad tip')
    



