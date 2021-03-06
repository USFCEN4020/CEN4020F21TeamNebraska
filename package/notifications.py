from package.dbRead import getUserProfile
from package.notify import getAllMessages
from datetime import datetime as dt


def countNewMessages(db, username):
    count = 0
    messages = getAllMessages(db, username)
    for i in range(0, messages.size()):
        if messages[i][0][2] == False:
            count += 1
    return count

def countNewUsers(db, username):
    count = 0
    user_result = []
    db[0].execute('SELECT username, lastLogin, createdOn FROM users')
    results = db[0].fetchall()
    for i in results:
        if i[0] == username:
            user_result = i
            break
    
    for i in results:
        if i[2] < user_result[1]:
            count = count + 1
    
    return count
        

def getNotifications(db, isLoggedIn, username):
    notifs = []
    if(isLoggedIn):
        # alert if any new messages
        msgs = countNewMessages(db, username)
        if(msgs > 0):
            print("You have", msgs, "new messages.")
        prof = getUserProfile(db, username)
        if(prof == None):
            print("You still need to create a profile.")
        if(countNewUsers(db, username) > 0):
            print(countNewUsers(db, username), "new users have registered since you last logged in.")
    return