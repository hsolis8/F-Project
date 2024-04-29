import sqlite3

conn = sqlite3.connect('example1.db')
c = conn.cursor()
c.execute("CREATE TABLE bank_account(Id integer primary key, Pin integer, Name text, Balance integer)")
conn.commit()

c.execute("INSERT INTO bank_account(Pin, Name, Balance) VALUES (313, 333, 'Heidi', 10309)")
conn.commit()
conn.close()

#c.execute("INSERT INTO bank_account(Id, Pin, Name, Balance) VALUES (202544, 333, 'Heidi', 10309)")
#conn.commit()
#c.execute()
#conn.commit()
#Querying from Data

#c.execute("SELECT * FROM bank_account")
#conn.commit()
#print(c.fetchall())

#c.execute("SELECT Name, Pin FROM bank_account")
#conn.commit()
#print(c.fetchall())

#testQuery = 'SELECT * FROM bank_account'
#cursor.execute(testQuery)

#conn.close()