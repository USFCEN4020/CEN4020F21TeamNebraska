import sqlite3
from package import dbRead as rd
from package import dbWrite as wr
from package import userIO as io

mainTerm = 16
isLoggedIn = 0
currentLan = 1
languageDict = {1: 'English',
                2: 'Spanish'
                }


def connectFriend(db, isLoggedIn):
    fName = input('Enter first name of the friend you wish to connect with: ')
    lName = input('Enter last name of the friend you wish to connect with: ')
    if not isLoggedIn:
        if (rd.find_people(db, fName, lName)):
            print('They are a part of the InCollege system. Please login or sign up to connect with them.')
        else:
            print('They are NOT a part of the InCollege system.')
    else:
        print("Under Construction!")


def logIn(db):
    userName = input('Enter Account Name: ')
    userPassword = input('Enter Password: ')
    isLoggedIn = rd.loginUser(db, userName, userPassword)
    if(isLoggedIn == 1): return (1, userName)
    else: return (0, "")


def createAccount(db):
    userName = input('Enter an Account Name: ')
    userPassword = input('Enter a Password: ')
    firstName = input('Enter your first name: ')
    lastName = input('Enter your last name: ')
    setLanguage = 1
    isLoggedIn = wr.insertUser(db, userName, userPassword, firstName, lastName, setLanguage)
    if (isLoggedIn == 1): return (1, userName)
    else: return (0, "")

# job search
def job_search(db, isLoggedIn, userName):
    y = 0
    if (isLoggedIn == 0):
        print("Please log in to access job search and posting.")
        input("Press enter to return to the main menu.")
        return
    else:
        while (y != 5):
            print("\nWelcome to the jobs tab!\n")
            print("1. Post job")
            command = input("Choose an available option, or enter 5 to exit.")
            y = int(command)
            if (y == 1):
                io.postJob(db, userName)
                print()
            else:
                return

    return


# learn skills
def learn_skills():
    return 'Marketing\nSales\nEngineering\nWeb Design\nNursing'


def accountOptions(db, loginInfo):
    x = 0
    # because this
    returnable = loginInfo
    while x!=4:
        print("Account Options:")
        # if currently logged in, print the current account info
        if(loginInfo[0] == 1):
             print("Currently logged in as", loginInfo[1])
        print(loginInfo[1])

        print(" 1. Log In")
        print(" 2. Create an Account")
        print(" 3. Log Out")
        option = input("Choose from available options or enter 4 to return: ")
        try:
            x = int(option)
        except ValueError:
            print("\n\nERROR: Please enter a valid numeric input.\n\n")
            x = -1
            continue
        if(x == 1):
            returnable = logIn(db)
        elif(x == 2):
            returnable = createAccount(db)
        elif(x == 3):
            if(returnable[0] == 0): print("\nYou are already logged out.\n")
            else: print("\nYou are now logged out.\n")
            returnable = (0, "")
        elif(x == 4):
            print("Returning.")
            return returnable
        else:
            print("Please enter a valid option.")
            continue
    return returnable


def about():
    print("In College: Welcome to In College, the world's largest college student network with many users in many countries and territories worldwide.")
    return


# Week 3: Done
def general(db, loginInfo):
    x = 0
    # Since general has access to accountOptions, our login status can change. We will return our login state
    returnable = loginInfo
    while x != 8:
        print(io.loadTextFile("general"))
        option = input("Choose from available options or enter 8 to return: ")
        try:
            x = int(option)
        except ValueError:
            print("\n\nERROR: Please enter a valid numeric input.\n\n")
            x = -1
            continue
        if(x == 1):
            # Log In / Log Out / Create Account
            returnable = accountOptions(db, returnable)
            continue
        elif(x == 2):
            # Help Center
            print("We are here to help.")
            continue
        elif(x == 3):
            # About
            about()
            continue
        elif (x == 4):
            # Press
            print("In College Pressroom: Stay on top of the latest news, updates, and reports.")
            continue
        elif (x == 5):
            # Blog
            print("Under construction.")
            continue
        elif (x == 6):
            # Careers
            print("Under construction.")
            continue
        elif (x == 7):
            # Developers
            print("Under construction.")
            continue
        elif (x == 8):
            print("Returning.")
        else:
            print("Please choose a valid option.")
    return returnable

