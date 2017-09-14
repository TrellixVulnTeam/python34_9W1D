from random import randrange

#for initial testing, harcode secret:
#secret = 7 #random
secret = randrange(1,11)

guess = eval(input('Please guess a number: '))

if guess == secret:
    print('You won')
else:
    print('You lost')
    print('The number was ' + str(secret))
print('Game Over')
