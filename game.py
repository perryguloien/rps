


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
    u = "ROCK"
    print("USER CHOSE: ROCK")
elif u in p:
    u = "PAPER"
    print("USER CHOSE: PAPER")
elif u in s:
    u = "SCISSORS"
    print("USER CHOSE: SCISSORS")
else:
    print("Invalid selection. Please try again!")

# VALIDATE THE USER CHOICE

valid_input = ["ROCK","PAPER","SCISSORS"]

#by fixing the case above, I integrated the data validation


#Failing gracefully:



# COMPUTER CHOICE

computer_choices = ["rock","paper","scissors"]

import random
c = random.choice(computer_choices)
print("COMPUTER CHOSE:", c)


# DETERMINE THE WINNER





# FINAL RESULTS