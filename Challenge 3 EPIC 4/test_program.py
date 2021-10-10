#Team Nebraska
#Epic 3

# Database used
import sqlite3

# Connection object represents
# the database
conn = sqlite3.connect('inCollege1.db')

# Cursor object to perform
# SQL commands
cursor = conn.cursor()

db = (cursor, conn)

# Create user table
cursor.execute('''CREATE TABLE IF NOT EXISTS users
            (username text, password text, fname text, lname text, lan text)''')
cursor.execute('''CREATE TABLE IF NOT EXISTS jobs
            (username text, title text, description text, employer text, location text, salary text)''')
cursor.execute('''CREATE TABLE IF NOT EXISTS userFunction
            (username text, email bool, sms bool, targetAD bool)''')

# Unit testing for program using pytest

from package import dbRead
from package import dbWrite
from package import menu
from package import userIO

# First we need to create users, then see if they exist in the databse or not

####################################################################
# Database must be empty in order for these following test to work #
####################################################################

def test_validateUsername():
    
    dbWrite.insertUser(db, 'Josh_123', 'Bananaboat88!', 'Josh', 'Stenson', 1) #adding first user to database for test
    assert dbRead.validateUser(db, "Josh_123") == False # Since "Josh" is already added his username is not available
    assert dbRead.validateUser(db, "James_The_Great") == True #available username
    assert dbRead.validateUser(db, "Red_Pill_Neo") == True #available username


def test_validatePassword():
    # Wrong passwords
    assert userIO.validatePassword("abc@d") == False #too short
    assert userIO.validatePassword("abcd@efg123456789") == False #too long
    assert userIO.validatePassword("123456789") == False #no alphabet
    assert userIO.validatePassword("aaaaaaaaa") == False #no digits
    assert userIO.validatePassword("abcde12345") == False #no sepcial chars

    # Correct password
    assert userIO.validatePassword("Az@123Tom?") == True


def test_insertUser():
    assert dbWrite.insertUser(db, "Unemployed_Todd", "Todd123!", "Todd", "Helsinki", 1) == True #adding second user to database for test
    assert dbWrite.insertUser(db, "James_88", "James123!", "James", "Bryant", 1) == True #adding third user to database for test
    assert dbWrite.insertUser(db, 'Billy_The_Goat','Billy123!','Billy', 'Baaa', 1) == True #adding fourth user to database for test
    assert dbWrite.insertUser(db, 'All_Mighty_Jesus','Jesus123!', 'Jesus', 'Ramirez', 1) == True #adding fifth user to database for test
    assert dbWrite.insertUser(db, 'Trent.exe','Trent123!','Trent', 'Howard', 1) == False #attempting to add a sixth user to database for test
    assert dbWrite.insertUser(db, 'Trent.exe','Trent123!','Trent', 'Howard', 1) == False #attempting to add a sixth user to database for test
#def Test_findpeople(fName, lName):
    
    
def test_loginUser():

    assert dbRead.loginUser(db, "Unemployed_Todd", "Todd123!") == True #Valid user for log-in
    assert dbRead.loginUser(db, "James_88", "James123!") == True #Valid user for log-in
    assert dbRead.loginUser(db, 'Billy_The_Goat','Billy123!') == True #Valid user for log-in
    assert dbRead.loginUser(db, "Bobby", "Bobby123!") == False #Invalid user for log-in
    assert dbRead.loginUser(db, "Neo", "Neo1234!") == False #Invalid user for log-in


def test_commitJob():
    assert dbWrite.commitJob("James_88", db, "Server", "Hospitality", "Miller's Ale House", "Tampa", "$500 per Week") == None #Job 1
    assert dbWrite.commitJob("James_88", db, "Bartneder", "Hospitality", "Miller's Ale House", "Tampa", "$500 per Week") == None #Job 2
    assert dbWrite.commitJob("James_88", db, "Busser", "Hospitality", "Miller's Ale House", "Tampa", "$500 per Week") == None #Job 3
    assert dbWrite.commitJob("James_88", db, "Host", "Hospitality", "Miller's Ale House", "Tampa", "$500 per Week") == None #Job 4
    assert dbWrite.commitJob("James_88", db, "Cook", "Hospitality", "Miller's Ale House", "Tampa", "$500 per Week") == None #Job 5

    assert dbWrite.commitJob("James_88", db, "Manager", "Hospitality", "Miller's Ale House", "Tampa", "$500 per Week") == 1 #Job 6 //Not allowed


# Testing the find_people function
def test_findpeople():
    # Todd Helsinki and Billy Baaa exist in database
    assert dbRead.find_people(db, "Todd", "Helsinki") == 1
    assert dbRead.find_people(db, "Billy", "Baaa") == 1

    # Turtle Fox and Armo Diolo DO NOT exist in databaase
    assert dbRead.find_people(db, "Turtle", "Fox") == 0
    assert dbRead.find_people(db, "Armo", "Diolo") == 0


# Testing the learn_skill function
def test_learnSkill():
    assert menu.learn_skills() == "Marketing\nSales\nEngineering\nWeb Design\nNursing"


# Testing the job_search function
def test_jobSearch():
    # using the job serach while not logged in
    assert menu.job_search(db, 0, "James_88") == None 

    ### Not really sure how to test this as it is not returning anything


# Testing the Langauges functions
def test_language():
    #testing the language function in menu
    assert menu.language(db, (0, "James_88")) == None #user is not logged in so it returns nothing

    #switching languages and testing if they were switched or not
    #english
    dbWrite.changeLanguage(db, "James_88", 1) #changing language to english
    assert dbRead.currentLanguage(db, "James_88") == 1 #check passed

    #spanish
    dbWrite.changeLanguage(db, "James_88", 2) #changing language to spanish
    assert dbRead.currentLanguage(db, "James_88") == 2 #check passed


# Testing the Privacy functions
def test_privacy():
    #setting the privacies
    dbWrite.changePrivacy(db, "James_88", 1) #turning them off
    dbWrite.changePrivacy(db, "James_88", 2) #turning them off
    dbWrite.changePrivacy(db, "James_88", 3) #turning them off

    #comparing the set privacy to the actual one
    assert dbRead.currentPrivacy(db, "James_88")[1] == 0 #off
    assert dbRead.currentPrivacy(db, "James_88")[2] == 0 #off
    assert dbRead.currentPrivacy(db, "James_88")[3] == 0 #off

    #setting the privacies
    dbWrite.changePrivacy(db, "James_88", 1) #turning them on
    dbWrite.changePrivacy(db, "James_88", 2) #turning them on
    dbWrite.changePrivacy(db, "James_88", 3) #turning them on

    #comparing the set privacy to the actual one
    assert dbRead.currentPrivacy(db, "James_88")[1] == 1 #on
    assert dbRead.currentPrivacy(db, "James_88")[2] == 1 #on
    assert dbRead.currentPrivacy(db, "James_88")[3] == 1 #on
