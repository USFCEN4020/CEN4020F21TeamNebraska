from package import dbRead as rd
from package import dbWrite as wr
from package import userIO as io
from package import friend as fd
from package.job import postJob
from package import tier as tr
from package import message as ms
from package import notify as nt
from datetime import datetime as dt

mainTerm = 20 
isLoggedIn = 0
currentLan = 1
languageDict = {1: 'English',
                2: 'Spanish'
                }


def logIn(db):
    userName = input('Enter Account Name: ')
    userPassword = input('Enter Password: ')
    isLoggedIn = rd.loginUser(db, userName, userPassword)
    if (isLoggedIn == 1):
        return (1, userName)
    else:
        return (0, "")


def createAccount(db):
    userName = input('Enter an Account Name: ')
    userPassword = input('Enter a Password: ')
    firstName = input('Enter your first name: ')
    lastName = input('Enter your last name: ')
    print("Membership Plans:")
    tier = tr.chooseMembership()
    setLanguage = 1
    tier = tier.lower() #converts to lowercase
    isLoggedIn = wr.insertUser(db, userName, userPassword, firstName, lastName, setLanguage, tier, dt.now())
    if (isLoggedIn == 1):
        return (1, userName)
    else:
        return (0, "")


# learn skills
def learn_skills():
    return 'Marketing\nSales\nEngineering\nWeb Design\nNursing'


def accountOptions(db, loginInfo):
    x = 0
    # because this
    returnable = loginInfo
    while x != 4:
        print("Account Options:")
        # if currently logged in, print the current account info
        if (loginInfo[0] == 1):
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
        if (x == 1):
            returnable = logIn(db)
        elif (x == 2):
            returnable = createAccount(db)
        elif (x == 3):
            if (returnable[0] == 0):
                print("\nYou are already logged out.\n")
            else:
                print("\nYou are now logged out.\n")
            returnable = (0, "")
        elif (x == 4):
            print("Returning.")
            return returnable
        else:
            print("Please enter a valid option.")
            continue
    return returnable


def about():
    print(
        "In College: Welcome to In College, the world's largest college student network with many users in many countries and territories worldwide.")
    return


# Week 3: Done
def general(db, loginInfo):
    x = 0
    # Since general has access to accountOptions, our login status can change. We will return our login state
    returnable = loginInfo
    while x != 8:
        print(io.loadTextFile("General"))
        option = input("Choose from available options or enter 8 to return: ")
        try:
            x = int(option)
        except ValueError:
            print("\n\nERROR: Please enter a valid numeric input.\n\n")
            x = -1
            continue
        if (x == 1):
            # Log In / Log Out / Create Account
            returnable = accountOptions(db, returnable)
            continue
        elif (x == 2):
            # Help Center
            print("We are here to help.")
            continue
        elif (x == 3):
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


# User Profile
def updateTitle(db, username):
    profile = rd.getUserProfile(db, username)
    try:
        entries = profile[0][1]
    except IndexError:
        entries = 1

    if entries == "1":
        profiletitle = input("Please enter a title for your profile\n")
        wr.insertUserTitle(db, username, profiletitle)
    else:
        profiletitle = "delete"
        while profiletitle == "delete":
            print(f"Your saved entry: \ntitle: {entries}")
            profiletitle = input("Please enter more to add into your profile\n or enter delete to delete old title:\n")
            if profiletitle == "delete":
                entries = ""
            else:
                entries += " " + profiletitle
                wr.insertUserTitle(db, username, entries)


def updateMajor(db, username):
    profile = rd.getUserProfile(db, username)
    try:
        entries = profile[0][2]
    except IndexError:
        entries = 1

    if entries == "1":
        major = input("Please enter a major for your profile\n")
        new_str = io.capitalize_First_Letter_Of_Every_Word(major)
        wr.insertUserMajor(db, username, new_str)
    else:
        major = "delete"
        while major == "delete":
            print(f"Your saved entry: \nMajor: {entries}")
            major = input("Please enter more to add into your profile\n or enter delete to delete old Major:\n")
            if major == "delete":
                entries = ""
            else:
                entries += " " + major
                new_str = io.capitalize_First_Letter_Of_Every_Word(entries)
                wr.insertUserMajor(db, username, new_str)


