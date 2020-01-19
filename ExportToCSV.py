import sqlite3
import csv
from sqlite3 import Error
import os

try:

  # Connect to database
  conn=sqlite3.connect('testmydb1.db')

 # Export data into CSV file
  cursor = conn.cursor()
  cursor.execute('''select * from testmydb1."table2"''')
  with open("file.csv", "w") as csv_file:
      csv_writer = csv.writer(csv_file, delimiter="\t")
      csv_writer.writerow([i[0] for i in cursor.description])
      csv_writer.writerows(cursor)

  dirpath = os.getcwd() + "/file.csv"
  print("Data exported Successfully into {}".format(dirpath))

except Error as e:
  print(e)

# Close database connection
finally:
  conn.close()