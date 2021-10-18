'''
CAMEL GAME
----------
The pseudo-code for how to code this game is in Chapter 5 of the Python Jedi book

'''
import random

#variables set

done = False
#alive = True

print("Welcome to the camel game (totally not a copy)")
print("You and your camel are running from natives in the desert")
print("You only have a certain range of miles you can travel without food and water, so be prepared and be smart.")

#setting attributes
foodamt = random.randint(10,15)
health = int(50)
wolfdistance = int(50)
healthdecrease = random.randint(5, 15)
randomrunrandomwolf = random.randint(5, 15)
randomrun = random.randint(5, 15)
sleepheal = int(10)
randomwalk = random.randint(5, 10)
easyhealthdecrease = random.randint(99, 100)
#start of sequence
if wolfdistance == 0:
    done = True
if health <= 0:
    print("You have died. Get good kid. I'm not even gonna let you end it yourself. Nerd.")
    done = True
while not done:
    print("What do you want to do?")
    userinput = input("Do you want to, A: check status, B: Sleep, C: Eat, D: Sprint till ya cant no more, E: Moderate walk, Q: Quit game")
    if userinput == 'A':
        print("Health", health, "Food", foodamt)
    elif userinput == 'C':
        print("You have eaten food, your health has increased.")
        health += 10
        foodamt -= 1
    elif userinput == 'D':
        print("You have ran",randomrun, "mile away from the wolves.The wolves have advanced by", randomrunrandomwolf, "Your health has decreased by", healthdecrease)
        wolfdistance = wolfdistance + randomrun
        wolfdistance = wolfdistance - randomrunrandomwolf
        health = health - healthdecrease
    elif userinput == 'B':
        print("You have decided to stay and sleep. Your health increased by", sleepheal, " However the wolves have advanced by", randomrunrandomwolf)
        health = health + sleepheal
        wolfdistance = wolfdistance - randomrunrandomwolf
    elif userinput == 'E':
        print("You have ran", randomwalk, "This was a easy run so you only lost", easyhealthdecrease, "Health")
        health = health - easyhealthdecrease
    elif userinput == 'Q':
        quit()



'''
CURRENT BUGS:
Need random number removals (EX health) to actually apply 
Random.randint(X,X) selections are not applied correctly (not a random num)
Program does not quit when health is below 0
add way to eat food
sleep night 
direct quit command 
needs finish line 
just add more things in general to it to make it more usable 
add a warning if they get close 
'''




