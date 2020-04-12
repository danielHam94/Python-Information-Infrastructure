#! /usr/bin/env python3

print("Content-type: text/html\n")

file1 = open("top100moviesAFI.txt","r")
AFI_file = file1.readlines()
file1.close()

file2 = open("top100moviesRT.txt","r")
RT_file = file2.readlines()
file2.close()

afi_list = [movie.strip() for movie in AFI_file]
rt_list = [movie.strip() for movie in RT_file]

allmovies = []

count = 0
rtmovieRank ={}

for movie in rt_list:
    count += 1
    if movie not in rtmovieRank:
        rtmovieRank[movie] = count
    if movie not in allmovies:
        allmovies.append(movie)

count = 0
afimovieRank = {}

for movie in afi_list:
    count += 1
    if movie not in afimovieRank:
        afimovieRank[movie] = count
    if movie not in allmovies:
        allmovies.append(movie)
 

html = """<!doctype html>
<html>
<head>
    <meta charset="utf-8">
    <title>Top Movies</title>
</head>
<body>
    <h1> Top 100 Film Comparisons </h1>
    <table border = 1>
    <tr>
        <td>Movie</td>
        <td>AFI Rank</td>
        <td>RT Rank</td>"""
       

allmovies = sorted(allmovies)
for movie in allmovies:
    html +="<tr>\n"
    html += "\t\t<td>" + movie + "</td>\n"
    if movie in afi_list:
        html += "\t\t<td>" + str(afimovieRank[movie]) + "</td>\n"
    else:
        html += "\t\t<td>--</td>\n"
    if movie in rt_list:
        html += "\t\t<td>" + str(rtmovieRank[movie]) + "</td>\n"
    else:
        html += "\t\t<td>--</td>\n"
        
html += """
    </table>
</body>
</html>"""

print(html)

