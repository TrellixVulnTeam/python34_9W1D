def words(name):
    try:
        'count how many words file name contains'
        infile = open(name, 'r')
        s = infile.read()
        infile.close()

        lst = s.split()
        print('The file contains {} words.'.format(len(lst)))

    except FileNotFoundError:
        print("Could not open file '{}'.".format(name))

def triangle(n):
    if n > 0:
        print(n * '*')
        triangle(n-1)


def prompt():
   password = input('Enter password: ')
   
   if password != '':
    return password
       
   else:
    return prompt()

           
def space(word):
    if len(word) != 0:
        rem_word = space(word[1:])
        if rem_word is not None:
            return str(word[0])+ ' ' + str(rem_word)
        else:
            return str(word)


def juggle(n):
    print(str(n))
    if(n != 1):
        if(n % 2 == 0):
            n = int(n**0.5)
        else:
            n = int(n**1.5)
        juggle(n)    
       
