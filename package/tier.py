from package import dbRead as rd
from package import dbWrite as wr
from package import userIO as io
from package import friend as fd
from package.job import postJob



def getTier(db, username):
        db[0].execute('SELECT tier FROM users WHERE username=?', (username,))
        tier = db[0].fetchone()
        return tier[0]


def chooseMembership():#epic 7
    x = 0
    returnable = "standard"
    while x != 3:
        print(io.loadTextFile("MembershipPlans"))
        option = input("Choose from available options or enter 3 to return: ")
        try:
            x = int(option)
        except ValueError:
            print("\n\nERROR: Please enter a valid numeric input.\n\n")
            x = -1
            continue
        if (x == 1):
            
            
            returnable = "standard"
            return returnable
            
        elif (x == 2):
            
           
            returnable = "plus"
            return returnable
        
        elif (x == 3):
            print("Returning.")
        else:
            print("Please choose a valid option.")
    return returnable


    