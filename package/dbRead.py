# logs a user in
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

# username is the Account Name
def validateUser(db, username): 
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
    if check is None:
        return 0
    else:
        return 1

# finds username based on first and last name fron users table
def nameToUserName(db, fName, lName):
    db[0].execute('SELECT * FROM users WHERE fname=? AND lname=?', (fName, lName))
    check = db[0].fetchone()
    if check is None:
        return None
    else:
        return check[0]

# get a users selected language
def currentLanguage(db, username):
    db[0].execute('SELECT lan FROM users WHERE username=?', (username,))
    lan = db[0].fetchone()
    return int(lan[0])

# gets a users selected privacy option
def currentPrivacy(db, username):
    db[0].execute('SELECT * FROM userFunction WHERE username=?', (username,))
    privacy = db[0].fetchone()
    return privacy

# gets a users profile based on thier username
def getUserProfile(db, username):
    profile = []
    db[0].execute('SELECT * FROM userProfile WHERE username=?', (username,))
    profile.append(db[0].fetchone())
    db[0].execute('SELECT * FROM UserExperience WHERE username=?', (username,))
    profile.append(db[0].fetchall())
    db[0].execute('SELECT * FROM userEducation WHERE username=?', (username,))
    profile.append(db[0].fetchall())
    if profile[0] is None:
        return None
    else:
        if profile[1] == [] or profile[2] == []:
            profile.append(None)
            return profile
        for each in profile:
            for index in range(len(each)):
                if each[index] == "1":
                    profile.append(None)
                    return profile
    return profile