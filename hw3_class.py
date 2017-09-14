def password_check(oldpassword, newpassword):
    if newpassword != oldpassword and \
        len(newpassword) >= 8 and \
        newpassword.isalpha()== False:
        return True
    else:
        return False

    
def stats(name):
    infile=open(name,'r')
    s=infile.read()
    infile.close()

    
    for let_code in range(ord('a'), ord('z') + 1):
        letter = chr(let_code)

        firstPart='Letter {} is {:3.2f} in numerical form.'
        secondPart=firstPart.format(letter,let_code)
        print(secondPart)
        print('Letter {} has a frequency of {:.1f}%'.format(letter, 100*(s.count(letter)+s.count(letter.upper()))/len(s)))

def directions(name, logname):
    infile=open(name,'r')
    s=infile.read()
    infile.close()

    directions = ['north', 'east', 'west', 'south']

    message=''

    for direction in directions:
        message +='{} occurs {} times.\n'.\
                 format(direction, s.count(direction))

        outfile=open(logname,'w')
        outfile.write(message)
        outfile.close()


def avgC(name):
    infile=open(name,'r')
    s=infile.read()
    infile.close()

    words = s.split(' ')
    count = 0  #count of characters in file.

    for word in words: # for each word in array.
        
        for c in range(0, len(word)): # for 0 to length of each word
            
            if word[c].isalnum(): #if character is alpha numeric
                count += 1

    wordAverage = count / len(words) #count divided by lenght of words array, the characters per word

    print('The average number of letters per word is: {}'.format(wordAverage))

    
    
