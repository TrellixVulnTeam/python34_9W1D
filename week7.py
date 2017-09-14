#some helper functions for following
def average(lst):
    return sum(lst)/len(lst)

def clean(lst):
    'convert list lst of strings into list of integers'
    intlst = []

    for e in lst:
        intlst.append(eval(e))

    return intlst

#first version, slow, processes records over and over
def avg_score(fname):
    'read fname, and find average score for sname'

    infile = open(fname, 'r')
    records = infile.readlines()
    infile.close()

    sname = input('Name: ')
    while(sname != ''):
        found = False
            lst = record.split(',')
            lname = lst[0]
            scores = clean(lst[1:])
            if lname == sname.upper():
                print('{} has average score {:.2f}'.\
                      format(lname, average(scores)))
                found = True
                break
        if not found:
            print('{} not found.'.format(sname))
        sname = input('Name: ')

#same, but with infinite loop
def avg_score(fname):
    'read fname, and find average score for sname'

    infile = open(fname, 'r')
    records = infile.readlines()
    infile.close()

    
    while(True):
        sname = input('Name: ')
        if sname == '':
            return
        found = False
        for record in records[2:]:
            lst = record.split(',')
            lname = lst[0]
            scores = clean(lst[1:])
            if lname == sname.upper():
                print('{} has average score {:.2f}'.\
                      format(lname, average(scores)))
                found = True
                break
        if not found:
            print('{} not found.'.format(sname))

#faster: using dictionary avgscores to store results
def avg_score(fname):
    'read fname, and find average score for sname'

    infile = open(fname, 'r')
    records = infile.readlines()
    infile.close()

    #process recordsa and store in dictionary
    avgscores = {} # dict()
    for record in records[2:]:
        lst = record.split(',')
        lname = lst[0].upper()
        scores = clean(lst[1:])
        avg = average(scores)
        avgscores[lname] = avg

    #return avgscores

    while(True):
        sname = input('Name: ').upper()
        if sname == '':
            return
        elif sname in avgscores:
            print('{} has average score {:.2f}'.\
                      format(sname, avgscores[sname]))
        else:
            print('{} not found.'.format(sname))


def freq(fname):
    'print frequency of all symbols in file fname'

    infile = open(fname, 'r')
    s = infile.read()
    infile.close()

    ctrs = {}
    for symbol in s:
        if symbol not in ctrs:
            ctrs[symbol] = 1
        else:
            ctrs[symbol] += 1

    n = len(s)
    for symbol in ctrs:
        print('{} has frequency {:.2f}%'.\
              format(symbol, 100*ctrs[symbol]/n))

def freq(fname):
    'print frequency of all symbols in file fname'
    
    infile = open(fname, 'r')
    s = infile.read()
    infile.close()

    ctrs = {}
    for symbol in s:
        if symbol not in ctrs:
            ctrs[symbol] = 1
        else:
            ctrs[symbol] += 1

    n = len(s)
    for (symbol,f) in ctrs.items():
        print('{} has frequency {:.2f}%'.\
              format(symbol, 100*f/n))

#sample dictionary with paris (2-tuples)
        
pb = {('Baggins', 'Frodo'): 1111111,
      ('Beutlin', 'Sam'): 2222222,
      ('Sauton', ''): 6666666,
      ('the Grey', 'Gandalf'): 9999999}

def reverse(d):
    'reverse dictionary'

    d2 = {}
    for key in d:
        value = d[key]
        d2[value] = key
        #print(key,value)
    return d2

def reverse(d):

    d2 = {}
    for (key, value) in d.items():
        d2[value] = key
        #print(key,value)
    return d2

def reverse(d):
    'reverse dictionary, allowing multiple keys'
    d2 = {}
    for (key, value) in d.items():
        if value in d2:
            d2[value].append(key)
        else:
            d2[value] = [key]
        #print(key,value)
    return d2
