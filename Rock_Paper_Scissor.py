#Author : Avish Shah
#Title : Rock, Paper and Scissor game
#Date and Time of creation: 21 June 2020 || 18:11 

import random
print("Hey user, you can choose from the following \n 1.Rock \n 2.Paper \n 3.Scissor ")

# user input
user = input("Please Choose one of the above :").capitalize()
print("You have selected: " + user)

# computer input
print("Now it's computer's turn to select")
computer = random.randint(1, 3)
if computer == 1: 
    comp_choice = 'Rock'
elif computer == 2: 
    comp_choice = 'Paper'
else: 
    comp_choice = 'Scissor'
print("Computer Choice is: " + comp_choice)
print(user + " ||-------V/s-------|| " + comp_choice)

def game(user, comp_choice_name):
    if user == "Rock" and comp_choice == "Paper":
        print("You Lose!")
    elif user == "Paper" and comp_choice == "Rock":
        print("You Win!")
    elif user == "Paper" and comp_choice == "Scissor":
        print("You Lose!")
    elif user == "Rock" and comp_choice == "Scissor":
        print("You Win!")
    elif user == "Scissor" and comp_choice == "Paper":
        print("You Win!")
    elif user == "Scissor" and comp_choice == "Rock":
        print("You Lose!")
    elif user == comp_choice:
        print("Tie!")

game(user, comp_choice)


