import time
from datetime import datetime

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
        dt_object = datetime.fromtimestamp(time.time())
        db[0].execute("INSERT INTO jobs VALUES (?,?,?,?,?,?)",(userName, title,description, employer, location, salary, dt_object))
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

        # apply for job
        if option == 1:
            if username == jobs[0][choice -1][0]:
                print("you can not apply for a job you posted")
                return

            # check to see if user has already applied for this job
            applied = []
            db[0].execute("SELECT * FROM appliedFor WHERE username=? AND employer=? AND title=?",
                         (username, jobs[0][choice - 1][3], jobs[0][choice - 1][1]))
            applied.append(db[0].fetchall())
            if len(applied[0]) != 0:
                print("You have already applied to this job")
                return 

            # additional user application info
            graduateDate = input("Enter your graduation date as ('mm/dd/yyyy'): ")
            startDate = input("Enter the date you can start working as ('mm/dd/yyyy'): ")
            reason = input("Enter why you would be a good fit for this job: ")
            whyThis = input("Why did you pick this job: ")

            # aading to the databse
            dt_object = datetime.fromtimestamp(time.time())
            db[0].execute("INSERT INTO appliedFor VALUES (?,?,?,?,?,?,?)", 
                         (username, jobs[0][choice - 1][3], jobs[0][choice - 1][1], graduateDate, startDate, reason, whyThis, dt_object))
            db[1].commit()
            
            print("You have successfully applied to the job.")
            return
        
        # save job
        if option == 2:
            db[0].execute("INSERT INTO savedJobs VALUES (?,?,?)",(username, jobs[0][choice -1][3], jobs[0][choice -1][1]))
            db[1].commit()
            return

        print("Leaving ... ")
        return


def showApplied(db, username):
    applied = []
    db[0].execute("SELECT * FROM appliedFor WHERE username=?", (username))
    applied.append(db[0].fetchall())

    print("Your applied jobs: \n")
    for x in applied[0]:
        print("employer: ", x[1])
        print("title: ", x[2])
        print()
    return len(applied)


def showNotApplied(db, username):
    applied = []
    db[0].execute("SELECT * FROM appliedFor WHERE username=?", (username))
    applied.append(db[0].fetchall())
    
    appliedJobs = []
    for x in applied[0]:
        appliedJobs.append((x[1], x[2]))  # applied job's employer, title

    jobs = []
    db[0].execute("SELECT * FROM jobs")
    jobs.append(db[0].fetchall())
    
    AllJobs = []
    for x in jobs[0]:
        AllJobs.append((x[1], x[2]))  # all job's employer title

    NotApplied = [i for i in AllJobs if i not in appliedJobs]
    print("Your not applied jobs: \n")
    for x in NotApplied:
        print("employer: ", x[1])
        print("title: ", x[2])
        print()


# not sure the reasons for these or how to implement them into the function

#def saveJob(db, username, choice):
#    find_job = "SELECT * FROM jobs"
#    cursor.execute(find_job)
#    results = cursor.fetchall()
#
#    choice1 = integer_in_range("\nDo you want to save this job to your list?"
#                               " 1. Save the job"
#                               " 2. Back to main menu ", 1, 2, "NULL")
#    if choice1 == 1:
#        find_savedjob = "SELECT * FROM applyInfo WHERE username = ? AND title = ? AND status ='saved'"
#        cursor.execute(find_savedjob, [(username), (results[choice - 1][1])])
#        st = cursor.fetchall()
#        if len(st) > 0:
#            print("You have already saved it")
#        else:
#            cursor.execute(
#                """
#            INSERT INTO applyInfo (username, title, status) VALUES(?,?,'saved')""",
#                (username, results[choice - 1][2]),
#            )
#            db.commit()
#            print("The job is saved!")

#def unsaveJob(username):
#
#    choice2 = integer_in_range("\nDo you want to unsave any job in your list?"
#                               " 1. Unsave the job"
#                               " 2. Back to main menu ", 1, 2, "NULL")
#    if choice2 == 1:
#        title1 = (single_line_string("Enter your Title you want to unsave: ")).title()
#
#        delete_save = "DELETE FROM applyInfo WHERE username = ? AND title = ? AND status = 'saved'"
#        cursor.execute(delete_save, [(username), (title1)])
#        db.commit()
#
#        print("this job has been unsaved")
#        db.close()


# job search basically main function for job
def jobSearch(db, isLoggedIn, username):
    y = 0
    num_of_jobs = showApplied(db, username)
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
            print("4. Show applied jobs")
            print("5. Show jobs have not been applied")
            print("6. Show saved jobs")
            print("You have applied for: ", num_of_jobs, " number of jobs.")
            # user option
            y = input("Choose an available option, or enter 9 to exit.")

            # print all jobs
            if y == 1:
   	    	    printJobs(db, username)
            
            # post a new job
            if y == 2:
                postJob(db, username)
                print()
            
            # delete a job
            if y == 3:
                title = input("Enter the title of the job you want to delete")
                employer = input("Enter the employer of the job you want to delete")
                deleteJob(db, username, title, employer)
                print()
            
            # shows jobs you have applied for
            if y == 4:
                showApplied(db, username)
            
            # shows jobs you have not applied for yet
            if y == 5:
                showNotApplied(db, username)

            # shows saved jobs
            if y == 6:
                saved = []
                db[0].execute("SELECT * FROM savedJobs WHERE username=?", (username))
                saved.append(db[0].fetchall())

                print("Your applied jobs: \n")
                for x in saved[0]:
                    print("employer: ", saved[1])
                    print("title: ", saved[2])
                    print()

# Check for deleted jobs
def isDeleted(db, userName) :
    applied = []
    db[0].execute("SELECT * FROM appliedFor WHERE username=?", (userName))
    applied.append(db[0].fetchall())
    for x in applied[0]:
        db[0].execute("SELECT * FROM appliedFor WHERE username=? AND employer=?", (userName, x[1]))
        temp_data = db[0].fetchall()
        if len(temp_data) == 0:
            print("The job: ", x[2], " that you applied for has been deleted!")

# Search for new posted jobs
def isNewJob(db, userName) :
    jobs = []
    db[0].execute("SELECT * FROM jobs")
    jobs.append(db[0].fetchall())
    for x in jobs[0] :
        cur_time = time.time()
        # 86400 seconds in a day
        # A job is considered new if it was posted within a day
        prev = datetime.timestamp(x[6])
        if (cur_time - prev <= 86400) :
            print("A new job has been posted! Go to job search tab to check it out.")
    return

# Check if applied for a job recently
def hasAppliedRecently(db, userName) :
    applied = []
    db[0].execute("SELECT * FROM appliedFor WHERE username=?", (userName))
    applied.append(db[0].fetchall())
    max_time = 0
    for x in applied[0] :
        if (x[0] == userName) :
            # find latest time applied
            if (x[7] > max_time) :
                max_time = x[7]

    # 604800 seconds in 7 days
    cur_time = time.time()
    if (cur_time - max_time > 604800) :
        print("You haven't applied for a job in 7 days!")
    return