'''
ROSHAMBO PROGRAM
----------------

Create a program that randomly prints 1, 2, or 3.
Expand the program so it randomly prints rock, paper, or scissors using if statements. Don't select from a list.
Add to the program so it first asks the user their choice as well as if they want to quit.
(It will be easier if you have them enter 1 for rock, 2 for paper, and 3 for scissors.)
Add conditional statements to figure out who wins and keep the records
When the user quits print a win/loss record

'''
import random


userinput = input("What is your bet?")

for i in range(1):
    num = random.randint(1,2,3)
    if num == 1 and userinput == 'Scissors': #Computer says rock
        print("You Lose!")
    elif num == 1 and userinput == 'Paper':
        print("You win!")

    elif num == 2 and userinput == 'Rock': #Computer says paper
        print("You Lose!")
    elif num == 2 and userinput == 'Scissors':
        print("You win!")

    elif num == 3 and userinput == 'Paper': #Computer says Skizzors
        print("You Lose!")
    elif num == 3 and userinput == 'Rock':
        print("You win!")


quit_game = input("In order to quit Type Y or N")
if quit_game == 'Y':
    quit()






