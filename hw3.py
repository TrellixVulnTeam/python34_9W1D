#2 a.
#new function declaration

def password_check(oldpassword, newpassword):

    if newpassword != oldpassword:

        if len(newpassword) >= 8:

            if newpassword.isalpha()== False:

                return True
            
    return False

#2 b.
# new function declaration

def standing(hours):

    if (hours >= 0):

         lst = ["freshman", "sophmore", "junior", "senior"]

         index = int(min(hours / 48, 3))

         return (lst[index])
         
    else:
         return ("invalid input")

#3
# new function declaration

def stats(name):
    
#variables
    numOfChars = 0
    
#parallel arrays
    letters= ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o","p","q","r","s", "t", "u","v","w","x","y","z"]
    num = [0] * 26

    infile = open(name, 'r')

    content = infile.read()
    
    infile.close()
    
    pointer = 0
    
#process input file
    while (pointer < len(content)):
        
#convert file into lower case letters
        c = (content[pointer]).lower()
        
        if c in letters:
            position = letters.index(c)
            num[position] = num[position] +1
            numOfChars = numOfChars+1
            
#iteration to next character            
        pointer=pointer+1
        
#process output
    counter = 0
    while counter < len(letters):
        print('Letter ' + letters[counter] + ' has a frequency of ' + '{:3.1f}'.format(num[counter] / numOfChars * 100)+ '%')
        counter = counter + 1

#4
#new function declaration
        

def directions(name,logname):

#parallel arrays
    compass= ['north', 'south', 'west', 'east']
    num = [0] * 4

    infile = open(name, 'r')

    content = infile.read()
    infile.close()
    
    pointer = 0
    words=content.split()
    
    outstring = ''

#read each word at a time    
    while (pointer < len(words)):
#convert each word to lowercase
        w = (words[pointer]).lower()

#check if word is north, south, west, or east        
        if w in compass:
            position = compass.index(w)
            num[position] = num[position] +1
            
#iteration to next word        
        pointer=pointer+1

    counter = 0
    
    while counter < len(compass):
        outstring= outstring + (str(compass[counter]) + ' occurs ' + str(num[counter]) + ' times.\n')
        counter = counter + 1

#write to output file
    outfile=open(logname,'w')
    outfile.write(outstring)
    outfile.close()
    
        
            
        
