#! /usr/bin/env python3
print('Content-type: text/html\n')

import cgi

form = cgi.FieldStorage()   #parses form data

html = """<!doctype html>
<html>
<head><meta charset="utf-8">
<title>Form in CGI</title></head>
    <body>
        <h1>Please enter the two numbers to add.</h1>
        <p>{content}</p>
    </body>
</html>"""

num1 = form.getfirst('num1','0')
num2 = form.getfirst('num2','0')

try:
    print(html.format(content = "The total is " + str(int(num1)+(int(num2)))))
except:
    print("Please enter the two numbers.")
