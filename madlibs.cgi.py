#! /usr/bin/env python3
print('Content-type: text/html\n')

import cgi

form = cgi.FieldStorage()   #parses form data

html = """<!doctype html>
<html>
<head><meta charset="utf-8">
<title>Madlibs</title></head>
    <body>
        <h1>A day in my favorite course: I211</h1>
        <p>As a {w1}, I always make sure to arrive early so I can get the best {w2}</br>
        Next to arrive is my group member,{name}, who goes by {w4}, and is always telling jokes about {w5}. Always makes me {w6}</br>
        When class begins, I {w7} {w8}. This show that I'm paying attention.</br>
        We start to work on the first problem, and I wave my {w9} to let the AI know that I have a question. My AI tells me that a {w10} in my code is causing an error.</br>
        The problems are {w11}, but my team is {w12} and we make it through.</br>
        Class ends and we all go to {w13} to get a {w14}.</p>
    </body>
</html>"""

var1 = form.getfirst('drink','coffee')#9
var2 = form.getfirst('facial expression','laugh')#7
var3 = form.getfirst('adjective','tought')#11
var4 = form.getfirst('thing','upright')#8
var5 = form.getfirst('body part','hand')#2
var6 = form.getfirst('thing','bug')#10
var7 = form.getfirst('piece of furniture','seat')#4
var8 = form.getfirst('objects','pandas')#5
var9 = form.getfirst('rank','junior')#6
var10 = form.getfirst('verb','sit')#3
var11 = form.getfirst('nickname','Skippy')#13
var12 = form.getfirst('place','Starbucks')#12
var13 = form.getfirst('adjective','persistent')#1
var14 = form.getfirst('exclamation','golly')#14
name = form.getfirst('member','Jacob')

print(html.format(w9=var1,w7=var2,w11=var3,w8=var4,w2=var5,w10=var6,w4=var7,w5=var8,w6=var9,w3=var10,w13=var11,w12=var12,w1=var13,w14=var14,name=name))
