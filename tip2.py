total = eval(input('Please enter total: '))
tip = eval(input('Please enter tip: '))

if tip > 0.2*total:
    print('Generous tip')
else: #tip <= 20%
    if tip > 0.1*total: #so tip >10% but < 20%
        print('Good tip')
    else: #tip <= 10%
        print('Bad tip')
    



