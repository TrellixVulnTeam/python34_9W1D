def check_pwd(password):

    for index in range(0, len(password)-2):
        if password[index].isalpha() and password[index+1].isalpha() or \
	password[index].isnumeric() and password[index+1].isnumeric():
            return False
    return True

def secret1(message):
    if len(message) > 0:
        secret = message[0]
        pos=0
        for i in range(1, len(message) - 1):
            i=pos+1
            subpos=message[i:].find("\n")
            i+=subpos
            if subpos==-1 or i == len(message)-1:
                break
            secret += message[i+1]
            pos=i
        print(secret)
            
    else:
        print("Invalid message.")

def secret(message):
    if len(message) > 0:
        secret = message[0]

        for i in range(1, len(message) - 2):

            if message[i] == "\n":
                secret += message[i+1]

        print(secret)
            
    else:
        print("Invalid message.")

    
