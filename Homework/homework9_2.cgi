#! /usr/bin/env python3
print('Content-type: text/html\n')

import MySQLdb, cgi

#establish DB connection
string = "i211s19_hamsu" 	#change this to yours
password = "my+sql=i211s19_hamsu"	#change this to yours
db_con = MySQLdb.connect(host="db.soic.indiana.edu", port = 3306, user=string, passwd=password, db=string)
cursor = db_con.cursor()

form = cgi.FieldStorage()

item = form.getfirst("item", "laptop")
method = form.getfirst("method", "drone")
cost = form.getfirst("cost", "0")

if method == "drone":
    add_cost = 10
elif method == "self driving car":
    add_cost = 20
else:
    add_cost = 1000

total = str(eval(cost) + add_cost)

def results_table(records, item, cost, method): 
    html = """<!doctype html>
    <html>
    <head><meta charset="utf-8">
    <title>Robot Delivery</title>
    </head>
        <body>
            <h1>Robot Delivery System Confirmation</h1>
            <p>You have selected to have a {item} delivered by {method}.</p>
            <p>Your total comes to ${total}</p>
            <h2>Delivery Records</h2>
            <table border='1' width='100%'>
            <tr><th>DeliveryID</th><th>Item</th><th>Cost</th><th>Method</th><th>Shipping</th></tr>
            {content}
            </table>
            <p><a href="homework9_1.cgi">Go Back</a></p>
        </body>
    </html>"""

    table = ""
    for row in records:
            table += "<tr>"
            for item in row:
                table += "<td  align='center'>"+str(item)+"</td>"
            table += "</tr>"
    print(html.format(content = table, item = item, method = method, total = total))

try:
    SQL = "INSERT INTO Deliveries(Item, Cost, Method, Shipping)"
    SQL += "VALUES('"+item+"',"+str(cost)+",'"+method+"',"+str(total)+");"
    cursor.execute(SQL)
    db_con.commit()
    
    SQL = "SELECT * FROM Deliveries;"
    cursor.execute(SQL)
    results = cursor.fetchall()
    
except Exception as e:
    print('<p>Something went wrong with the SQL!</p>')
    print(SQL)
    print("\nError:", e)
else:
    results_table(results, item, cost, method)


