import sqlite3

#connect to SQLite database
conn = sqlite3.connect('geeks2.db')
cursor = conn.cursor()

#Create table
cursor.execute("""CREATE TABLE IF NOT EXISTS STUDENT(NAME VARCHAR(255), CLASS VARCHAR(255), SECTION VARCHAR(255))""")

#insert data into the table
cursor.execute("INSERT INTO STUDENT VALUES ('Raju', '7th', 'A')")
cursor.execute("INSERT INTO STUDENT VALUES ('Shyam', '8th', 'B')")
cursor.execute("INSERT INTO STUDENT VALUES ('Baburao', '9th', 'C')")

#display inserted data
print("Data inserted in the table:")
cursor.execute("SELECT * FROM STUDENT")
for row in cursor.fetchall():
    print(row)

#commit changes and close connection
conn.commit()
conn.close()