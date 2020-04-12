#! /usr/bin/env python3
import cgitb
cgitb.enable()
print('Content-type: text/html\n')

text = """<!doctype html>
<html>
    <head><meta charset="utf-8">
	<title>Tables in CGI</title></head>
    <body><h1>Your table should look like this:</h1>
        <table border=1>
	{content}
	</table>
    </body>
</html>"""

table=""
for i in range(10):
    table += "<tr>"
    for j in range(10):
        table += "<td>Row " + str(i+1) + ", Col " + str(j+1) + "</td>"
    table += "</tr>"

print(text.format(content=table))
