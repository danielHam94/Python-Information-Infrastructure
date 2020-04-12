#! /usr/bin/env python3
print('Content-type: text/html\n')

import MySQLdb, cgi

string = "i211s19_hamsu" 			#change this to yours
password = "my+sql=i211s19_hamsu"	#change this to yours
db_con = MySQLdb.connect(host="db.soic.indiana.edu", port = 3306, user=string, passwd=password, db=string)
cursor = db_con.cursor()


html = """
<!doctype html>
<html>
<head><meta charset="utf-8">
<title>Robot Delivery System</title></head>
    <body>
    <form action="homework9_2.cgi" method="post">
        <h1>What would you like to have delivered?</h1>
        {content}
        <h2>Cost: $</h2>
        <input type="text" name="cost" /><br />
        <h2>Delivery Method:</h2>
            <br/><input type="radio" name="method" value="drone">Flying Drone ($10)
            <br/><input type="radio" name="method" value="self driving car"/>Self Driving Car ($20)
            <br/><input type="radio" name="method" value="giant robot"/>Giant Robot ($1000)
        <p><button type="submit">Submit</button></p>
    </form>
    </body>
</html>"""

try:
    SQL = "SELECT DISTINCT Item from Items;"
    cursor.execute(SQL)
    results = cursor.fetchall()
    
except Exception as e:
    print('<p>Something went wrong with the SQL!</p>')
    print(SQL)
    print("\nError:", e)

else:
    button = ""
    for item in results:
        button += "<p><input type = 'radio' name = 'item' value = '"+item[0]+"'>"+ item[0]+"</p>"
    print(html.format(content = button))


    

