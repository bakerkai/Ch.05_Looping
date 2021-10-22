'''
CAMEL GAME
----------
The pseudo-code for how to code this game is in Chapter 5 of the Python Jedi book

'''
import random

#variables set

#done = False
#alive = True

print("Welcome to the camel game (totally not a copy)")
print("You and your camel are running from wolves in the desert")
print("You only have a certain range of miles you can travel without food and water, so be prepared and be smart.")
print("You must reach your house before the wolves catch you. ")
print("You are a very hungry person for no reason at all so make sure to check your food very often.")
#setting attributes
foodamt = int(10)
health = int(30)
wolfdistance = int(40)
sleepheal = int(10)
distancefromhome = int(50)
randomevent = random.randint(0, 1)
#start of sequence
#if wolfdistance <= int(0):
    #done = True
#if health <= int(0):
    #print("You have died. Get good kid. I'm not even gonna let you end it yourself. Nerd.")
    #done = True
while health >= 0 and wolfdistance >= 0:
    print("\033[1;32;48m""What do you want to do?")
    userinput = str(input("\033[1;32;48m" "Do you want to,\nA: check status, \nB: Sleep, \nC: Eat, \nD: Sprint till ya cant no more, \nE: Moderate walk, \nQ: Quit game, \nX: Scavange for food"))
    if userinput == 'A':
        print("\033[1;34;48m" "Health", health, "Food", foodamt)
    elif userinput == 'C':
        print("\033[1;34;48m" "You have eaten food, your health has increased.")
        health += 10
        foodamt -= 2
    elif userinput == 'D':
        print("\033[1;34;48m" "You have ran",random.randint(5, 15), "miles away from the wolves. But the wolves have advanced by", random.randint(10, 15), "Miles. Your health has decreased by", random.randint(10, 15), "However you have lost", random.randint(0, 5), " food")
        wolfdistance = wolfdistance + random.randint(5, 15)
        wolfdistance = wolfdistance - random.randint(10, 15)
        health = health - random.randint(5, 10)
        distancefromhome = distancefromhome - random.randint(5, 10)
        foodamt = foodamt - random.randint(0, 5)
    elif userinput == 'B':
        print("\033[1;34;48m" "You have decided to stay and sleep. Your health increased by", sleepheal, " However the wolves have advanced by", random.randint(5,15), "miles.")
        health = health + sleepheal
        wolfdistance = wolfdistance - random.randint(5,15)
    elif userinput == 'E':
        print("\033[1;34;48m" "You have ran", random.randint(5, 15), "miles. This was a easy run so you only lost", random.randint(5, 8), "Health.")
        health = health - random.randint(5, 8)
        distancefromhome = distancefromhome - random.randint(5, 10)
        wolfdistance = wolfdistance - random.randint(5, 7)
    elif userinput == 'Q':
        quit()
    elif userinput == 'X':
        print("\033[1;34;48m" "You have chosen to scavange for food. Whilst doing this the wolves advanced by", random.randint(5,10), "miles. But you have gotten", random.randint(0, 4), "food.")
        wolfdistance = wolfdistance - random.randint(5, 10)
        foodamt = foodamt + random.randint(1, 4)
    if wolfdistance <= 10:
        print("\033[1;31;48m", "WARNING the hungry dogs are getting close") #red
    if distancefromhome <= 10:
        print("WARN- oops i meant good job you are close to home! keep going")
    if distancefromhome <= 20 and randomevent == 1:
        print("You have found a 6 foot deep hole but you are only 2 feet tall. But there is a ladder however it is old and crusty")
        userchoice = str(input("Do you want to go into the ladder? \n Y \n or \n N"))
        if userchoice == 'Y':
            print("You decided to go in. The ladder held up because it was crusty iron and you found 20 food!")
            foodamt = foodamt + 20
        if userchoice == 'N':
            print("You took the easy way... was it worth it though?")

if distancefromhome <= 0:
    print("Congratulations! You have made it home alive!")
if wolfdistance <= 0:
    print("The wolves have ate you")
    print("lmao that bozo sucked, we weren't every trying")

#  "\033[1;31;48m" Red
#  "\033[1;32;48m" Green
#  "\033[1;33;48m" Yellow
#  "\033[1;34;48m" Blue
#  "\033[1;35;48m" Purple
#  "\033[1;36;48m" Cyan






'''
CURRENT BUGS:
'''




