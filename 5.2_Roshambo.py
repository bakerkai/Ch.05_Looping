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

done = False
gameplayed = 0

while not done:
    userinput = input("What is your bet?")
    if userinput.lower() == "q" or userinput.lower() == "quit":
        done = True
        break
    else:
        for i in range(1):
            num = random.randint(1,3)
            if num == 1 and userinput.lower() == 'scissors': #Computer says rock
                print("You Lose!")
                gameplayed += 1
            elif num == 1 and userinput.lower() == 'paper':
                print("You win!")
                gameplayed += 1
            elif num == 2 and userinput.lower() == 'rock': #Computer says paper
                print("You Lose!")
                gameplayed += 1
            elif num == 2 and userinput.lower() == 'scissors':
                print("You win!")
                gameplayed += 1
            elif num == 3 and userinput.lower() == 'paper': #Computer says Skizzors
                print("You Lose!")
                gameplayed += 1
            elif num == 3 and userinput.lower() == 'rock':
                print("You win!")
                gameplayed += 1

    '''quit_game = input("In order to quit Type Y or N")
    if quit_game == 'Y':
        quit()
    else:'''

# while not done:
#     quit = input("Do you want to quit? Answer Y or N")
#     if quit == "Y":
#         done = True
#     else:
#         continue
#         grit+=1

print("You didn't quit ",gameplayed," times!")






