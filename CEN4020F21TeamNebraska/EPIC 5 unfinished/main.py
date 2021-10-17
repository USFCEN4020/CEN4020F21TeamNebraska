#Team Nebraska
#Epic 3

# Database used
import sqlite3

from package import dbRead as rd
from package import dbWrite as wr
from package import menu as menu

# Connection object represents
# the database
conn = sqlite3.connect('inCollege2.db')

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


menu.mainMenu(db)
