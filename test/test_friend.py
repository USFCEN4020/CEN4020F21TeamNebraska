import sqlite3
import os

from package import dbWrite as wr
from package import friend as fd

# deleting the database file
os.remove("inCollegetest.db")

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


def test_friends():
    # printing james friend list
    fd.myFriends(db, "James_88")

    # sending friend requests from 
    fd.sendFriendRequest(db, "Unemployed_Todd", "James_88")
    fd.sendFriendRequest(db, "Billy_The_Goat", "James_88")
    fd.sendFriendRequest(db, "KnightNinja", "James_88")
    fd.sendFriendRequest(db, 'Parxi', "James_88")
    fd.sendFriendRequest(db, 'Parxi', "James_88") # this user already sent a friend request before
    
    # going through james pending requests
    fd.pendingRequests(db, "James_88")

    # checking to see if friends were added to james friend list
    fd.myFriends(db, "James_88")

    # removing billy and todd from james friend list
    fd.deleteFriend(db, "James_88", "Billy_The_Goat")
    fd.deleteFriend(db, "James_88", "KnightNinja")

    # checking to see if billy and tood were removed or not
    fd.myFriends(db, "James_88")
