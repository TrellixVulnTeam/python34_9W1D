def spaces(s):
    scount = 0
    if s[0:] != '':    
        if s[0:] == '':
            scount += 1
            spaces(s[1:])
    return scount

def grades():
    gradedict = {}

    while(True):
        sname = input('Student: ')
        

        if sname == '':
            for key in gradedict:
                print('Student ' + key + ' got a '+ gradedict[key])
            return

        else:
            sgrade = input('Grade: ')
            gradedict[sname] = sgrade
