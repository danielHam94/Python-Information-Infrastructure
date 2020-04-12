#! /usr/bin/env python3

import cgi, random

print('Content-type: text/html\n')

options = ["Paper", "Rock", "Scissors"]

images = {"Paper": "http://images.clipartpanda.com/writing-on-paper-clipart-black-and-white-1206556249326967385nexxuz_Loose_Leaf_Paper.svg", "Rock": "http://icons.iconarchive.com/icons/raindropmemory/down-to-earth/256/G12-Rock-icon.png", "Scissors": "http://icons.iconarchive.com/icons/custom-icon-design/pretty-office-10/512/Scissors-icon.png"}

choice = random.choice(options)

form = cgi.FieldStorage()
user_choice = form.getfirst('symbol', 'Rock')

if user_choice == choice:
	status = "Tie"
elif (user_choice == "Rock" and choice == "Scissors") or (user_choice == "Paper" and choice == "Rock") or \
     (user_choice == "Scissors" and choice == "Paper"):
	status = "You Win!"
else:
	status = "You Lose!"
	
html = """
<!doctype html>
<html>
<head><meta charset="utf-8">
<title>Rock Paper Scissors</title></head>
    <body>
        <p>You chose: </p><img src="{source1}" height="300">
        <p>Computer chose: </p><img src="{source2}" height="300">
	<h2>{result}</h2>
    </body>
</html>"""

print(html.format(source1 = images[user_choice], source2 = images[choice], result = status))
