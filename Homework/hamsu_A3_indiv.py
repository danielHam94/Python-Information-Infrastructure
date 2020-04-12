##Sung Hoon Ham
##Group 2


##load the text file
##strip lines and split the lines
##print the words and numbers
##list teams that have less than 5 letters
##select teams that have the highest wins, in this case, more than 7 wins
fileContents = [line.strip().split(" ") for line in open("teams.txt", "r")]


for i in fileContents:
    print("The",i[0]," have won", i[1], " games")

##use len to print words that have less than 5 letters and use index to only select from the first item in line
##print names in string
short_names = [word[0] for word in fileContents if len(word[0]) < 5]

print("Teams with names shorter than 5 letters: ", short_names)

##Made outcome in reverse order with reverse = True
team_rev = sorted([[int(word[1]),word[0]] for word in fileContents], reverse = True)
most_wins = [team_rev[i][1] for i in range(3)]

#double index
print("The three teams with the highest wins are: ", most_wins)
