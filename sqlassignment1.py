import sqlite3

conn = sqlite3.connect('orgs.sqlite')

curs = conn.cursor()

curs.execute('DROP TABLE IF EXISTS Counts')

curs.execute('CREATE TABLE Counts (org Text, count Integer)')

#url = "https://www.py4e.com/code3/mbox.txt"
#fhandle = urllib.request.urlopen(url)
fname = input('Enter file: ')
fhandle = open(fname)
wordlist = list()
for line in fhandle:
    if line.startswith('From:'):
        wordlist = line.split()
        org = wordlist[1].split('@')[1]
        curs.execute('SELECT count from Counts WHERE org = ?',(org,))
        row = curs.fetchone()
        if row is None:
            curs.execute('INSERT INTO Counts(org,count) VALUES (?,1)',(org,))
        else:
            curs.execute('UPDATE Counts SET count = count + 1 WHERE org = ?',(org,))
        conn.commit()

sqlstr = curs.execute('SELECT * FROM Counts ORDER by count')

for row in sqlstr:
    print(str(row[0]),row[1])
    
curs.close()