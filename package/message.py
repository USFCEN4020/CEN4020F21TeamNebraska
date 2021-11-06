from package import friend as fd
from package import tier as tr

def getMessage():
    message = input("Please input message: ")
    return message

# the user sends friend request to friend
def sendMessage(db, username, friend, tier):
    friends = []
    

    # getting all the friends of the other user
    db[0].execute('SELECT friend FROM userFriends WHERE username=?', (friend,))
    friends.append(db[0].fetchall())
    
    # If user is not on their friend list
    if (tier[0] == "standard" or tier == "standard"):
        if (friends[0].count((username,)) == 0):
            print("You two are not friends so you can not send a message")
            return -1
        else:
            # sending a friend request since user is a friendr
            message = getMessage()
            print("Message sent!(SU)")
            db[0].execute("INSERT INTO inbox VALUES (?,?,?,?)",(friend, username, message, False)) #message goes in friends inbox
            db[1].commit()
            return 1
    else: 
        message = getMessage()
        print("Message sent!(PU)")
        db[0].execute("INSERT INTO inbox VALUES (?,?,?,?)",(friend, username, message, False))
        db[1].commit()
        return 1

    

def connectUsertoMessage(db, isLoggedIn, username):
    if not isLoggedIn:
        print('Please login or sign up to send message.')
    else:
        choice = input("Enter 1 to search users by last name, 2 to search users by university, 3 to search users by major: ")
        choice = int(choice)
        while (choice < 1 or choice > 3):
            choice = input("Enter 1 to serach by last name, 2 to search by university, 3 to search by major: ")
        
        # searching and adding user by last name
        if choice == 1:
            lname = input("Enter the user's lname: ")
            users = fd.searchByLname(db, lname)

            if len(users) == 0:
                print("No user with last name {} was found".format(lname))
                return -1
            else:
                for x in range(0, len(users)):
                    print("{}. {}".format(x+1, users[x][0]))
            
                user_choice_to_send_message = input("Would you like to send someone from this list a message? Y/y to accept or anything else to deny.")
                if user_choice_to_send_message == 'Y' or user_choice_to_send_message == 'y':
                    select = input("Select the number coresponding with the user you want to send a message to: ")
                    select = int(select)
                    tier = tr.getTier(db, username)
                    
                    sendMessage(db, username, users[select - 1][0], 'standard') #sendFriendRequest(db, username, users[select - 1][0])

                return 1


        # searching and adding user by university
        elif choice == 2:
            university = input("Enter the user's university: ")
            users = fd.searchByUniversity(db, university)

            if len(users) == 0:
                print("No user in {} was found".format(university))
                return -1
            else:
                for x in range(0, len(users)):
                    print("{}. {}".format(x+1, users[x][0]))

                user_choice_to_send_message = input("Would you like to send someone from this list a message? Y/y to accept or anything else to deny.")
                if user_choice_to_send_message == 'Y' or user_choice_to_send_message == 'y':
                    select = input("Select the number coresponding with the user you want to send a message to: ")
                    select = int(select)
                
                    sendMessage(db, username, users[select - 1][0], 'standard') #sendFriendRequest(db, username, users[select - 1][0])

                return 1

        # searching and adding user by major
        elif choice == 3:
            major = input("Enter the user's major: ")
            users = fd.searchByMajor(db, major)

            if len(users) == 0:
                print("No user with major {} was found".format(major))
                return -1
            else:
                for x in range(0, len(users)):
                    print("{}. {}".format(x+1, users[x][0]))
                user_choice_to_send_message = input("Would you like to send someone from this list a message? Y/y to accept or anything else to deny.")
                if user_choice_to_send_message == 'Y' or user_choice_to_send_message == 'y':
                    select = input("Select the number coresponding with the user you want to send a message to: ")
                    select = int(select)
                
                    sendMessage(db, username, users[select - 1][0], 'standard')

                return 1



