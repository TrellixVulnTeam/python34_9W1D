def alt(s,t):
    if (len(s) != len(t)) or s == "":
        return
    if t[1:] != "":
        return s[0] + t[0] + alt(s[1:], t[1:])
    
    return s + t

import os

def check(name, words):
    'check whether word occurs in file name'
    output = []
    try:
        infile = open(name, 'r')
        s = infile.read()
        infile.close()
       

        for word in words:
            if word in s:
                output.append(word)
                
        return output

    
    except: #if file cannot be opened, or file format cannot be read
        return output

def clean(array):
    output = ''
    for i in range(0, len(array)):
        output += str(array[i])
        if i != len(array)-1:
            output += ', '
    return(output)            

def scan(fname, words):
    'scan folders within fname recursively, looking for word'
    print('Scanning: {}'.format(fname))
    for name in os.listdir(fname):
        subname = os.path.join(fname, name)
        if os.path.isfile(subname):
            
            array = check(subname, words)
            if array:
                print('In {} found {}.'.format(subname, clean(array)))
                
        elif os.path.isdir(subname):
            scan(subname, words)
        else:
            pass


def space_h(fname):
    'count number of files in fname'
    
    filesz = 0
    for name in os.listdir(fname):#name of files in path
        subname = os.path.join(fname, name)#makes new path with name of file
        if os.path.isfile(subname):
            filesz += os.path.getsize(subname)
        elif os.path.isdir(subname):
            filesz += space_h(subname)
        else:
            pass
    return filesz

def space(fname):
    size = space_h(fname)// 1000000
    print('{} takes {}MB'.format(fname,str(size)))

def depth_h(fname):
    'count number of files in fname'

    dirctr = 0
    
    for name in os.listdir(fname):
        subname = os.path.join(fname, name)
        if os.path.isdir(subname):
            level = depth_h(subname) #store level of child
            if level > dirctr: #if new child path is greater than previous depth
                dirctr = level #set depth count to child's depth count
    return dirctr + 1 #root to childs depth

def depth(fname):
    print(str(depth_h(fname)))

#prints depth count and file path
def path_h(fname):
    'count number of files in fname'

    dirctr = 0
    path = fname #base case is path given
    for name in os.listdir(fname):
        subname = os.path.join(fname, name)
        if os.path.isdir(subname):
            level, tempPath = path_h(subname) #store level of child and child path
            if level > dirctr: #if new child path is greater than previous depth
                dirctr = level #set depth count to child's depth count
                path = tempPath #set path to child path
    return (dirctr + 1, path) #root to childs depth and path of child

def path(fname):
    print(str(path_h(fname)))  #print depth and path  
    
    
            

    
