import sqlite3
from package import menu as menu


# Creating the database
conn = sqlite3.connect('inCollege.db')
cursor = conn.cursor()
db = (cursor, conn)


# users table (username, password, fname, lname, language)
cursor.execute('''CREATE TABLE IF NOT EXISTS users
            (username text, password text, fname text, lname text, lan text, tier text)''')
# jobs table (username, title, description, employer, location, salary)
cursor.execute('''CREATE TABLE IF NOT EXISTS jobs
            (username text, title text, description text, employer text, location text, salary text)''')
# userFunction table (username, email, sms, targetAD)
cursor.execute('''CREATE TABLE IF NOT EXISTS userFunction
            (username text, email bool, sms bool, targetAD bool)''')
# userProfile table (username, title, major, schoolname, bio)
cursor.execute('''CREATE TABLE IF NOT EXISTS userProfile
            (username text, title text, major text, schoolname text, bio text)''')
# userExperience table (username, employer, startdate, enddate, location, description, counts)
cursor.execute('''CREATE TABLE IF NOT EXISTS userExperience
            (username text, employer text, startdate text, enddate text, location text, description text, counts text)''')
# userEducation table (username, schoolname, degree, years_attended, counts)
cursor.execute('''CREATE TABLE IF NOT EXISTS userEducation
            (username text, schoolname text, degree text, years_attended text, counts text)''')
# userFriends table (username, friend)
cursor.execute('''CREATE TABLE IF NOT EXISTS userFriends
            (username text, friend text)''')
# friendRequests table (username, request)
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


# calling the main menu function
menu.mainMenu(db)
