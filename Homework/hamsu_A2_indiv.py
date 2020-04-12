import time

name = input("What is your name? ")
print("Hello, " + name, "Time to play hangman!")
print("")

time.sleep(1)

print ("Start guessing")
time.sleep(0.5)

word = "hangman
"
guesses = ''

turns = 10

while turns > 0:         
    failed = 0
    
    for char in word:      
        if char in guesses:     
            print(char),    

        else:
            print("_"),     
            failed += 1    

    if failed == 0:        
        print("You won") 
        break
    guess = input("Guess a character:") 
    guesses += guess                    
    if guess not in word:  
        turns -= 1        
        print("Wrong")   
        print("You have", + turns, 'more guesses')
        if turns == 0:           
            print("You Lose")



#3.

from random import randint

def round(items):

    player = input("rock, paper, scissors?: ");
  
    chance = randint(1,100);
  
    if chance < 33:
        choice = 1;
    elif chance >= 33 and chance <= 66:
        choice = 2;
    else:
        choice = 3;
  
    computer = items[choice-1];
  
    print(" Computer chose: " + items[choice-1] + ". ");
  
    inputs = [player.upper(), computer.upper()];  
    return inputs;
  

def main():
    print(" Welcome to the game of Rock-Paper-Scissors ");
    total=0;
    win=0;
    flag=1;
    while(flag!=0):
        items = ["Rock", "Paper", "Scissors"];
  
        inputs = round(items);
  
        while inputs[0] == inputs[1]:
            inputs = round(items);
        total=total+1;
        if inputs == ['ROCK', 'PAPER'] or inputs == ['PAPER', 'ROCK']:
            if inputs[0] == 'PAPER':
                win=win+1;
                print("Paper beats rock! You win!");
            else:
                print("Paper beats rock! You lose!");
  
        elif inputs == ['ROCK', 'SCISSORS'] or inputs == ['SCISSORS', 'ROCK']:
            if inputs[0] == 'ROCK':
                win=win+1;
                print("Rock beats scissors! You win!");
            else:
                print("Rock beats scissors! You lose!");
  
        elif inputs == ['SCISSORS', 'PAPER'] or inputs == ['PAPER', 'SCISSORS']:
            if inputs[0] == 'SCISSORS':
                win=win+1;
                print("Scissors beats paper! You win!");
            else:
                print("Scissors beats paper! You lose!");
  
        else:
            print("Invalid entry!");
            total=total-1;
        flag=int(input('Press 1 to try again, else press 0: '));
  
    print('Total games',total,'Total wins',win);
main();


