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
        db[0].execute("INSERT INTO userFriends VALUES (?,?,?)",(username, "", ""))
        db[1].commit()
        print('User added to database!')
        # 1 => true on success
        return 1
    if(count > 10):
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


def sendFriendRequest(db, username, friend):
    temp = []
    friends = []
    requests = []
    db[0].execute('SELECT friends, pending FROM userFriends WHERE username=?', (friend,))
    temp.append(db[0].fetchone())
    
    friends = temp[0][0].split(',')
    requests = temp[0][1].split(',')

    # if noting is in friend list or pending requests
    if len(friends) == 0 and len(requests) == 0:
        db[0].execute('UPDATE userFriends SET (pending)=(?)'
                      'WHERE username=?', (username, friend))

    # friend is already in friends list
    elif friends.count(username) != 0:
        return "You two are already friends"

    # request to friend already sent   
    elif requests.count(username) != 0:
        return "Friend request was already sent"

    # if the user is not in friends list or pending list
    else:
        string = ""
        # getting all request already in pending
        for x in requests:
            if x == friends[0]: 
                string = x
            elif string == "" and x != friends[0]:
                string = x
            else:
                string = string + "," + x
        # adding the new request
        string = string + "," + username
        db[0].execute('UPDATE userFriends SET (pending)=(?)'
                      'WHERE username=?', (string, friend))
        db[1].commit()

        return "Friend request sent"

def pendingRequest(db, username):
    temp = []
    friends = []
    requests = []
    db[0].execute('SELECT friends, pending FROM userFriends WHERE username=?', (username,))
    temp.append(db[0].fetchone())
    
    friends = temp[0][0].split(',')
    requests = temp[0][1].split(',')

    # checking to see if the requests are empty 
    if requests[0] == "" and len(requests) == 1:
        return "No new friend requests"

    string = ""

    # getting all the friends that exist in the firendlist already
    # this just works and gets rid of the linguring "" if it exists
    for x in friends:
        if x == friends[0]: 
            string = x
        elif string == "" and x != friends[0]:
            string = x
        else:
            string = string + "," + x

    # loops through all ending requests to accept or deny them
    for x in requests:
        # precaution to get rid a of empty strings
        if x != "":
            choice = input("{} has sent you a friend request! Y/y to accept or anything else to deny. ".format(x))

            # adding it to the friends
            if choice == 'Y' or choice == 'y':
                # if the string is empty 
                if string == "":
                    string = x
                else:
                    string = string + "," + x

                ### since this user accepted the friend request we have to also add this user to the other's friendlist
                otherTemp = []
                otherFriends = []
                db[0].execute('SELECT friends, pending FROM userFriends WHERE username=?', (x,))
                otherTemp.append(db[0].fetchone())
                
                otherFriends = temp[0][0].split(',')

                #everyone on the other users friendlist
                string2 = ""
                for x in otherFriends:
                    if x == otherFriends[0]: 
                        string2 = x
                    elif string2 == "" and x != otherFriends[0]:
                        string2 = x
                    else:
                        string2 = string2 + "," + x

                # adding this user to the other list
                string2 + string2 + "," + username

                db[0].execute('UPDATE userFriends SET (friends)=(?)'
                        'WHERE username=?', (string2, x))
                db[1].commit()

    # setting the new friends list and empty pending list
    db[0].execute('UPDATE userFriends SET (friends, pending)=(?,?)'
                      'WHERE username=?', (string, "", username))
    db[1].commit()
