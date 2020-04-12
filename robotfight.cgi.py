#! /usr/bin/env python3

print('Content-type: text/html\n')

import cgi
import random
import MySQLdb

string = "i211s19_hamsu" 			#change this to yours
password = "my+sql=i211s19_hamsu"	#change this to yours
db_con = MySQLdb.connect(host="db.soic.indiana.edu", port = 3306, user=string, passwd=password, db=string)
cursor = db_con.cursor()

def getWeapon(cursor, winner):
    try:
        SQL = "SELECT Weapon from Robot where Name = '"+winner+"';"
        cursor.execute(SQL)
        weapon=cursor.fetchall

html = """
<html>
    <head><title>Robot Fight!</title></head>
    <body>
        <H1>Choose two robots to face off!</H1><hr />
        <FORM method = "post" action = "robot_fight.cgi">
        <H3>Please select robots:</H3>
        <p>Robot Name:
        <select name = "robot1"><option>BB-*</option><option>Megatron</option><option>Commander Data</option><option>Terminator</option><option>Roomba</option></select><select name="robot2"><option>BB-8</option><option>Megatron</option><option>Commander Data</option><option>Terminator</option><option>Roomba</option></select></p>
    <input type = "submit" value = "Fight!" />
    </FORM>
    <hr />
    </body>
</html>"""

try:					#Always surround .execute with a try!
        SQL = "SELECT * FROM Robots;"
        cursor.execute(SQL)
        results = cursor.fetchall()
except Exception as e:		#Here we handle the error
        print('<p>Something went wrong with the SQL!</p>')
        print(SQL, "\nError:", e)
else:				#This runs if there was no error
        result = ""
        for row in results:
            result+="<tr>"
            for i in row:
                result += "<td>"+str(i)+"</td>"
            result+="</tr>"
        print(html.format(content=result))
print(html.format(content = table))