def updateSchoolName(db, username):
    profile = rd.getUserProfile(db, username)
    try:
        entries = profile[0][3]
    except IndexError:
        entries = 1

    if entries == "1":
        schoolname = input("Please enter your school's name\n")
        new_str = io.capitalize_First_Letter_Of_Every_Word(schoolname)
        wr.insertUserSchoolName(db, username, new_str)
    else:
        schoolname = "delete"
        while schoolname == "delete":
            print(f"Your saved entry: \nSchool Name: {entries}")
            schoolname = input("Please enter more to add into your profile\n"
                               "or enter delete to delete old School Name:\n")
            if schoolname == "delete":
                entries = ""
            else:
                entries += " " + schoolname
                new_str = io.capitalize_First_Letter_Of_Every_Word(entries)
                wr.insertUserSchoolName(db, username, new_str)


def updateBio(db, username):
    profile = rd.getUserProfile(db, username)
    try:
        entries = profile[0][4]
    except IndexError:
        entries = 1

    if entries == "1":
        bio = input("Please enter a bio for your profile\n")
        wr.insertUserBio(db, username, bio)
    else:
        bio = "delete"
        while bio == "delete":
            print(f"Your saved entry: \nBio: {entries}")
            bio = input("Please enter more to add into your profile\n"
                        "or enter delete to delete old bio:\n")
            if bio == "delete":
                entries = ""
            else:
                entries += " " + bio
                wr.insertUserBio(db, username, entries)


def updateExperience(db, username, counts=3):
    print('Employment status')
    profile = rd.getUserProfile(db, username)
    entries = [list(entry) for entry in profile[1]]

    dataname = ["userName", "employer", "start date", "end date", "job's location", "description of your job duties"]
    if len(entries) == 0:
        counts = 0
    else:
        print(f"You have {len(entries)} work experience")
        counts = int(input(f"Enter 1 to {len(entries)} to choose edit or enter 0 "
                           f"to add more Education experience "))

    entries.append([username, '1', '1', '1', '1', '1'])

    if counts >= len(entries):
        counts = 0

    for index, entryy in enumerate(entries[counts - 1]):
        if index != 0 and index != 6:
            if entryy == "1":
                entries[counts - 1][index] = input(f"Please enter a {dataname[index]} for your profile\n")
            else:
                entry = "delete"
                while entry == "delete":
                    print(f"Your saved entry: \n{dataname[index]}: {entries[counts - 1][index]}")
                    entry = input(f"Please enter more to add into your profile\n"
                                  f"or enter delete to delete old {dataname[index]}:\n")
                    if entry == "delete":
                        entries[counts - 1][index] = ""
                    else:
                        entries[counts - 1][index] += " " + entry

    wr.insertUserExperience(db, username, entries[counts - 1][1], entries[counts - 1][2], entries[counts - 1][3],
                            entries[counts - 1][4], entries[counts - 1][5], counts)


def updateEducation(db, username):
    print("Education information")
    profile = rd.getUserProfile(db, username)
    entries = [list(entry) for entry in profile[2]]

    dataname = ["userName", "schoolname", "degree", "years attended"]
    if len(entries) == 0:
        counts = 0
    else:
        print(f"You have {len(entries)} Education experience")
        counts = int(input(f"Enter 1 to {len(entries)} to choose edit or enter 0 "
                           f"to add more Education experience "))

    entries.append([username, '1', '1', '1'])

    for index, entryy in enumerate(entries[counts - 1]):
        if index != 0 and index != 4:
            if entryy == "1":
                entries[counts - 1][index] = input(f"Please enter a {dataname[index]} for your profile\n")
            else:
                entry = "delete"
                while entry == "delete":
                    print(f"Your saved entry: \n{dataname[index]}: {entries[counts - 1][index]}")
                    entry = input(f"Please enter more to add into your profile\n"
                                  f"or enter delete to delete old {dataname[index]}:\n")
                    if entry == "delete":
                        entries[counts - 1][index] = ""
                    else:
                        entries[counts - 1][index] += " " + entry

    wr.insertUserEducation(db, username, entries[counts - 1][1], entries[counts - 1][2], entries[counts - 1][3])

