


#
# todo: write some Python code here to satisfy the exercise objectives
# ... https://github.com/prof-rossetti/intro-to-python/blob/main/exercises/rock-paper-scissors/README.md
#

# ASK FOR A USER INPUT AND WELCOME TO GAME

print("Rock, Paper, Scissors, Shoot!")

u = input("Please choose one of 'rock', 'paper', 'scissors': ")

print("USER CHOSE:", u)

# VALIDATE THE USER CHOICE

valid_input = ["ROCK","PAPER","SCISSORS","rock","paper","scissors","Rock","Paper","Scissors"]

if u in valid_input:
    
    print("Choice received!")

#Failing gracefully:

else: 
    print("Invalid selection. Please play again!") 
    quit()


# COMPUTER CHOICE

computer_choices = ["rock","paper","scissors"]

import random
c = random.choice(computer_choices)
print("COMPUTER CHOSE:", c)


# DETERMINE THE WINNER





# FINAL RESULTS