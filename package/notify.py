# Go through new messages during login/notification time
def getNewMessages(db, userName) :
    messages = getAllMessages(db, userName)
    size = len(messages)

    # no new messages
    if not any(messages):
        print("You have no new messages!")
        return
    
    # new messages
    print("You have {} new messages!".format(size))
    for x in range(0, size) :
        # print messages one by one
        if (messages[x][0][2] == False) :
            print("{}. {}".format(x+1, messages[x][0]))
            # ask to mark read on each message
            markRead = input("Do you want to mark this message read? Press Y to proceed and any other key to skip.")
            if (markRead == 'Y') :
                db[0].execute('INSERT INTO inbox(read) VALUES(?)', (True,))
            # ask for reply
            isReply = input("Do you want to reply to this message? Press Y to proceed and any other key to skip.")
            if (isReply == 'Y') :
                sendToUser = messages[x][0][0]
                enterReply = input("Type your reply: ")
                db[0].execute('INSERT INTO inbox VALUES(?,?,?,?)', (sendToUser, userName, enterReply, False))
            deleteMsg = input("Do you want to now delete this message? Press Y to proceed and any other key to skip.")
            if (deleteMsg == 'Y') :
                sender = messages[x][0][0]
                receiver = userName
                msg = messages[x][0][1]
                deleteMessage(db, sender, receiver, msg)
            print('\n')
        else :
            print("The message number: {} has been read!", (x+1))
            print('\n')
    return

# Read a message
def readMessage(db, userName) :
    messages = getAllMessages(db, userName)
    size = len(messages)
    if not any(messages):
        print("You have no new messages!")
        return

    for x in range(0, size) :
        # print messages one by one
        print("{}. {}".format(x+1, messages[x][0]))
        # ask to mark read on each message
        markRead = input("Do you want to mark this message read? Press Y to proceed and any other key to skip.")
        if (markRead == 'Y') :
            db[0].execute('INSERT INTO inbox(read) VALUES(?)', (True,))
        print('\n')
    return

# Reply to a message
def replyMessage(db, userName) :
    messages = getAllMessages(db, userName)
    size = len(messages)
    for x in range(0, size) :
        # print messages one by one
        print("{}. {}".format(x+1, messages[x][0]))
        # ask for reply
        isReply = input("Do you want to reply to this message? Press Y to proceed and any other key to skip.")
        if (isReply == 'Y') :
            sendToUser = messages[x][0][0]
            enterReply = input("Type your reply: ")
            db[0].execute('INSERT INTO inbox VALUES(?,?,?,?)', (sendToUser, userName, enterReply, False))
        print('\n')
    return

# Fetch list of all messages from db
def getAllMessages(db, userName) :
    messages = []
    db[0].execute('SELECT sender, message, read FROM inbox WHERE receiver=?', (userName,))
    messages.append(db[0].fetchall())
    return messages

def deleteMessage(db, sender, receiver, msg) :
    db[0].execute('DELETE FROM inbox WHERE sender=? AND receiver=? AND message=?', (sender, receiver, msg,))
    print("Your message has been deleted!")
    print('\n')
    return