#User Profile
def updateTitle(db, username):
    profiletitle = input("Please enter a title for your profile\n")
    wr.insertUserTitle(db, username, profiletitle)

def updateMajor(db, username):
    major = input("Please enter a major for your profile\n")
    new_str = io.capitalize_First_Letter_Of_Every_Word(major)
    print(new_str)
    wr.insertUserMajor(db, username, new_str)   

def updateSchoolName(db, username):
    schoolname = input("Please enter your school's name\n")
    new_str = io.capitalize_First_Letter_Of_Every_Word(schoolname)
    print(new_str)
    wr.insertUserSchoolName(db, username, new_str)

def updateBio(db, username):
    bio = input("Please enter a bio for your profile\n")
    wr.insertUserBio(db, username, bio)

def updateExperience(db, username):
    employer = input("Please enter employer\n")
    startdate = input("Please enter start date\n") 
    enddate = input("Please enter end date\n")
    location = input("Please enter job's location\n")
    description = input("Please enter description of your job duties\n")
    wr.insertUserExperience(db, username, employer, startdate, enddate, location, description)

def updateEducation(db, username):
    print("Education information")
    schoolname = input("Please enter schoolname\n")
    degree = input("Please enter your degree\n")
    total_years_attended = input("Please enter years attended \n")
    wr.insertUserEducation(db, username, schoolname, degree, total_years_attended)

def updateUserProfile(db, loginInfo):
    x = 0
    # Since general has access to accountOptions, our login status can change. We will return our login state
    returnable = loginInfo
    while x != 7:
        
        print(io.loadTextFile("userprofile"))
        
        option = input("Choose which section of your profile you would like to update or enter 7 to return: ")
        try:
            x = int(option)
        except ValueError:
            print("\n\nERROR: Please enter a valid numeric input.\n\n")
            x = -1
            continue
        if(x == 1):
            # title
            # returnable = accountOptions(db, returnable)
            updateTitle(db, loginInfo[1])
            continue
        elif(x == 2):
            # Major
            updateMajor(db, loginInfo[1])
            continue
        elif(x == 3):
            # University Name
            updateSchoolName(db, loginInfo[1])
            continue
        elif (x == 4):
            # Bio
            updateBio(db, loginInfo[1])
            continue
        elif (x == 5):
            # Experience
            updateExperience(db, loginInfo[1])
            continue
        elif (x == 6):
            # Education
            updateEducation(db, loginInfo[1])
            continue
        elif (x == 7):
            print("Returning.")
        else:
            print("Please choose a valid option.")
    return returnable


def language(db, loginInfo):
    x = 1
    if (loginInfo[0] == 0):
        print("Please log in to access job search and posting.")
        input("Press enter to return to the main menu.")
        return
    else:
        currentLan = rd.currentLanguage(db, loginInfo[1])
        while x != len(languageDict) + 1:
            print("Language Setting:")
            print(f'Your current language is {languageDict[currentLan]}')
            print("You can change the language to:")
            for i in languageDict.keys():
                print(f"{i}. {languageDict[i]}")
            option = input(f'Choose from available options or enter {len(languageDict) + 1} to return:')
            try:
                x = int(option)
            except ValueError:
                print("\n\nERROR: Please enter a valid numeric input.\n\n")
                x = -1
                continue

            if x in languageDict:
                print(f"Successfully change the language to {languageDict[x]}")
                wr.changeLanguage(db, loginInfo[1], x)
                break

            elif x != len(languageDict) + 1:
                print('Please enter a valid number')
    input('Press enter to continue')
    return x


