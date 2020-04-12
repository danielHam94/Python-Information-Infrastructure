#Sung Hoon Ham
#Group 2

#1. Answer the question: when using strftime what is the placeholder that will display the full name of the day of the week (Monday, Tuesday, etc.).
#(ex. "%d" is the placeholder that displays the day as a two digit number)

#Answer: "%A"

#2. Write an algorithm for step 3.

#Import datetime
#Mark the date as today
#Format date in the order: year/month/date and change order by index
#Format the date to show the name of the day Monday~Sunday
#Select items that were sold only on the weekends and print those items

#3. Write a program that reads in the information from a file called ShopRecords.csv

import csv
import datetime

shop_rec = csv.DictReader(open("ShopRecords.csv","r"))

for entry in shop_rec:
    date = datetime.date.today()
    date_entry = entry["Date"].split("/")
    day = datetime.date(int(date_entry[2]), int(date_entry[0]), int(date_entry[1]))
    
    if day.strftime("%A") == "Saturday" or day.strftime("%A") == "Sunday":  
        print(entry["Item"])
