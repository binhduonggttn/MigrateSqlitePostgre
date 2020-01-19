import sys
import psycopg2
import sqlite3

# connect  sqlite db
sqliteConnection = sqlite3.connect("testmydb4.db")
sqliteCursor = sqliteConnection.cursor()

# connect to postgresql
pgConnectString = "host='127.0.0.1' dbname='testmydb4' user='postgres' password='1234'"
pgConnection=psycopg2.connect(pgConnectString)
pgCursor = pgConnection.cursor()

sqliteCursor.execute("SELECT * from table1")
rows = sqliteCursor.fetchall()

# loop and insert into postgre
for row in rows:
    sqliteCursor.execute("INSERT INTO table1 VALUES (id)", {"id": row[0]})
    sqliteConnection.commit()

# close all connections
sqliteConnection.close()
pgConnection.close()