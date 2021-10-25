# searches usernames from users table based on last name
def searchByLname(db, Lname):
    users = []
    db[0].execute('SELECT username FROM users WHERE lname=?', (Lname,))
    users.append(db[0].fetchall())
    
    return users[0]


# searches username from userEducation table based on school name
def searchByUniversity(db, university):
    users = []
    db[0].execute('SELECT username FROM userEducation WHERE schoolname=?', (university,))
    users.append(db[0].fetchall())
    
    return users[0]


# searches username from userProfile table based on major
def searchByMajor(db, major):
    users = []
    db[0].execute('SELECT username FROM userProfile WHERE major=?', (major,))
    users.append(db[0].fetchall())
    
    return users[0]


# the user sends friend request another user
def sendFriendRequest(db, username, friend):
    friends = []
    requests = []

    # getting all the friends of the other user(whom we want to add)
    db[0].execute('SELECT friend FROM userFriends WHERE username=?', (friend,))
    friends.append(db[0].fetchall())

    # user is already on their friend list
    if (friends[0].count((username,)) != 0):
        print("You two are already friends!")
        return

    # getting all the pending request for the other user(whom we want to add)
    db[0].execute('SELECT request FROM friendRequests WHERE username=?', (friend,))
    requests.append(db[0].fetchall())

    # user has already sent them a friend request before
    if (requests[0].count((username,)) != 0):
        print("You have already sent a request before!")
        return

    # sending a friend request
    db[0].execute("INSERT INTO friendRequests VALUES (?,?)",(friend, username))
    db[1].commit()
    print("Friend request sent!")


# user can accepts or deny all pending friend requests
def pendingRequests(db, username):
    requests = []

    # getting all the pending request for user
    db[0].execute('SELECT request FROM friendRequests WHERE username=?', (username,))
    requests.append(db[0].fetchall())

    # no new friend request
    if (len(requests[0]) == 0):
        print("You have no new friend request!")
        return

    for x in requests[0]:
        choice = input("{} has sent you a friend request! Y/y to accept or anything else to deny. ".format(x[0]))

        if choice == 'Y' or choice == 'y':
            # removing user from friend request table
            db[0].execute('DELETE FROM friendRequests WHERE username=? AND request=?', (username, x[0]))
            db[1].commit()

            # adding user to friend list
            db[0].execute("INSERT INTO userFriends VALUES (?,?)",(username, x[0]))
            db[1].commit()

            # adding this user to the other's friend list
            db[0].execute("INSERT INTO userFriends VALUES (?,?)",(x[0], username))
            db[1].commit()

# This function is called when the use logs-in and it goes through their pending
# friend request list and asks to either accept them or deny them
def connectFriend(db, isLoggedIn, username):
    if not isLoggedIn:
        print('Please login or sign up to connect with friends.')
    else:
        choice = input("Enter 1 to serach users by last name, 2 to search users by university, 3 to search users by major: ")
        while (choice < 1 or choice > 3):
            choice = input("Enter 1 to serach by last name, 2 to search by university, 3 to search by major: ")
        
        # searching and adding user by last name
        if choice == 1:
            lname = input("Enter the user's lname: ")
            users = searchByLname(db, lname)

            if len(users) == 0:
                print("No user with last name {} was found".format(lname))
            else:
                for x in range(0, len(users)):
                    print("{}. {}".format(x+1, users[x][0]))

            select = input("select the number coresponding with the user you want to add: ")
            sendFriendRequest(db, username, users[select - 1][0])

            return

        # searching and adding user by university
        elif choice == 2:
            university = input("Enter the user's university: ")
            users = searchByUniversity(db, university)

            if len(users) == 0:
                print("No user in {} was found".format(university))
            else:
                for x in range(0, len(users)):
                    print("{}. {}".format(x+1, users[x][0]))

            select = input("select the number coresponding with the user you want to add: ")
            sendFriendRequest(db, username, users[select - 1][0])

            return

        # searching and adding user by major
        elif choice == 3:
            major = input("Enter the user's major: ")
            users = searchByMajor(db, major)

            if len(users) == 0:
                print("No user with major {} was found".format(major))
            else:
                for x in range(0, len(users)):
                    print("{}. {}".format(x+1, users[x][0]))

            select = input("select the number coresponding with the user you want to add: ")
            sendFriendRequest(db, username, users[select - 1][0])

            return


# "Show my Network"
def myFriends(db, username):
    friends = []

    # getting all the friends of user
    db[0].execute('SELECT friend FROM userFriends WHERE username=?', (username,))
    friends.append(db[0].fetchall())

    # connected with no friends
    if (len(friends[0]) == 0):
        print("\nYou are connected with no yet!")
        return

    # printing all the connections
    print("\nYou have connected with:")
    for x in friends[0]:
        print(x[0])
    print("")

# "disconnect from someone"
def deleteFriend(db, username, friend):
    # removing friend from friend list
    db[0].execute('DELETE FROM userFriends WHERE username=? AND friend=?', (username, friend))
    db[1].commit()

    # removing user from friend's friend list
    db[0].execute('DELETE FROM userFriends WHERE username=? AND friend=?', (friend, username))
    db[1].commit()

    print("You two are no longer connected")