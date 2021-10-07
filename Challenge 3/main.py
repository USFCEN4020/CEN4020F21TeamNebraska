#Team Nebraska
#Epic 3

# Database used
import sqlite3

from package import dbRead as rd
from package import dbWrite as wr
from package import menu as menu

# Connection object represents
# the database
conn = sqlite3.connect('inCollege1.db')

# Cursor object to perform
# SQL commands
cursor = conn.cursor()

db = (cursor, conn)

# Create user table
cursor.execute('''CREATE TABLE IF NOT EXISTS users
            (username text, password text, fname text, lname text, lan text)''')
cursor.execute('''CREATE TABLE IF NOT EXISTS jobs
            (username text, title text, description text, employer text, location text, salary text)''')
cursor.execute('''CREATE TABLE IF NOT EXISTS userFunction
            (username text, email bool, sms bool, targetAD bool)''')
cursor.execute('''CREATE TABLE IF NOT EXISTS userProfile
            (username text, email bool, sms bool, targetAD bool)''')


menu.mainMenu(db)
