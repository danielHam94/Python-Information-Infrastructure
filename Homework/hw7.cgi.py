import cgi

form = cgi.FieldStorage()

html = """<!doctype html>
<html>
<head><meta charset="utf-8">
<title>Robot Delivery System Confirmation</title>
</head>
    <body>
        <h1>Robot Delivery System Confirmation</h1>
        <p>You have selected to have a {item} delivered by {method}.</p>
        <p>Your total comes to ${total}.</p>
    </body>
</html>"""

item = form.getfirst("item", "unknown item")
method = form.getfirst("method", "drone")
cost = form.getfirst("cost","0")

if method == "drone":
    add_cost = 10
elif method == "self driving car":
    add_cost = 20
else:
    add_cost = 1000

total = str(eval(cost) + add_cost)

print(html.format(item = item, method = method, total = total))
