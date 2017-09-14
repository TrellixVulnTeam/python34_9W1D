from random import randrange

#secret = 7 #random
secret = randrange(1,11)

guess = eval(input('Please guess a number: '))

if secret > guess:
    print('You lost')
    print('The secret number is larger')
elif guess == secret:
    print('You won')
else:
    print('You lost')
    print('The secret number is smaller')
## following code was for debugging, to see whether output was correct
#print(secret)
print('Game Over')