def job(db, loginInfo):
    x = 0
    # Since general has access to accountOptions, our login status can change. We will return our login state
    returnable = loginInfo
    while x != 2:

        print(io.loadTextFile("job"))

        option = input("Choose following option or enter 2 to return: ")
        try:
            x = int(option)
        except ValueError:
            print("\n\nERROR: Please enter a valid numeric input.\n\n")
            x = -1
            continue
        if (x == 1):
            #postJob
            postJob(db, loginInfo[1])
            continue 
        elif (x == 2):
            print("Returning.")
        else:
            print("Please choose a valid option.")
    return returnable

def updateUserProfile(db, loginInfo):
    x = 0
    # Since general has access to accountOptions, our login status can change. We will return our login state
    returnable = loginInfo
    while x != 7:

        print(io.loadTextFile("UserProfile"))

        option = input("Choose which section of your profile you would like to update or enter 7 to return: ")
        try:
            x = int(option)
        except ValueError:
            print("\n\nERROR: Please enter a valid numeric input.\n\n")
            x = -1
            continue
        if (x == 1):
            # title
            # returnable = accountOptions(db, returnable)
            updateTitle(db, loginInfo[1])
            continue
        elif (x == 2):
            # Major
            updateMajor(db, loginInfo[1])
            continue
        elif (x == 3):
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


