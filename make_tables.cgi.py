#! /usr/bin/env python3

print('Content-type: text/html\n')

import MySQLdb

string = "i211s19_hamsu" 		#change username to yours!!!
password = "my+sql=i211s19_hamsu" 	#change username to yours!!!

db_con = MySQLdb.connect(host="db.soic.indiana.edu", port = 3306, user=string, passwd=password, db=string)
cursor = db_con.cursor()

def makeStudent(cursor):
        try:				#Always surround .execute with a try!
                SQL = "CREATE TABLE Student(StudentID int(11) NOT NULL UNIQUE AUTO_INCREMENT, Name varchar(25) NOT NULL, Major varchar(25) NOT NULL, Email varchar(30), Credits int(11));"
                cursor.execute(SQL))
        except Exception as e:	#Here we handle the error
                print('<p>Something went wrong with the SQL!</p>')
                print(SQL, "Error:", e)
        else:				#This runs if there was no error
                result = "Table Created"
                print(result)
def InsertStudent(cursor, name, major, email, credits):
        try:				#Always surround .execute with a try!
                SQL = "INSERT INTO Student(Name, Major, Email, Credits)"
                SQL += "VALUES('Robert White', 'Informatics', 'robwhy@iu.edu', 18), ('Sam Reynolds', 'Finance', 'samrey@iu.edu', 16), ('Mary Merrium','Accounting', 'marmer@iu.edu', 15); 
                cursor.execute(SQL)
                db_con.commit()
        except Exception as e:	#Here we handle the error
                print('<p>Something went wrong with the SQL!</p>')
                print(SQL, "Error:", e)
        else:				#This runs if there was no error
                result = "Student added"
                print(result)
#main
