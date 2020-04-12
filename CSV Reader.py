##import csv
##
##
##data = open("people_header.csv","r")
##
##
##people = list(csv.reader(data))
##
##
##for line in people:
##    print(line)


import csv

people = csv.DictReader(open("people_header.csv","r"))

for entry in people:
    print(entry,
