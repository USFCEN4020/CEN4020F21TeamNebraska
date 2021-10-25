# commit a job
def commitJob(userName, db, title, description, employer, location, salary):
    # counter to limit
    # number of accounts
    count = 1
    # count no. of users
    for i in db[0].execute('SELECT * FROM jobs'):
        count += 1
    if (count > 10):
        print("All permitted Jobs Have been created")
        return 1
    else:
        db[0].execute("INSERT INTO jobs VALUES (?,?,?,?,?,?)",(userName, title,description, employer, location, salary))
        db[1].commit()
        print("Job", title, "posted successfully!")


# post a job
def postJob(db, userName):
    print("\nEnter 'cancel' at any time to cancel.\n")
    title = input("Enter job title: ")
    if(title=='cancel'):
        print("Returning to main menu.")
        return
    description = input("Enter job description: ")
    if(description=='cancel'):
        print("Returning to main menu.")
        return
    employer = input("Enter job employer: ")
    if(employer=='cancel'):
        print("Returning to main menu.")
        return
    location = input("Enter job location: ")
    if(location=='cancel'):
        print("Returning to main menu.")
        return
    salary = input("Enter job salary (in USD please): ")
    if(salary=='cancel'):
        print("Returning to main menu.")
        return
    commitJob(userName, db, title, description, employer, location, salary)


# delete a job
def deleteJob(db, username, employer, title):
    jobs = []
    
    # getting all the jobs this user has created
    db[0].execute('SELECT title, employer FROM jobs WHERE username=?', (username,))
    jobs.append(db[0].fetchall())

    # seeing if the job exists
    if len(jobs[0]) == 0:
        print("Either the job doesn't exist or you do not have permission to delete it")
        return
    
    # checking to see if the titles and employers match match
    for x in jobs[0]:
        if x[0] == title and x[1] == employer:
            db[0].execute('DELETE FROM jobs WHERE username=? AND title=? AND employer=?', (username, title, employer))
            db[1].commit()
            print("job has been delete")

            # potentionaly send canidids a message

# print all jobs
def printJobs(db, username):
    jobs = []

    # getting all jobs
    db[0].execute('SELECT * FROM jobs')
    jobs.append(db[0].fetchall())

    # formating and printing jobs
    jobCount = 0
    for x in jobs[0]:
        jobCount += 1

        print("1. Title:       {}".format(x[1]))
        print("   Description: {}".format(x[2]))
        print("   Employer:    {}".format(x[3]))
        print("   Location:    {}".format(x[4]))
        print("   Salary:      {}".format(x[5]))

    # options to save or apply for job
    choice = input('\nEnter corresponding job number for more options or exit to leave')
    if choice == "exit":
        return
    
    if choice >= 1 and choice <= 10:
        option = input("Enter 1 to apply for job, 2 to save job, or anything else to leave")

        if option == 1:
            # apply for job
            if username == jobs[0][choice -1][0]:
                print("you can not apply for a job you posted")
                return

            ##
            ##  apply for job function call here
            ##
        
        if option == 2:
            # save job
            db[0].execute("INSERT INTO savedJobs VALUES (?,?, ?)",(username, jobs[0][choice -1][3], jobs[0][choice -1][1]))
            db[1].commit()
            return

        print("Leaving ... ")
        return


# job search basically main function for job
def jobSearch(db, isLoggedIn, userName):
    y = 0
    if (isLoggedIn == 0):
        print("Please log in to access job search and posting.")
        input("Press enter to return to the main menu.")
        return
    else:
        while (y != 9):
            print("\nWelcome to the jobs tab!\n")
            print("1. Show all Jobs")
            print("2. Post a new job")
            print("3. Delete a job")
            command = input("Choose an available option, or enter 9 to exit.")

            if y == 2:
                postJob(db, userName)
                print()
            
            if y == 3:
                title = input("Enter the title of the job you want to delete")
                employer = input("Enter the employer of the job you want to delete")
                deleteJob(db, userName, title, employer)
                print()
            
            else:
                return

    return