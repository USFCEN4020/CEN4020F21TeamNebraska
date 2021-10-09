import sqlite3
from package import dbRead as rd
from package import userIO as io

# Insert User in Database
def insertUser(db, username, password, fname, lname, lan):
    # counter to limit
    # number of accounts
    count = 1
    # count no. of users
    for i in db[0].execute('SELECT * FROM users'):
        count += 1

    # insert if validated
    if(io.validatePassword(password) and rd.validateUser(db, username) and count < 6):
        db[0].execute("INSERT INTO users VALUES (?,?,?,?,?)",(username, password, fname, lname, lan))
        db[0].execute("INSERT INTO userFunction VALUES (?,?,?,?)",(username, True, True, True))
        db[0].execute("INSERT INTO userProfile VALUES (?,?,?,?,?)",(username, True, True, True, True))
        db[1].commit()
        print('User added to database!')
        # 1 => true on success
        return 1
    if(count > 5):
        print("All permitted accounts have been created, please come back later")
        # 0 => false on failure
        return 0

def commitJob(userName, db, title, description, employer, location, salary):
    # counter to limit
    # number of accounts
    count = 1
    # count no. of users
    for i in db[0].execute('SELECT * FROM jobs'):
        count += 1
    if (count > 5):
        print("All permitted Jobs Have been created")
        return 1
    else:
        db[0].execute("INSERT INTO jobs VALUES (?,?,?,?,?,?)",(userName, title,description, employer, location, salary))
        db[1].commit()
        print("Job", title, "posted successfully!")

def changeLanguage(db, userName, lan):
    db[0].execute('UPDATE users SET lan=? WHERE username=?',(lan, userName))
    db[1].commit()

def changePrivacy(db, userName, option):
    current = rd.currentPrivacy(db, userName)
    selected = ['email', 'sms', 'targetAD']
    db[0].execute(f'UPDATE userFunction SET {selected[option - 1]}=? WHERE username=?',
                  (not current[option], userName))
    db[1].commit()

# Insert functions for User Profile
def insertUserTitle(db, userName, title):
    db[0].execute('UPDATE userProfile SET title=? WHERE username=?',(title, userName))
    db[1].commit()
    print("Profile title has been added")

def insertUserMajor(db, userName, major):
    db[0].execute('UPDATE userProfile SET major=? WHERE username=?',(major, userName))
    db[1].commit()
    print("Profile major has been added")

def insertUserSchoolName(db, userName, schoolname):
    db[0].execute('UPDATE userProfile SET schoolname=? WHERE username=?',(schoolname, userName))
    db[1].commit()
    print("School name has been added")

def insertUserBio(db, userName, Bio):
    db[0].execute('UPDATE userProfile SET Bio=? WHERE username=?',(Bio, userName))
    db[1].commit() 
    print("Bio has been added")  

def insertUserExperience(db, userName, employer, startdate, enddate, location, description):
    count = 0
    t = (userName,)
    for i in db[0].execute('SELECT * FROM userExperience WHERE username=?', t):
        count = count + 1
    if (count > 2):
        print(count)
        print("You may only list 3 jobs under your experience section")
        return 1
    else:
        db[0].execute("INSERT INTO userExperience VALUES (?,?,?,?,?,?)",(userName, employer, startdate, enddate, location, description))
        db[1].commit()
        print("Experience has been added")
def insertUserEducation(db, userName, schoolname, degree, years_attended):
    count = 0
    t = (userName,)
    for i in db[0].execute('SELECT * FROM userEducation WHERE username=?', t):
        count = count + 1
    if (count > 1):
        print(count)
        print("You may only list 2 schools under your education section")
        return 1
    else:
        db[0].execute("INSERT INTO userEducation VALUES (?,?,?,?)",(userName, schoolname, degree, years_attended))
        db[1].commit()
        print("Education has been added")
