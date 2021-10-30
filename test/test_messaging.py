import sqlite3
import os

from package import dbWrite as wr
from package import friend as fd
from package import tier as tr
from package import message as ms

# deleting the database file
#os.remove("inCollegetest.db")

# creating the database
conn = sqlite3.connect('inCollegetest.db')
cursor = conn.cursor()
db = (cursor, conn)

# Create user table
cursor.execute('''CREATE TABLE IF NOT EXISTS users
            (username text, password text, fname text, lname text, lan text, tier text)''')
cursor.execute('''CREATE TABLE IF NOT EXISTS jobs
            (username text, title text, description text, employer text, location text, salary text)''')
cursor.execute('''CREATE TABLE IF NOT EXISTS userFunction
            (username text, email bool, sms bool, targetAD bool)''')
cursor.execute('''CREATE TABLE IF NOT EXISTS userProfile
            (username text, title text, major text, schoolname text, bio text)''')
cursor.execute('''CREATE TABLE IF NOT EXISTS userExperience
            (username text, employer text, startdate text, enddate text, location text, description text, counts text)''')
cursor.execute('''CREATE TABLE IF NOT EXISTS userEducation
            (username text, schoolname text, degree text, years_attended text, counts text)''')
cursor.execute('''CREATE TABLE IF NOT EXISTS userFriends
            (username text, friend text)''')
cursor.execute('''CREATE TABLE IF NOT EXISTS friendRequests
            (username text, request text)''')
# appliedFor table (username, employer, title, graduation, startDate, whyU, whyThisJob)
cursor.execute('''CREATE TABLE IF NOT EXISTS appliedFor
            (username text, employer text, title text, graduation text, startDate text, whyU text, whyThisJob text)''')
# savedJobs table (username, employer, title)
cursor.execute('''CREATE TABLE IF NOT EXISTS savedJobs
            (username text, employer text, title text)''')
#inbox
cursor.execute('''CREATE TABLE IF NOT EXISTS inbox
                (receiver text, sender text, message text, read bool)''')
#notify
cursor.execute('''CREATE TABLE IF NOT EXISTS notify
                (sender text, receiver bool)''')


# entering dummy users into the database
wr.insertUser(db, "Unemployed_Todd", "Todd123!", "Todd", "Helsinki", 1, "standard")
wr.insertUser(db, "James_88", "James123!", "James", "Bryant", 1, "standard")
wr.insertUser(db, 'Billy_The_Goat','Billy123!','Billy', 'Baaa', 1, "standard")
wr.insertUser(db, 'All_Mighty_Jesus','Jesus123!', 'Jesus', 'Ramirez', 1, "standard")
wr.insertUser(db, 'Trent.exe','Trent123!','Trent', 'Howard', 1, "standard")
wr.insertUser(db, 'Undertaker','Sckyler123!','lamb', 'password', 1, "plus")
wr.insertUser(db, 'Parxi','Ready123!','Xhristophin', 'one', 1, "plus")
wr.insertUser(db, 'darthmartain','Starwars123!','Nickoly', 'micky', 1, "plus")
wr.insertUser(db, 'KnightNinja','Knsd123!','Knight', 'Ninja', 1, "plus")



def testMessaging():
    
    assert ms.sendMessage(db, "Unemployed_Todd", "Parxi", "standard") == -1 #Sending message to non-friend == Should Fail beacuse of standard memebership
    assert ms.sendMessage(db, "Unemployed_Todd", "Parxi", "plus") == 1 #Sending message to non-friend == Should work beacuse of plus memebership
    
    