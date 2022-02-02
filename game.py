


#
# todo: write some Python code here to satisfy the exercise objectives
# ... https://github.com/prof-rossetti/intro-to-python/blob/main/exercises/rock-paper-scissors/README.md
#

# ASK FOR A USER INPUT AND WELCOME TO GAME

print("Rock, Paper, Scissors, Shoot!")

u = input("Please choose one of 'rock', 'paper', 'scissors': ")

r = ["ROCK","rock","Rock"]
p = ["PAPER","paper","Paper"]
s = ["SCISSORS","scissors","Scissors"]

#could have also put print("USER CHOSE:" u) but wanted to unify case

if u in r:
    u = "rock"
    print("USER CHOSE: rock")
elif u in p:
    u = "paper"
    print("USER CHOSE: paper")
elif u in s:
    u = "scissors"
    print("USER CHOSE: scissors")
else:
    print("Invalid selection. Please try again!")

# VALIDATE THE USER CHOICE

valid_input = ["rock","paper","scissors"]

#by fixing the case above, I integrated the data validation


#Failing gracefully is integrated with the data validation


# COMPUTER CHOICE

computer_choices = ["rock","paper","scissors"]

import random
c = random.choice(computer_choices)
print("COMPUTER CHOSE:", c)

# DETERMINE THE WINNER

if u == c:
    print("You both chose",u,"It's a draw!")




# FINAL RESULTS