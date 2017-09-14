#3b.
#prompt for lower and upper bound numbers
lower = int(input("Please enter a lower bound: "))

upper = int(input("Please enter an upper bound: "))


#for each number in the range
for exp in range(lower, upper + 1):

#print 2 ** exp = answer

    print("2**" + str(exp) + " = " + str(2**exp))
