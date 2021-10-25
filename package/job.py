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
	    graduateDate = single_line_string("Enter the graduation date: ")
            startDate = single_line_string("Enter the date you can start working: ")
            reason = mutli_line_string("Enter why you would be a good fit for this job: ")

            cursor.execute(
                """
            INSERT INTO applyInfo (username, title, graduateDate, startDate, reason, status) VALUES(?,?,?,?,?,'applied')""",
                (username, number[choice - 1][2], graduateDate, startDate, reason),
            )
            db.commit()
            print("Your applied jobs info has been created.")
            db.close()
        
        if option == 2:
            # save job
            db[0].execute("INSERT INTO savedJobs VALUES (?,?, ?)",(username, jobs[0][choice -1][3], jobs[0][choice -1][1]))
            db[1].commit()
            return

        print("Leaving ... ")
        return


# job search basically main function for job
def jobSearch(db, isLoggedIn, username):
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
	    print("4. Show applied jobs")
	    print("5. Show jobs have not been applied")
	    print("6. Show saved jobs")
	    
            command = input("Choose an available option, or enter 9 to exit.")

	    if y == 1:
   	    	printJobs(db, username)
            if y == 2:
                postJob(db, username)
                print()
            
            if y == 3:
                title = input("Enter the title of the job you want to delete")
                employer = input("Enter the employer of the job you want to delete")
                deleteJob(db, username, title, employer)
                print()
	    if y == 4
		find_JobsApplied = "SELECT * FROM applyInfo WHERE username = ? AND status = 'applied'"
    		cursor.execute(find_JobsApplied, [(username)])
    		results = cursor.fetchall()

    		print("Your applied jobs: \n")
    		for applied in results:
        	print("title: ", applied[1])
        
	    if y == 5
		find_JobsApplied = "SELECT * FROM applyInfo WHERE username = ? AND status = 'applied'"
    		cursor.execute(find_JobsApplied, [(username)])
   		results = cursor.fetchall()
   		AppliedJobs = []
    		for applied in results:
        		AppliedJobs.append(applied[1])  # applied job's title

    		cursor.execute("SELECT * FROM jobs")
    		job_results = cursor.fetchall()
    		AllJobs = []
    		for each in job_results:
        		AllJobs.append(each[2])  # all jobs' title

    		# NotApplied = []
    		#NotApplied = list(set(AppliedJobs).difference(set(AllJobs)))  # difference AppliedJobs
   	 	NotApplied = [i for i in AllJobs if i not in AppliedJobs]
    		print("Your not applied jobs: \n")
    		for x in NotApplied:
        		print("title: ", x)
		
	    if y == 6
		find_JobsSaved = "SELECT * FROM applyInfo WHERE username = ? AND status = 'saved'"
    		cursor.execute(find_JobsSaved, [(username)])
    		results = cursor.fetchall()

    		if len(results) > 0:
        		print("Your saved jobs: \n")
        		for saved in results:
            		print("title: ", saved[1])
            		unsaveJob(username)
    		else:
        		print("You haven't save any job!")
	else:
                return

    return

def saveJob(db, username, choice):

    find_job = "SELECT * FROM jobs"
    cursor.execute(find_job)
    results = cursor.fetchall()

    choice1 = integer_in_range("\nDo you want to save this job to your list?"
                               " 1. Save the job"
                               " 2. Back to main menu ", 1, 2, "NULL")
    if choice1 == 1:
        find_savedjob = "SELECT * FROM applyInfo WHERE username = ? AND title = ? AND status ='saved'"
        cursor.execute(find_savedjob, [(username), (results[choice - 1][1])])
        st = cursor.fetchall()
        if len(st) > 0:
            print("You have already saved it")
        else:
            cursor.execute(
                """
            INSERT INTO applyInfo (username, title, status) VALUES(?,?,'saved')""",
                (username, results[choice - 1][2]),
            )
            db.commit()
            print("The job is saved!")

def unsaveJob(username):

    choice2 = integer_in_range("\nDo you want to unsave any job in your list?"
                               " 1. Unsave the job"
                               " 2. Back to main menu ", 1, 2, "NULL")
    if choice2 == 1:
        title1 = (single_line_string("Enter your Title you want to unsave: ")).title()

        delete_save = "DELETE FROM applyInfo WHERE username = ? AND title = ? AND status = 'saved'"
        cursor.execute(delete_save, [(username), (title1)])
        db.commit()

        print("this job has been unsaved")
        db.close()

