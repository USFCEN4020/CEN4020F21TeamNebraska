from package import dbRead as rd
from package import userIO as io
from datetime import datetime as dt

def updateUserCourses(db, username, course):
    db[0].execute("INSERT INTO learning VALUES (?, ?)", (username, course))
    db[1].commit()
    return

def updateUserLogin(db, username):
    db[0].execute("UPDATE users SET lastLogin = (?) WHERE username = (?)", dt.now(), username)
    db[1].commit()
    return

# Insert User in Database
def insertUser(db, username, password, fname, lname, lan, tier, now):
    # counter to limit
    # number of accounts
    count = 1
    # count no. of users
    for i in db[0].execute('SELECT * FROM users'):
        count += 1

    # insert if validated
    if(io.validatePassword(password) and rd.validateUser(db, username) and count <= 10):
        db[0].execute("INSERT INTO users VALUES (?,?,?,?,?,?, ?, ?)",(username, password, fname, lname, lan, tier, now, now))
        db[0].execute("INSERT INTO userFunction VALUES (?,?,?,?)",(username, True, True, True))
        db[0].execute("INSERT INTO userProfile VALUES (?,?,?,?,?)",(username, True, True, True, True))
        db[1].commit()
        print('User added to database!')
        # 1 => true on success
        return 1
    if(count > 10):
        print("All permitted accounts have been created, please come back later")
        # 0 => false on failure
        return 0


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

def insertUserExperience(db, userName, employer, startdate, enddate, location, description, counts = 0):
    count = 1
    t = (userName,)
    if counts == 0:
        for i in db[0].execute('SELECT * FROM userExperience WHERE username=?', t):
            count = count + 1
        if (count > 3):
            print("You may only list 3 jobs under your experience section")
            return 1
        else:
            db[0].execute("INSERT INTO userExperience VALUES (?,?,?,?,?,?,?)",(userName, employer, startdate, enddate, location, description, count))
            db[1].commit()
            print("Experience has been added")
    else:
        db[0].execute('UPDATE userExperience SET (employer,startdate,enddate,location,description)=(?,?,?,?,?) '
                      'WHERE username=? and counts=?',
                      (employer, startdate, enddate, location, description, userName, counts))
        db[1].commit()
        print("Experience has been modified")

def insertUserEducation(db, userName, schoolname, degree, years_attended, counts = 0):
    count = 1
    t = (userName,)
    if counts == 0:
        for i in db[0].execute('SELECT * FROM userEducation WHERE username=?', t):
            count = count + 1
        if (count > 2):
            print("You may only list 2 schools under your education section")
            return 1
        else:
            db[0].execute("INSERT INTO userEducation VALUES (?,?,?,?,?)",(userName, schoolname, degree, years_attended, count))
            db[1].commit()
            print("Education has been added")
    else:
        db[0].execute('UPDATE userEducation SET (schoolname,degree,years_attended)=(?,?,?) '
                      'WHERE username=? and counts=?',
                      (schoolname, degree, years_attended, userName, counts))
        db[1].commit()
        print("Experience has been modified")
