import sqlite3
import os

from package import dbWrite as wr
from package import job as jb

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
cursor.execute('''CREATE TABLE IF NOT EXISTS appliedFor
            (username text, employer text, title text, graduation text, startDate text, whyU text, whyThisJob text, applydate current_timestamp)''')
cursor.execute('''CREATE TABLE IF NOT EXISTS savedJobs
            (username text, employer text, title text)''')
cursor.execute('''CREATE TABLE IF NOT EXISTS inbox
                (receiver text, sender text, message text, read bool)''')
cursor.execute('''CREATE TABLE IF NOT EXISTS notify
                (sender text, receiver bool)''')


# entering dummy users into users
wr.insertUser(db, "Unemployed_Todd", "Todd123!", "Todd", "Helsinki", 1, "standard")
wr.insertUser(db, "James_88", "James123!", "James", "Bryant", 1, "standard")
wr.insertUser(db, 'Billy_The_Goat','Billy123!','Billy', 'Baaa', 1, "standard")
wr.insertUser(db, 'All_Mighty_Jesus','Jesus123!', 'Jesus', 'Ramirez', 1, "standard")
wr.insertUser(db, 'Trent.exe','Trent123!','Trent', 'Howard', 1, "standard")
wr.insertUser(db, 'Undertaker','Sckyler123!','lamb', 'password', 1, "plus")
wr.insertUser(db, 'Parxi','Ready123!','Xhristophin', 'one', 1, "plus")
wr.insertUser(db, 'darthmartain','Starwars123!','Nickoly', 'micky', 1, "plus")
wr.insertUser(db, 'KnightNinja','Knsd123!','Knight', 'Ninja', 1, "plus")


def test_jobs():
    # commiting a few jobs
    jb.commitJob("A", db, "A Job", "Get the job done", "Ahmad", "Tampa", "10000")
    jb.commitJob("B", db, "B Job", "Get the job done", "Ahmad", "Tampa", "10000")
    jb.commitJob("C", db, "C Job", "Get the job done", "Ahmad", "Tampa", "10000")

    # printing to see if the jobs were added or not
    jobs = []
    db[0].execute('SELECT * FROM jobs')
    jobs.append(db[0].fetchall())

    # formating and printing jobs
    jobCount = 0
    for x in jobs[0]:
        jobCount += 1

        print("{}. Title:       {}".format(jobCount, x[1]))
        print("   Description: {}".format(x[2]))
        print("   Employer:    {}".format(x[3]))
        print("   Location:    {}".format(x[4]))
        print("   Salary:      {}".format(x[5]))

    # deleting a jobs
    jb. deleteJob(db, "B", "Ahmad", "B Job")

    # printing jobs afterr deleting B:
    jobsAfter = []

    db[0].execute('SELECT * FROM jobs')
    jobsAfter.append(db[0].fetchall())

    jobCount = 0
    for x in jobsAfter[0]:
        jobCount += 1

        print("{}. Title:       {}".format(jobCount, x[1]))
        print("   Description: {}".format(x[2]))
        print("   Employer:    {}".format(x[3]))
        print("   Location:    {}".format(x[4]))
        print("   Salary:      {}".format(x[5]))