def guestControl(db, loginInfo):
    x = 0
    if not loginInfo[0]:
        print('Please login to proceed')
        input("Press enter to continue")
    else:
        print('Guest control settings:')
        selected = ['email', 'sms', 'targetAD']
        while x != 4:
            current = rd.currentPrivacy(db, loginInfo[1])
            status = {1: "ON", 0: "OFF"}
            print('\nYour current setting is:')
            for i in range(3):
                print(f"{selected[i]} status: {status[current[i+1]]}")
            option = input('Choose from available options to toggle or enter 4 to return: ')
            try:
                x = int(option)
            except ValueError:
                print("\n\nERROR: Please enter a valid numeric input.\n\n")
                x = -1
                continue
            if x in [1,2,3]:
                wr.changePrivacy(db, loginInfo[1], x)
                print('Change successfully')
            elif x != 4:
                print('Please enter a valid number')


def mainMenu(db):
    global currentLan
    # User option value
    x = 0
    # User logIn status
    isLoggedIn = 0
    userName = ""
    

    print('Welcome to InCollege!')
    print()

    while x != mainTerm:
        print()

        if isLoggedIn:
            currentLan = rd.currentLanguage(db, userName)
            if currentLan not in languageDict:
                currentLan = 1
                wr.changeLanguage(db, userName, 1)


        if not isLoggedIn:
            currentLan = 1
            print('+-+-+  "I became a quadrillionaire thanks to inCollege!" -Madison +-+-+')
            print(f"Current language is {languageDict[currentLan]}")
            print('0. Watch video about inCollege')
            print()
            print(io.loadTextFile("mainmenu"))

        else:
            print('----- Currently logged in as', userName, '-----')
            print(f"Current language is {languageDict[currentLan]}")
            print()
            print(io.loadTextFile("mainmenu"))

        option = input("Choose from available options: ")
        print()


        try:
            x = int(option)
        except ValueError:
            print("\n\nERROR: Please enter a valid numeric input.\n\n")
            x = -1
            continue

        if (x == 0):
            print()
            print("Video is now playing")
            print()

        elif (x == 1):
            # General
            returned = general(db, (isLoggedIn, userName))
            isLoggedIn = returned[0]
            userName = returned[1]
        
            continue

        elif (x == 2):
            # Browse InCollege
            print("Under construction.")
            continue

        elif (x == 3):
            # Business Solutions
            print("Under construction.")
            continue

        elif (x == 4):
            # Directories
            print("Under construction.")
            continue
        
        elif (x == 5):
            # Create User Profile
            if isLoggedIn:
                returned = updateUserProfile(db, (isLoggedIn, userName))
                isLoggedIn = returned[0]
                userName = returned[1]
            else:
                print("User must be logged in")

            continue
        
        elif (x == 6):
            # A Copyright Notice
            print("Under construction.")
            continue

        elif (x == 7):
            # About
            about()
            continue

        elif (x == 8):
            # Accessibility
            continue
        elif (x == 9):
            # User Agreement
            continue
        elif (x == 10):
            # Privacy
            fileName ="PrivacyPolicy.txt"
            openFile(fileName)
           
            guestControl(db, (isLoggedIn, userName))
            continue
        elif (x == 11):
            # Cookie Policy
            fileName ="CookiesPolicy.txt"
            openFile(fileName)
            continue
        elif (x == 12):
            # Copyright Policy
            fileName ="CopyRightPolicy.txt"
            openFile(fileName)
            continue
        elif (x == 13):
            # Brand Policy
            continue
        elif (x == 14):
            # Guest Controls
            guestControl(db, (isLoggedIn, userName))
            continue
        elif (x == 15):
            # Language
            currentLan = language(db, (isLoggedIn, userName))
            continue
        elif (option == str(mainTerm)):
            x = mainTerm
            print("Exit!")
            # this is will exit the program
        else:
            print("Invalid input. Please try again.\n")


def openFile(fileName):
            f= open(fileName, encoding="ISO-8859-1")
            text = f.read()
            f.close()
            print(text)

          

            