import sqlite3
from package import dbWrite

conn = sqlite3.connect('inCollege5.db')
cursor = conn.cursor()
db = (cursor, conn)

# Create user table
cursor.execute('''CREATE TABLE IF NOT EXISTS users
            (username text, password text, fname text, lname text, lan text)''')
cursor.execute('''CREATE TABLE IF NOT EXISTS jobs
            (username text, title text, description text, employer text, location text, salary text)''')
cursor.execute('''CREATE TABLE IF NOT EXISTS userFunction
            (username text, email bool, sms bool, targetAD bool)''')
cursor.execute('''CREATE TABLE IF NOT EXISTS userProfile
            (username text, title text, major text, schoolname text, bio text)''')
#userExperience table will hold 3 jobs for each user in the same table. In order to view or print their jobs you will have to search by username
cursor.execute('''CREATE TABLE IF NOT EXISTS userExperience
            (username text, employer text, startdate text, enddate text, location text, description text, counts text)''')
#userEducation table will hold 2 schools for each user in the same table. In order to view or print their jobs you will have to search by username
cursor.execute('''CREATE TABLE IF NOT EXISTS userEducation
            (username text, schoolname text, degree text, years_attended text, counts text)''')
#friends
cursor.execute('''CREATE TABLE IF NOT EXISTS userFriends
            (username text, friends text, pending text)''')

test_user = "Josh_123"

def test_insertUser():
    assert dbWrite.insertUser(db, "Unemployed_Todd", "Todd123!", "Todd", "Helsinki", 1) == True #adding second user to database for test
    assert dbWrite.insertUser(db, "James_88", "James123!", "James", "Bryant", 1) == True #adding third user to database for test
    assert dbWrite.insertUser(db, 'Billy_The_Goat','Billy123!','Billy', 'Baaa', 1) == True #adding fourth user to database for test
    assert dbWrite.insertUser(db, 'All_Mighty_Jesus','Jesus123!', 'Jesus', 'Ramirez', 1) == True #adding fifth user to database for test

    
def test_commitJob():
    assert dbWrite.commitJob("James_88", db, "Server", "Hospitality", "Miller's Ale House", "Tampa", "$500 per Week") == None #Job 1
    assert dbWrite.commitJob("James_88", db, "Bartneder", "Hospitality", "Miller's Ale House", "Tampa", "$500 per Week") == None #Job 2
    assert dbWrite.commitJob("James_88", db, "Busser", "Hospitality", "Miller's Ale House", "Tampa", "$500 per Week") == None #Job 3
    assert dbWrite.commitJob("James_88", db, "Host", "Hospitality", "Miller's Ale House", "Tampa", "$500 per Week") == None #Job 4
    assert dbWrite.commitJob("James_88", db, "Cook", "Hospitality", "Miller's Ale House", "Tampa", "$500 per Week") == None #Job 5

    assert dbWrite.commitJob("James_88", db, "Manager", "Hospitality", "Miller's Ale House", "Tampa", "$500 per Week") == 1 #Job 6 //Not allowed

def test_friends():
    dbWrite.sendFriendRequest(db, "Unemployed_Todd", "James_88")
    dbWrite.sendFriendRequest(db, "Billy_The_Goat", "James_88")

    temp = []
    requests = []
    db[0].execute('SELECT friends, pending FROM userFriends WHERE username=?', ("James_88",))
    temp.append(db[0].fetchone())

    requests = temp[0][1].split(',')
    print(requests)

    dbWrite.pendingRequest(db, "James_88")

    temp = []
    friends = []
    db[0].execute('SELECT friends, pending FROM userFriends WHERE username=?', ("James_88",))
    temp.append(db[0].fetchone())

    friends = temp[0][0].split(',')
    print(friends)
