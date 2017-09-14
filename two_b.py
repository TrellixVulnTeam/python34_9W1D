color =["red", "green", "purple", "orange", "blue", "yellow"]

pick = input("What is your favorite color ? ")

if pick in color:

    # Storing the rank of the color picked

    rank = color.index(pick) + 1

    # Check if the color is in your list

    if rank == 1:
        
        print("That is my favorite color.")
        
    elif rank == 2:
        print("That is my 2nd favorite color.")

    elif rank == 3:
        print("That is my 3rd favorite color.")

    elif rank > 3:
        print("That is my "+str(rank) +"th favorite color.")
        
else:    
    print("I do not care too much for that color.")
