
#new function declaration

def password_check(oldpassword, newpassword):

    if newpassword != oldpassword:

        if len(newpassword) >= 8:

            if newpassword.isalpha()== False:

                return True
            
    return False



            
        
