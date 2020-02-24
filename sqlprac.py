import sqlite3

conn = sqlite3.connect('wordcountromeodb.sqlite')

curs = conn.cursor()

curs.execute('DROP TABLE IF EXISTS Wordcount')

curs.execute('CREATE TABLE Wordcount (word Text, count Integer)')

fhandle = open('romeo.txt')

wordlist = list()

for line in fhandle:
    wordlist = line.strip().split()
    for word in wordlist:
        curs.execute('SELECT count from Wordcount WHERE word = ?',(word,))
        rows = curs.fetchone()
        if rows is None:
            curs.execute('INSERT INTO Wordcount(word,count) VALUES (?,1)',(word,))
        else:
            curs.execute('UPDATE Wordcount SET count = count + 1 WHERE word = ?',(word,))
        conn.commit()

curs.close()

