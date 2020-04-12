#! /usr/bin/env python3


print('Content-type: text/html\n')

import MySQLdb, cgi

string = "i211s19_hamsu" 			#change this to yours
password = "my+sql=i211s19_hamsu"	#change this to yours
db_con = MySQLdb.connect(host="db.soic.indiana.edu", port = 3306, user=string, passwd=password, db=string)
cursor = db_con.cursor()
form = cgi.FieldStorage()

##I attempted to try and make the web to go running but it wouldnt
##fid=form.getfirst("fid","0")

##html = """
##<!doctype html>
##<html>
##<head>
##<meta charset="utf-8">
##<title>Purchased Records</title>
##</head>
##<body>
##    <form action = "TuneShop.cgi" method="get">
##    <input type = "hidden"name="fid" value="{fid}" />
##    <h1> Purchased Records </h1>
##    <table width="400" border="1">
##    <tr><th>Song</th><th>Purchased Times</th></tr>
##    {content}
##    </table>
##</form>
##</body>
##</html>"""

html = """
<!doctype html>
<html>
<head>
<meta charset="utf-8">
<title>Purchased Records</title>
</head>
<body>
    <h1> Purchased Records </h1>
    <table width="400" border="1">
    <tr><th>Song</th><th>Purchased Times</th></tr>
    <tr><td>Chandelier></td><td>0</td></tr><tr><td>Happier</td><td>0</td></tr>
    </table>
</form>
</body>
</html>"""
##try:
##    SQL = "SELECT Song, COUNT(SongID) FROM Songs"
##    SQL += "WHERE FacultyID = " + fid + ";"
##    cursor.execute(SQL)
##    results = cursor.fetchone()
##except:
##    print('<p>Something went wrong with the SQL!</p>')
##    print(SQL)
##    print("\nError:", e)
##else:
##    print(html.format(fid = fid)

print(html)
