def SSN():
    ssndict = {}

    while(True):
        sname = input('Name: ')

        # if no name entered print list and end.
        if sname == '':

            for key in ssndict:
                print(key + ' has SSN ' + ssndict[key])
            return
        
        elif sname not in ssndict:
            ssn = input('SSN for '+ sname + ': ')
            ssndict[sname] = ssn

        else:
            option = input(sname + ' has SSN '+ ssndict[sname] + '.  Update (y or n) ? ')
            if option.lower() == 'y':
                ssn = input('New SSN for '+ sname + ': ')
                ssndict[sname] = ssn
            
def read_ticker():
    infile = open('tickers.csv', 'r')
    s = infile.readlines()
    infile.close()

    tdict = {}
    for line in s: # for each line in s
        fileinput = line.split(',') # split line and store as array of strings.
        stringv = fileinput[1] #store array at position 1 a string for later use.
        stringk = fileinput[0]
        tdict[stringk] = stringv[0:-1] #create dictionary entry using key and value minus the new line.
    return(tdict)
    
def ticker():
    tdict = read_ticker()

    while(True):
        sname = input('Please enter a ticker symbol: ').upper()

        # if no name found end.
        if sname == '':
            return
        
        elif sname not in tdict:
            print('Ticker symbol \"' + sname + '\" not found.')

        else:
            print('Company \"' + tdict[sname] + '\" has ticker symbol ' + sname + '.')

def index(fname, words):

    infile = open(fname, 'r')
    lines = infile.readlines()
    infile.close()

    location = {}
    lineNum = 0

    for line in lines: #for each line in array lines.
        lineNum += 1 #increment line number.

        for w in words:#for each word in array of words.
            if w in line: # if word in line.
                key = w #current word set to key.
                
                if key in location: #if word already in dictonary.
                    (location[key]).append(lineNum)#add line number to array in dictionary.
                    
                else: #word not in dictionary
                    value = [lineNum]#creating new array with value of lineNum and storing into value.
                    location[key] = value #placing lineNum value in dictionary.

    for key in location:
       print(key + '\t' + plist(location[key]))
       
       


def plist(array):
    output = ''
    for i in range(0, len(array)):
        output += str(array[i])
        if i != len(array)-1:
            output += ', '
    return(output)            
            

       
       
                
        
    

    
