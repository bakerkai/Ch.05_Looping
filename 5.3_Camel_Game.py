'''
CAMEL GAME
----------
The pseudo-code for how to code this game is in Chapter 5 of the Python Jedi book

'''
import random

#variables set

done = False
alive = True

print("Welcome to the camel game (totally not a copy)")
print("You and your camel are running from natives in the desert")
print("You only have a certain range of miles you can travel without food and water, so be prepared and be smart.")

#setting attributes
foodamt = random.randint(10,15)
health = int(20)
status = print(health, foodamt)
sleep =


#start of sequence
while not done:
    print("What do you want to do?")
    userinput = input("Do you want to, A: check status, B: Sleep, C: Eat, D: Sprint till ya cant no more, E: Moderate walk")
    if userinput == 'A':
        print(status)
    elif userinput == 'B':








