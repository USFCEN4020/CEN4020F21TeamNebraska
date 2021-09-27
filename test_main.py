# Unit testing for main program using pytest

import main




# First we need to create users, then see if they exist in the databse or not

####################################################################
# Database must be empty in order for these following test to work #
####################################################################

def test_validateUsername(monkeypatch):
    
    main.insertUser('Josh_123', 'Bananaboat88!', 'Josh', 'Stenson') #adding first user to database for test
    assert main.validateUser("Josh_123") == False # Since "Josh" is already added his username is not available
    assert main.validateUser("James_The_Great") == True #available username
    assert main.validateUser("Red_Pill_Neo") == True #available username

def test_validatePassword(monkeypatch):
    # monkeypatch.setattr('builtins.input', lambda _: 6)
    
    # Wrong passwords
    assert main.validatePassword("abc@d") == False
    assert main.validatePassword("abcd@efg123456789") == False
    assert main.validatePassword("123456789") == False
    assert main.validatePassword("aaaaaaaaa") == False
    assert main.validatePassword("abcde12345") == False

    # Correct password
    assert main.validatePassword("Az@123Tom?") == True


def test_insertUser():
    assert main.insertUser("Unemployed_Todd", "Todd123!", "Todd", "Helsinki") == True #adding second user to database for test
    assert main.insertUser("James_88", "James123!", "James", "Bryant") == True #adding third user to database for test
    assert main.insertUser('Billy_The_Goat','Billy123!','Billy', 'Baaa') == True #adding fourth user to database for test
    assert main.insertUser('All_Mighty_Jesus','Jesus123!', 'Jesus', 'Ramirez') == True #adding fifth user to database for test
    assert main.insertUser('Trent.exe','Trent123!','Trent', 'Howard') == False #attempting to add a sixth user to database for test
    assert main.insertUser('Trent.exe','Trent123!','Trent', 'Howard') == False #attempting to add a sixth user to database for test
#def Test_findpeople(fName, lName):
    
    
def test_loginUser():

    assert main.loginUser("Unemployed_Todd", "Todd123!") == True #Valid user for log-in
    assert main.loginUser("James_88", "James123!") == True #Valid user for log-in
    assert main.loginUser('Billy_The_Goat','Billy123!') == True #Valid user for log-in
    assert main.loginUser("Bobby", "Bobby123!") == False #Invalid user for log-in
    assert main.loginUser("Neo", "Neo1234!") == False #Invalid user for log-in

def test_commitJob():
    assert main.commitJob("Server", "Hospitality", "Miller's Ale House", "Tampa", "$500 per Week") == None #Job 1
    assert main.commitJob("Bartneder", "Hospitality", "Miller's Ale House", "Tampa", "$500 per Week") == None #Job 2
    assert main.commitJob("Busser", "Hospitality", "Miller's Ale House", "Tampa", "$500 per Week") == None #Job 3
    assert main.commitJob("Host", "Hospitality", "Miller's Ale House", "Tampa", "$500 per Week") == None #Job 4
    assert main.commitJob("Cook", "Hospitality", "Miller's Ale House", "Tampa", "$500 per Week") == None #Job 5

    assert main.commitJob("Manager", "Hospitality", "Miller's Ale House", "Tampa", "$500 per Week") == False #Job 6 //Not allowed




