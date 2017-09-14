import os

def check(name, word):
    'check whether word occurs in file name'
    try:
        infile = open(name, 'r')
        s = infile.read()
        infile.close()
        return (word in s)
    except: #if file cannot be opened, or file format cannot be read
        return False

def scan(fname, word):
    'scan folders within fname recursively, looking for word'
    print('Scanning: {}'.format(fname))
    for name in os.listdir(fname):
        subname = os.path.join(fname, name)
        if os.path.isfile(subname):
            if check(subname, word):
                print('Found in {}.'.format(subname))
        elif os.path.isdir(subname):
            scan(subname, word)
        else:
            pass

    
