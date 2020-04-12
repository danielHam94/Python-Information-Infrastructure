#Sung Hoon Ham
#Group 2
#Lab Practical 1

pw_list = [word.strip() for word in open("passwords.txt", "r")]

#I had trouble trying to list the words by 5 in each line. I attempted to use the .format to organize it, but I couldn't get it to work.
#I still attempted to try and do the list comprehensions.
output = "{} {} {} {} {}"
def possible_pw():
    print("The current possible passwords are:\n", "-" * 20)
    for i in pw_list[15]:            
        print(output.format(pw_list[index]))

print("Clue 1: The password is at least 6 characters long.\n")
print("The current possible passwords are:\n", "-" * 20)         
clue1 = [output.format(word[0]) for word in pw_list if len(word) >= 6]
print(clue1)

print("Clue 2: The password contains at least one letter.\n")
print("The current possible passwords are:\n", "-" * 20)
clue2 = [output.format(word) for word in clue1 if len([letter for letter in word if letter.isalpha()]) >= 1]
print(clue2)

print("Clue 3: The password starts with a consonant and the third letter is a vowel.\n")
print("The current possible passwords are:\n", "-" * 20)
clue3 = [output.format(word) for word in clue2 if tuple(word[0]) != "aeiou" and tuple(word[2]) == "aeiou"]
print(clue3)

print("Clue 4: The password has no more than half as many vowels as it does consonants.\n")
print("The current possible passwords are:\n","-" * 20)
clue4 = [output.format(word) for word in clue3 if len([letter for letter in word if let in "qwrtyupsdfghjklzxcvbnm"]) > 2 * len([letter for letter in word if letter in "aeiou"])]
print(clue4)

print("Bonus: The password has same letter twice in a row.\n")
print("Password Found!\n","-" * 20)
clue5 = [output.format(word) for word in clue4 if letter[i] == letter[i]]
print(clue5)
        
possible_pw()
