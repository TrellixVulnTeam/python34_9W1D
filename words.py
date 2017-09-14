#various file i/o functions

def words(name):
    'count how many words file name contains'
    infile = open(name, 'r')
    s = infile.read()
    infile.close()

    lst = s.split()
    print('The file contains {} words.'.format(len(lst)))

def lines(name):
    'count how many lines file name contains'
    infile = open(name, 'r')
    s = infile.read()
    infile.close()

    lst = s.split('\n')
    print('The file contains {} lines.'.format(len(lst)))

#illustrate readlines versus read
def lines(name):
    'count how may lines file name contains'
    infile = open(name, 'r')
    lst = infile.readlines()
    infile.close()

    #lst = s.split('\n')
    print('The file contains {} lines.'.format(len(lst)))

#simple function to replace punctuation with spaces
    #to remove punctuation, replace ' ' with ''
def strip(s):
    'remove punctuation from s'
    p = '.,:;!?'
    for symbol in p:
        #note that strings are immutable, so we need to reassign replace result
        s = s.replace(symbol, ' ')
    return s

def occurs(name, word):
    'how often does word occur in file name'
    infile = open(name, 'r')
    s = infile.read()
    infile.close()

    lst = s.split()
    #print(s, lst)
    s = strip(s)
    lst2 = s.split()
    #print(s, lst2)
    
    #4 different methods for counting, with various degrees of accuracy
    print('The file contains {} occurrences of {}.'.\
          format(s.count(word),word))
    print('The file contains {} occurrences of {}.'.\
          format(s.count(' '+word+' '),word))
    print('The file contains {} occurrences of {}.'.\
          format(lst.count(word),word))
    print('The file contains {} occurrences of {}.'.\
          format(lst2.count(word),word))

from time import strftime

def occurs(name, word):
    'count how often word occurs in name, and log result'
    infile = open(name, 'r')
    s = infile.read()
    infile.close()

    message = 'Request at {}:\n'.format(strftime('%I:%M:%S%p'))
    message += '\tThe file contains {} ' \
            'occurrences of \'{}\'.\n'.\
          format(s.count(word),word)
    #print(message)
  
    outfile = open('analysis_'+ name, 'a')
    outfile.write(message)
    outfile.close()
    
