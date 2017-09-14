import os

def count(fname):
    'count number of files in fname'

    #print('Scanning: {}'.format(fname))
    filectr = 0
    for name in os.listdir(fname):
        subname = os.path.join(fname, name)
        if os.path.isfile(subname):
            filectr += 1
        elif os.path.isdir(subname):
            filectr += count(subname)
        else:
            pass
    return filectr
    
