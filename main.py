#Team Nebraska
#Developers: Premanshu Yadav, Ethan Wuitschick
#Epic 2

# Database used
import sqlite3

# Connection object represents
# the database
conn = sqlite3.connect('users.db')

# Cursor object to perform
# SQL commands
cursor = conn.cursor()

# Create user table
cursor.execute('''CREATE TABLE IF NOT EXISTS users
            (username text, password text, fname text, lname text)''')
cursor.execute('''CREATE TABLE IF NOT EXISTS jobs
            (title text, description text, employer text, location text, salary text)''')

# find people by firstName and lastName
def find_people(fName, lName):
    cursor.execute('SELECT * FROM users WHERE fname=? AND lname=?', (fName, lName))
    check = cursor.fetchone()
    if (check == None): return 0
    else: return 1

# learn skills
def learn_skills():
    return 'Marketing\nSales\nEngineering\nWeb Design\nNursing'

#---------------------- Log In ----------------------#
# Username Validation
def validateUser(username): # username is the Account Name
    valid = True
    count = 0
    t = (username,)

    for i in cursor.execute('SELECT * FROM users WHERE username=?', t):
        count = count + 1

        if count == 0:
            valid = True
        else:
            valid = False
            print("Sorry, your username has already been taken.")

    return valid

# Password Validation
def validatePassword(password):
      
    SpecialSymbol =['$', '@', '#', '%', '!', '%', '^', '&', '*', '(', ')', '-', '_', '+', '=', '`', '~', '[', '{', ']', '}', '|', ';', ':', ',', '<', '.', '>', '/', '?']
    val = True
      
    if len(password) < 8:
        print('Your password needs to have 8 characters at least!')
        val = False
          
    if len(password) > 20:
        print('Your password can not exceed 12 characters!')
        val = False
          
    if not any(char.isdigit() for char in password):
        print('Your password needs to contains at lease one digit!')
        val = False
          
    if not any(char.isupper() for char in password):
        print('Password should have at least one uppercase letter')
        val = False
          
    if not any(char.islower() for char in password):
        print('Your password needs to contains at lease one capital character!')
        val = False
          
    if not any(char in SpecialSymbol for char in password):
        print('Your password need to contain at least one non-alpha character!')
        val = False
    
    return val

# Insert User in Database
def insertUser(username, password, fname, lname):
    # counter to limit 
    # number of accounts
    count = 1
    # count no. of users 
    for i in cursor.execute('SELECT * FROM users'):
        count += 1

    # insert if validated
    if(validatePassword(password) and validateUser(username) and count < 6):
        cursor.execute("INSERT INTO users VALUES (?,?,?,?)",(username,password, fname, lname))
        conn.commit()
        print('User added to database!')
        # 1 => true on success
        return 1
    if(count > 5):
        print("All permitted accounts have been created, please come back later")
        # 0 => false on failure
        return 0

# User logIn
def loginUser(username, password):
    # fetch user
    cursor.execute('SELECT username, password FROM users WHERE username=? AND password=?', (username,password,))
    if(cursor.fetchone()):
        print('You have successfully logged in')
        # 1 => true on success
        return 1
    else:
        print('Incorrect username / password, please try again"')
        # 0 => false on failure
        return 0

def commitJob(title, description, employer, location, salary):
    # counter to limit 
    # number of accounts
    count = 1
    # count no. of users 
    for i in cursor.execute('SELECT * FROM jobs'):
        count += 1
    if (count > 5):
        print("All permitted Jobs Have been created")
        return 1 
    else:
        cursor.execute("INSERT INTO jobs VALUES (?,?,?,?,?)",(title,description, employer, location, salary))
        conn.commit()
        print("Job", title, "posted successfully!")

# Post job function
def postJob():
    print("\nEnter 'cancel' at any time to cancel.\n")
    title = input("Enter job title: ")
    if(title=='cancel'):
        print("Returning to main menu.")
        return
    description = input("Enter job description: ")
    if(description=='cancel'):
        print("Returning to main menu.")
        return
    employer = input("Enter job employer: ")
    if(employer=='cancel'):
        print("Returning to main menu.")
        return
    location = input("Enter job location: ")
    if(location=='cancel'):
        print("Returning to main menu.")
        return
    salary = input("Enter job salary (in USD please): ")
    if(salary=='cancel'):
        print("Returning to main menu.")
        return
    commitJob(title, description, employer, location, salary)
    
# job search 
def job_search(isLoggedIn):
    y = 0
    if(isLoggedIn == 0):
        print("Please log in to access job search and posting.")
        input("Press enter to return to the main menu.")
        return 
    else:
        while(y != 5):
            print("\nWelcome to the jobs tab!\n")
            print("1. Post job")
            command = input("Choose an available option, or enter 5 to exit.")
            y = int(command)
            if(y == 1):
                postJob()
                print()
            else:
                return
    
    return 
#---------------------------------------------------------------#

# User option value
x = 0
# User logIn status
isLoggedIn = 0

print('Welcome to InCollege!')
print()

userName = ""

while x != 6:
    print()

    if not isLoggedIn:
        print('+-+-+  "I became a quadrillionaire thanks to inCollege!" -Madison +-+-+')
        print('0. Watch video about inCollege')
        print()
        print('Account Services:')
        print('1. Login')
        print('2. Create an Account')
        print()
        print('Services Offered:')
        print('3. Find jobs')
        print('4. Find people')
        print('5. Learn a new skill')
        print()
        print('6. Exit')
        print()
        
    else:
        print('----- Currently logged in as', userName, '-----')
        print()
        print('Account Services:')
        print('1. Login (You are already logged in)')
        print('2. Create an Account (You are already logged in)')
        print() 
        print('Services Offered:')
        print('3. Find & Post jobs')
        print('4. Find people')
        print('5. Learn a new skill')
        print()
        print('6. Exit')

    option = input("Choose from available options or enter 6 to exit: ")
    print()

    if(option == '0'):
        print()
        print("Video is now playing")
        print()

    if (option == '1'):
        x = 1
        userName = input('Enter Account Name: ')
        userPassword = input('Enter Password: ')
        isLoggedIn = loginUser(userName, userPassword)

    if (option == '2'):
        x = 2
        userName = input('Enter an Account Name: ')
        userPassword = input('Enter a Password: ')
        firstName = input('Enter your first name: ')
        lastName = input('Enter your last name: ')
        isLoggedIn = insertUser(userName,userPassword,firstName,lastName)
        print()

    if (option == '3'):
        x = 3
        print(job_search(isLoggedIn))
        print()

    if (option == '4'):
        x = 4
        fName = input('Enter first name of the friend you wish to connect with: ')
        lName = input('Enter last name of the friend you wish to connect with: ')
        if not isLoggedIn:
            if(find_people(fName, lName)):
                print('They are a part of the InCollege system. Please login or sign up to connect with them.')
            else: print('They are NOT a part of the InCollege system.')  
        else: print("Under Construction!")
        print()
        

    if (option == '5'):
        x = 5
        print(learn_skills())
        print()

    if (option == '6'):
        x = 6
        print("Exit!")
        #this is will exit the program
