import xml.etree.ElementTree as ET

def id_find(num):

    root = ET.parse("students.xml")

    students = root.iter("Student")

    for elem in students:
        if elem.find("id").text == num:
            return elem.find("name/first").text + " " + elem.find("name/last").text
    return "Not Found"

##def fee_find(name):
##
##    root = ET.parse("students.xml")
##
##    students = root.iter("Student")
##    for elem in students:
##        if name == elem.find("name/first").text + " " + elem.find("name/last").text:
##            attribute = elem.find("fees").attrib
##            return name + " owes " + elem.find("fees").text + " " + attribute["c"]+ " " + attribute["units"] + " in fees."
##    return "Not Found"

    


#main
print(id_find("0019846768"))
print(id_find("0019846789"))
print(id_find("1234567890"))

##print(fee_find("Rose Dawson"))
##print(fee_find("Jack Sparrow"))
##print(fee_find("No Body"))
