#! /usr/bin/env python3
print('Content-type: text/html\n')

import cgi, re

form = cgi.FieldStorage()

html = """
<!doctype html>
<html>
<head><meta charset="utf-8">
<title>Form in CGI</title></head>
    <body>
	<p>{content}</p>
    </body>
</html>"""

numbers = form.getfirst('numbers', '0')
num_list = re.findall('[\d.]+', numbers)
the_sum = 0
the_prod = 1

for num in num_list:
	the_sum += eval(num)
	the_prod *= eval(num)

op = form.getfirst('operation','mult')
if op == 'add':
    print(html.format(content = "The sum is: " + str(the_sum)))
else:
    print(html.format(content = "The product is: " + str(the_prod)))
