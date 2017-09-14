def check_pwd(password):

    for index in range(0, len(password)-2):
        if password[index].isalpha() and password[index+1].isalpha() or \
	password[index].isnumeric() and password[index+1].isnumeric():
            return False
    return True

def secret(message):
    if len(message) > 0:
        secret = message[0]

        for i in range(1, len(message) - 2):  #processing 2 chars at once.

            if message[i] == "\n":
                secret += message[i+1]
        return(secret)
        #print(secret)
            
    else:
        print("Invalid message.")

def drop(lst,k):

    for i in range(0,k):
        lst.remove(min(lst))
        
    return (sum(lst)/len(lst))/100


def score(fname, sname, homework):
    #read the file into records, one row per element in the list
    infile = open(fname, 'r')
    records = infile.readlines()
    infile.close()

    #Store the first row (column names) into a temp list lst
    lst=records[0].split(",")

    #Check if input is in lst
    if homework.upper() in lst:
        col=lst.index(homework.upper())
    #If not, check if (input+\n) is in lst
    elif homework.upper()+"\n" in lst:
        col=lst.index(homework.upper()+"\n")
    #else, not in lst
    else:
        print("No such column.")
        return

    #col = hw grade
    #find student one row of data at a time
    for record in records[2:]:
        #Create a temp list of this student's hw grades
        lst = record.split(',')
        #The student's last name is in the first column, save it to lname
        lname = lst[0]
        #His score (assuming this is the correct student) is in the col column (from above)
        score=lst[col]

        #Check if this student is the one we want
        if lname == sname.upper():
            #If so, print his score
            print(score)
            return
    print('{} not found.'.format(sname))

#print standard deviation
def stdev(lst):
    #find the mean
    mean = sum(lst) / len(lst)

    #find the sum of the difference at each element
    amount = 0
    for e in lst:
        amount += (e - mean) ** 2

    #take the square root of the sum / N
    stddev = (amount / len(lst)) ** .5

    #return the standard deviation
    return stddev