def searchProfile(db):
    print("Please enter the First name of person you would like to search")
    firstname = input("or press enter to return: ")

    if firstname == "":
        return
    else:
        lastname = input("Please enter the last name: ")
        username = rd.nameToUserName(db, firstname, lastname)
        if username is None:
            print(f"User {firstname} {lastname} is not exist")
            input("Please press enter to continue ")
            return
        userprofile = rd.getUserProfile(db, username)
        if userprofile is None:
            print(f"User {firstname} {lastname}'s profile is not registered")
        elif userprofile[-1] is None:
            print(f"User {firstname} {lastname}'s profile is not completed")
        else:
            print(f"User {firstname} {lastname}'s profile:")
            dataname = [['username', 'title', 'major', 'schoolname', 'bio'],
                        ['Work Experience', 'employer', 'startdate', 'enddate', 'location', 'description'],
                        ['Education Experience', 'schoolname', 'degree', 'years_attended']]
            for index, each in enumerate(userprofile):
                print()
                for index_2, profile in enumerate(each):
                    if index != 0:
                        print()
                        print(f"User {dataname[index][0]} {index_2 + 1}:")
                        for index_3, entry in enumerate(profile):
                            if index_3 != 0 and index_3 != len(profile) -1:
                                print(f"{dataname[index][index_3]}: {entry}")
                    else:
                        print(f"{dataname[index][index_2]}: {profile}")
            
        input('Press Enter to continue')


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
                print(f"{selected[i]} status: {status[current[i + 1]]}")
            option = input('Choose from available options to toggle or enter 4 to return: ')
            try:
                x = int(option)
            except ValueError:
                print("\n\nERROR: Please enter a valid numeric input.\n\n")
                x = -1
                continue
            if x in [1, 2, 3]:
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
            # notifications
            print("Checking to see if you have any new friend requests!")
            fd.pendingRequests(db, userName)
            print('\n')
            print("Checking for new messages!")
            nt.getNewMessages(db, userName)
            print('\n')


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
            print(io.loadTextFile("MainMenu"))

        else:
            print('----- Currently logged in as', userName, '-----')
            print(f"Current language is {languageDict[currentLan]}")
            print()
            print(io.loadTextFile("MainMenu"))

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
                print(returned)
            else:
                print("User must be logged in")
                input("please press enter to continue")

            continue

        elif (x == 6):
            #Search Profile/Send request
            fd.connectFriend(db, isLoggedIn, userName)
            continue

        elif (x == 7):
            # friends
            if (not(isLoggedIn)):
                print("You must be logged in to use show my network")
                continue
            no_friends = fd.myFriends(db, userName)
            if (no_friends == 2):
                continue
            else:
                choice = input("If you would like to view a friends profile input 1, and if you would like to disconnect from someone input 2: ")
                choice = int(choice)
                if (choice == 1):
                    toView = input("Enter the username of the user profile you would like to view: ")
                    fd.viewProfile(db, toView)
                   
                elif (choice == 2):
                    toDelete = input("Enter the username of the user you want to disconnect with: ")
                    fd.deleteFriend(db, userName, toDelete)
                else:
                    print("\ninvalid input, Returning")
                    continue
        elif (x == 8): 
           #Job Search/Internship
             
            if isLoggedIn:
                returned = job(db, (isLoggedIn, userName))
                isLoggedIn = returned[0]
                userName = returned[1]
                print(returned)
            else:
                print("User must be logged in")
                input("please press enter to continue")
            continue

        elif (x == 9):
            #messaging
            if isLoggedIn:
                # Get user Tier
                tier = tr.getTier(db, userName)
                choiceMsg = input('Do you want to read, reply, or send message? Press 1, 2, or 3 accordingly (Other '
                                  'key to skip): ')
                if choiceMsg == '1':
                    readMsg = input('Do you want to read unread messages? Press Y to proceed.')
                    if (readMsg == 'Y'):
                        nt.readMessage(db, userName)
                    print('\n')
                if choiceMsg == '2':
                    replyMsg = input('Do you want to reply to messages? Press Y to proceed')
                    if (replyMsg == 'Y'):
                        nt.replyMessage(db, userName)
                    print('Returning to Main Menu.')
                    print('\n')
                if choiceMsg == '3':
                    print("here")
                    # if 'Standard' tier
                    if (tier == 'standard') :
                        # send message to friends
                        ms.connectUsertoMessage(db, isLoggedIn, userName)
                        print('\n')
                    # if 'plus' tier
                    elif tier == 'plus':
                        # fetch list of all users
                        allUsers = rd.fetchAllUsers(db)
                        for user in allUsers :
                            print(user)
                            print('\n')
                        selectedUser = input('Enter username from user list that you want to send a message to: ')
                        # send message to selected user
                        ms.sendMessage(db, userName, selectedUser, 'plus')
                        print('\n')
            else:
                print("User must be logged in")
                input("please press enter to continue")
            continue
        elif (x == 10):
            # copyright notice
            continue

        elif (x == 11):
            # About
            about()
            continue

        elif (x == 12):
            # Accessibility
            continue
        
        elif (x == 13):
            # User Agreement
            continue
        
        elif (x == 14):
            # Privacy
            fileName = "resources\PrivacyPolicy.txt"
            openFile(fileName)
            guestControl(db, (isLoggedIn, userName))
            continue
        
        elif (x == 15):
            # Cookie Policy
            fileName = "resources\CookiesPolicy.txt"
            openFile(fileName)
            continue
        
        elif (x == 16):
            # Copyright Policy
            fileName = "resources\CopyRightPolicy.txt"
            openFile(fileName)
            continue
        
        elif (x == 17):
            # Brand Policy
            continue
        
        elif (x == 18):
            # Guest Controls
            guestControl(db, (isLoggedIn, userName))
            continue
        
        elif (x == 19):
            # Language
            currentLan = language(db, (isLoggedIn, userName))
            continue

               
        elif (option == str(mainTerm)):
            x = mainTerm
            print("Exit!")
            # this is will exit the program
          
        else:
            print("Invalid input. Please try again.\n")
    
    return userName



def openFile(fileName):
    f = open(fileName, encoding="ISO-8859-1")
    text = f.read()
    f.close()
    print(text)
