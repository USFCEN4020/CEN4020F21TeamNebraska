import sqlite3


def loginUser(db, username, password):
    # fetch user
    db[0].execute('SELECT username, password FROM users WHERE username=? AND password=?', (username, password))
    if (db[0].fetchone()):
        print('You have successfully logged in')
        # 1 => true on success
        return 1
    else:
        print('Incorrect username / password, please try again"')
        # 0 => false on failure
        return 0


def validateUser(db, username):  # username is the Account Name
    valid = True
    count = 0
    t = (username,)

    for i in db[0].execute('SELECT * FROM users WHERE username=?', t):
        count = count + 1

        if count == 0:
            valid = True
        else:
            valid = False
            print("Sorry, your username has already been taken.")

    return valid


# find people by firstName and lastName
def find_people(db, fName, lName):
    db[0].execute('SELECT * FROM users WHERE fname=? AND lname=?', (fName, lName))
    check = db[0].fetchone()
    if (check == None):
        return 0
    else:
        return 1


def currentLanguage(db, username):
    db[0].execute('SELECT lan FROM users WHERE username=?', (username,))
    lan = db[0].fetchone()
    return int(lan[0])


def currentPrivacy(db, username):
    db[0].execute('SELECT * FROM userFunction WHERE username=?', (username,))
    privacy = db[0].fetchone()
    return privacy
