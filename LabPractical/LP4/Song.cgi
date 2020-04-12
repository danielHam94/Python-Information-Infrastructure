#! /usr/bin/env python3

print('Content-type: text/html\n')

import MySQLdb, cgi

string = "i211s19_hamsu" 			#change this to yours
password = "my+sql=i211s19_hamsu"	#change this to yours
db_con = MySQLdb.connect(host="db.soic.indiana.edu", port = 3306, user=string, passwd=password, db=string)
cursor = db_con.cursor()
form = cgi.FieldStorage()



html = """
<!doctype html>
<html>
<head>
<meta charset="utf-8">
<title>Song Purchased</title>
</head>

<body>
<form action="ViewPurchased.cgi" method="post">
    
    
    <p1> Thank you for purchasing {songname} for {price}.  </p1>
    <br></br>
    <h2> View My Songs By </h2>
    <input type="radio" name="sortby" value="title"> Title
    <input type="radio" name="sortby" value="artist"> Artist
    <input type="radio" name="sortby" value="genre"> Genre
    <p><button type="submit">View Songs</button></p>
    


</form>
</body>
</html>"""
try:
    SQL = "INSERT INTO MyTunes(SongID)"
    SQL+="VALUES('"+songID"');"
    cursor.execute(SQL)
    db_con.commit()

except:
    print ('<p>Something went wrong with the SQL!</p>')
    print (SQL)
    print ("\nError:", e)
else:
    print(results)   


