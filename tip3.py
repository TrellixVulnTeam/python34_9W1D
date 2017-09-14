total = eval(input('Please enter total: '))
tip = eval(input('Please enter tip: '))

#clearer solution using elif

if tip > 0.2*total: # >= 20%
    print('Generous tip')
elif tip > 0.1*total: # between 10% and 20%
    print('Good tip')
else: # <= 10%
    print('Bad tip')
    



