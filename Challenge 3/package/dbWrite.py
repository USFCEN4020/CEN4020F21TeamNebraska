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