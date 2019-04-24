import time
import csv
import sqlite3
db_connection = sqlite3.connect('./test.db')
# db_connection.execute('CREATE TABLE ok (id int , name text, age int)')
# db_connection.executemany('INSERT INTO ok VALUES(?,?,?)',[(8,'中国',4),(44,'上海',5)])
# db_connection.commit()
data = db_connection.execute('SELECT * FROM ok').fetchall()
print(data)
with open('csvfiles.csv','w',newline='') as f:
    writer = csv.writer(f,dialect='excel')
    writer.writerows(data)