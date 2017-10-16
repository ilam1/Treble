'''
Irene Lam
SoftDev pd7
K#09: No Treble
10-16-17
'''

import sqlite3   #enable control of an sqlite database
import csv       #facilitates CSV I/O


f="discobandit.db"

db = sqlite3.connect(f) #open if f exists, otherwise create
c = db.cursor()    #facilitate db ops

#==========================================================

#Opens given csv files
peeps_file = csv.DictReader(open("peeps.csv"))
courses_file = csv.DictReader(open("courses.csv"))

#Creates table for peeps.csv
command = "CREATE TABLE peeps (name TEXT, age INTEGER, id INTEGER)"    #SQL statement
c.execute(command)    #run SQL statement
for row in peeps_file:
    #print(row)
    c.execute("INSERT INTO peeps VALUES('" + row["name"] + "', " + row["age"] + ", " + row["id"] + ")")

#Creates table for courses.csv
c.execute("CREATE TABLE courses (code TEXT, mark INTEGER, id INTEGER)")    #run SQL statement
for row in courses_file:
    #print(row)
    c.execute("INSERT INTO courses VALUES('" + row["code"] + "', " + row["mark"] + ", " + row["id"] + ")")

#==========================================================
db.commit() #save changes
db.close()  #close database