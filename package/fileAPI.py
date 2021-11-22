import os
from package import dbWrite as wr
import datetime, time, math
from datetime import datetime as dt


def createAccount(db):
    if os.path.exists('resources/studentAccounts.txt'):
        file = open('resources/studentAccounts.txt')
        lines = file.readlines()
        data = []
        for index, line in enumerate(lines):
            if index > 30:
                break
            if index % 3 != 2:
                data.append(line.strip('\n'))
            else:
                data[0] = data[0].split(' ')
                # print(data)
                db[0].execute('SELECT * FROM users WHERE username=?', (data[0][0],))
                userinfo = db[0].fetchall()
                if len(userinfo) == 0:
                    wr.insertUser(db, data[0][0], data[1], data[0][1], data[0][2], 1, 'standard',
                                  datetime.datetime.fromtimestamp(math.floor(time.time())))
                data = []


def creatJobs(db):
    if os.path.exists('resources/newJobs.txt'):
        file = open('resources/newJobs.txt')
        lines = file.readlines()
        count = 0
        data = ['', '', '', '', '', '']
        for line in lines:
            if count > 70:
                break
            if count % 7 != 6:
                data[count % 7] += line.strip('\n')
                data[count % 7] = data[count % 7].strip('&')
            else:
                # print(data)
                db[0].execute('SELECT * FROM jobs WHERE title=?', (data[0],))
                jobinfo = db[0].fetchall()
                if len(jobinfo) == 0:
                    wr.insertJobs(db, data[2], data[0], data[1], data[3], data[4], data[5], dt.now())
                data = ['', '', '', '', '', '']
            count += count % 7 != 1 or "&&&" in line


def creatTrain():
    if os.path.exists('resources/newtraining.txt'):
        file = open('resources/newtraining.txt')
        lines = file.readlines()
        returnable = [line.strip('\n') for line in lines]
        # print(returnable)
        return returnable
    else:
        return []


def printJobs(db):
    db[0].execute('SELECT * FROM jobs')
    jobs = db[0].fetchall()
    file = open('resources/MyCollege_jobs.txt', 'w')
    for job in jobs:
        for item in job:
            file.write(item + '\n')
        file.write('=====\n')


def printProfiles(db):
    db[0].execute('SELECT * FROM userProfile')
    users = db[0].fetchall()
    file = open('resources/MyCollege_profiles.txt', 'w')
    for user in users:
        username = user[0]
        printable = []
        for i in range(4):
            printable.append(user[i + 1])

        db[0].execute('SELECT description FROM userExperience WHERE username=?', (username,))
        experiences = db[0].fetchall()
        experiences = [i[0] for i in experiences]
        printable.extend(experiences)

        db[0].execute('SELECT schoolname FROM userEducation WHERE username=?', (username,))
        educations = db[0].fetchall()
        educations = [i[0] for i in educations]
        printable.extend(educations)

        for item in printable:
            file.write(item + '\n')
        file.write('=====\n')


def printUsers(db):
    db[0].execute('SELECT username,tier FROM users')
    users = db[0].fetchall()
    file = open('resources/MyCollege_users.txt', 'w')
    for user in users:
        file.write(user[0] + " " + user[1] + '\n')


def printTraining(db):
    db[0].execute('SELECT username FROM users')
    users = db[0].fetchall()
    db[0].execute('SELECT username,courseName FROM learningbhm')
    courses = db[0].fetchall()
    file = open('resources/MyCollege_training.txt', 'w')

    for i in range(len(users)):

        for j in range(len(courses)):
            if (users[i][0] == courses[j][0]):
                file.write(users[i][0] + " " + courses[j][1] + "\n====\n")
            else:
                file.write(users[i][0] + " None\n====\n")


def printappliedJobs(db):
    db[0].execute('SELECT title FROM jobs')
    jobTitles = db[0].fetchall()
    db[0].execute('SELECT title,username,whyU FROM appliedFor')
    applied = db[0].fetchall()
    file = open('resources/MyCollege_appliedJobs.txt', 'w')
    for i in range(len(jobTitles)):

        for j in range(len(applied)):
            if (jobTitles[i][0] == applied[j][0]):
                file.write( jobTitles[i][0] + "\n" + applied[j][1] +"\n" + applied[j][2] +"\n====\n")#shouldnt be printing twice
            else:
                file.write( jobTitles[i][0] + " None applied\n====\n")#shouldnt be printing twice

def printSavedJobs(db):
    db[0].execute('SELECT username,title FROM savedJobs')
    saved = db[0].fetchall()
    file = open('resources/MyCollege_savedJobs.txt', 'w')
    for save in saved:
        file.write(save[0] +" " + save[1] + "\n====\n")



