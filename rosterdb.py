import sqlite3
import json

con = sqlite3.connect('rosterdb.sqlite3')

curs = con.cursor()

curs.executescript('''DROP TABLE IF EXISTS Users;
             DROP TABLE IF EXISTS Member;
             DROP TABLE IF EXISTS Course''')

curs.execute('''CREATE TABLE Users(
        id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
        name TEXT UNIQUE);''')

curs.execute('''CREATE TABLE Course(
        id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
        course_title TEXT UNIQUE);''')

curs.execute('''CREATE TABLE Member(
        user_id  INTEGER,
        course_id INTEGER,
        role integer,
        PRIMARY KEY (user_id,course_id));''')

fname = 'roster_data.json'
fhandle = open(fname)
data = json.load(fhandle)

for element in data:
    name = element[0]
    course_title = element[1]
    role = element[2]
    
    curs.execute('''INSERT OR IGNORE INTO Users (name)
        VALUES (?)''',(name,))
    curs.execute('SELECT id FROM Users WHERE name = (?)',(name,))
    user_id = curs.fetchone()[0] #curs.fetchone() returns a tuple
    
    curs.execute('''INSERT OR IGNORE INTO Course (course_title)
        VALUES (?)''',(course_title,))
    curs.execute('SELECT id FROM Course WHERE course_title = (?)',(course_title,))
    course_id = curs.fetchone()[0]
    
    curs.execute('''INSERT OR REPLACE INTO Member (user_id,course_id,role) 
        VALUES (?,?,?)''',(user_id,course_id,role)) #REPLACE avoids duplication and respects the UNIQUE requirement
    
    con.commit()
    

