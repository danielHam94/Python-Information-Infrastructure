#! /usr/bin/env python

import cgi
import random

print('Content-type: text/html\n')

import MySQLdb

    cursor.execute(SQL)

string = "i211s16_hamsu"
password = "my+sql=i211s16_hamsu"

db_con = MySQLdb.connect(host="db.soic.indiana.edu", port = 3306, user=string, passwd=password, db=string)
cursor = db_con.cursor()

form = cgi.FieldStorage()
didFight = form.getfirst('didFight',True)

if didFight == True:
    print("did fight")
else:
    html = """
    <html>
        <head>
        <title>Robot Fight!</title>
        </head>
         <body>
                <H1>Choose two robots to face off!</H1><hr />
                <FORM method="post" action="robot_fight.cgi">
                <H3>Please select robots:</H3>
                <p> Robot Name:
                    <select name="robot1">
                        {options}
                    </select>
                    <select name="robot2">
                        {optionsSecond}
                    </select>
                </p>
        <input type="submit" value="Fight!" />
        </FORM>
        <hr /></body>
    </html>"""

    cursor.execute("SELECT * FROM Robots;")
    results = cursor.fetchall()

    optionsStringHTML = ""
    for row in results:
        optionsStringHTML+="<option value='"+row[1]+"'>"+row[1]+"</option>"

    print(html.format(options = optionsStringHTML, optionsSecond = optionsStringHTML))
