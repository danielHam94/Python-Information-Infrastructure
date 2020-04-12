import re

test = "test loon etta planet aaw meek ziiim try"


print("Match: ", re.findall('[\w]*[aeiou][aeiou][\w]*',test))
