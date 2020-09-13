"""
#!/usr/bin/python
__author__ = 'kilroy'
#  (c) 2014, WasHere Consulting, Inc.
#  Written for Infinite Skills

import MySQLdb

try:
    db = MySQLdb.connect(host="localhost", user="root", passwd="barrister!", db="kai_testdb")

    curs = db.cursor()

    curs.execute("select * from employees")

    for row in curs.fetchall():
        print("Name: %s, Grade: %s" % (row[1], row[2]))

except Exception as e:
    print(e)
"""

import pyodbc 
# Some other example server values are
# server = 'localhost\sqlexpress' # for a named instance
# server = 'myserver,port' # to specify an alternate port
server = 'LENOVO-PC\SQL' 
database = 'TRAINING' 
username = "Lenovo-PC\\User"
password = '' 
cnxn = pyodbc.connect(Trusted_Connection='Yes',
						Driver='{ODBC Driver 17 for SQL Server}',
						Server=server,
						DATABASE=database)
#UID='+username+';PWD='+ password)
cursor = cnxn.cursor()

cursor.execute("SELECT @@version;") 
row = cursor.fetchone() 
while row: 
    print(row[0])
    row = cursor.fetchone()
	
	

