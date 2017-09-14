#more comprehensive game example

from random import randrange

#game parameters (as global variables)
num_bombs = 2

#symbols
block_s = '\u2588'
empty_s = ' '
bomb_s = '\u1F4A'
treasure_s = '\u263A'

#display nxn grid, with fields in openFields opened
#of these, the ones in bombs will display a bomb, the one in
#treasure a treasure
def draw_grid(n, openFields, bombs, treasure):
    for i in range(n):
        for j in range(n):
            if (i,j) in openFields:
                if (i,j) in bombs:
                    print(bomb_s, end = '')
                elif (i,j) in treasure:
                    print(treasure_s, end = '')
                else:
                    print(empty_s, end = '')
            else:
                print(block_s, end = '')
        print()

def pick_point(n):
    'return a random point of the nxn grid'
    i = randrange(n)
    j = randrange(n)
    return (i,j)

def game(n):
    'play game'
    
    #initialization
    openFields = []
    bombs = []
    #place bombs
    for i in range(num_bombs):
        bombs.append(pick_point(n))
    #place treasure at new location
    p = pick_point(n)
    while p in bombs:
        p = pick_point(n)
    treasure = [p]

    while(True):
        #display state
        draw_grid(n, openFields, bombs, treasure)
        #user input
        s = input('Open: ')
        (i,j) = eval(s)
        openFields += [(i,j)]
        #react
        if (i,j) in bombs:
            draw_grid(n, openFields, bombs, treasure)
            print('you failed')
            return
        elif (i,j) in treasure:
            draw_grid(n, openFields, bombs, treasure)
            print('you won')
            return
            

    
