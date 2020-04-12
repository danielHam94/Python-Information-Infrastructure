import csv

companies = csv.DictReader(open("companies.csv","r"))

Incom=[]
for data in company:
    if data["state"] == "IN":
        INcom.append(data["company_name"])
print(sorted(Incom))



                        
