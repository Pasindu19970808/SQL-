import sqlite3

#creates a file
conn = sqlite3.connect('emaildb.sqlite')
#This is like our handle from python on the database
cur = conn.cursor()

cur.execute('DROP TABLE IF EXISTS Counts')

cur.execute('''CREATE TABLE Counts (email Text, count Integer)''')

fname = input('File Name: ')

if (len(fname) < 1):
    fname = 'words.txt'
fhandle = open(fname)
for line in fhandle:
        if line.startswith('From:') is True:
            #count = count + 1
            linewords = line.split()
            email = linewords[1]
            cur.execute('SELECT count from COUNTS where email = ?',(email,))
            #if there are no record that meet the above statement, row is None
            row = cur.fetchone()
            if row is None:
                cur.execute('INSERT INTO COUNTS(email,count) VALUES (?,1)',(email,))
            else:
                cur.execute('UPDATE Counts SET count = count + 1 where email = ?',(email,))
            conn.commit()

sqlstr = "SELECT * FROM Counts ORDER by count DESC LIMIT 10"

for row in cur.execute(sqlstr):
    print(str(row[0]),row[1])
    
cur.close()
