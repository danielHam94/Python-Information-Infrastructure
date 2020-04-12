## 2.

##Import random module
##
##Display welcome message and explain game rules
##
##Set wincount and totalcount zero
##
##Display user selection choice of Rock, Paper, Scissor
##If user selects a nonexisting option, generate error message and ask for selection choice until user chooses one that is available
##
##Computer chooses one random choice
##
##Compare
##
##If user choice = computer choice
##  print "Tie"
##  increment totalcount value
##
##If user choice = "paper" and computer choice = "scissor"
##  print "Computer Win"
##  increment totalcount value
##
##If user choice = "scissor" and computer choice = "rock"
##  print "Computer Win"
##  increment totalcount value
##
##If user choice = "rock" and computer choice = "paper"
##  print "Computer Win"
##  increment totalcount value
##
##If user choice = "paper" and computer choice = "rock"
##  print "User Win"
##  increment wincount value and totalcount value
##
##If user choice = "scissor" and computer choice = "paper"
##  print "User Win"
##  increment wincount value and totalcount value
##
##If user choice = "rock" and computer choice = "scissor"
##  print "User Win"
##  increment wincount value and totalcount value
##
##  Choose to continue game or quit
##  If user selects continue, go back to step 4
##  If no, print user win against total play and end message

## 3.

string = input("Enter the string: ")

duplicated_string = ""
 
for i in range(len(string)):
    duplicated_string = duplicated_string + string[i]*2

print(duplicated_string)

## 4.

list1 = list(input().split())
list2 = list(input().split())

count = 0

for i in set(list1):
    if i in list2:
        count += 1

print(count)
