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
print("You must reach your house before the wolves catch you. ")
#setting attributes
foodamt = random.randint(10,15)
health = int(50)
wolfdistance = int(50)
healthdecrease = random.randint(5, 15)
randomrunrandomwolf = random.randint(5, 15)
randomrun = random.randint(10, 15)
sleepheal = int(10)
randomwalk = random.randint(5, 10)
easyhealthdecrease = random.randint(99, 100)
distancefromhome = 50
hungerdecrease = random.randint(5, 10)
foodscavange = random.randint(0, 5)
#start of sequence
if wolfdistance <= int(0):
    done = True
if health <= int(0):
    print("You have died. Get good kid. I'm not even gonna let you end it yourself. Nerd.")
    done = True
while not done:
    print("What do you want to do?")
    userinput = str(input("Do you want to, A: check status, B: Sleep, C: Eat, D: Sprint till ya cant no more, E: Moderate walk, Q: Quit game, X:Scavange for food"))
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
        distancefromhome = distancefromhome - randomrun
        foodamt = foodamt - hungerdecrease
    elif userinput == 'B':
        print("You have decided to stay and sleep. Your health increased by", sleepheal, " However the wolves have advanced by", randomrunrandomwolf)
        health = health + sleepheal
        wolfdistance = wolfdistance - randomrunrandomwolf
    elif userinput == 'E':
        print("You have ran", randomwalk, "This was a easy run so you only lost", easyhealthdecrease, "Health")
        health = health - easyhealthdecrease
    elif userinput == 'Q':
        quit()
    elif userinput == 'X':
        print("You have chosen to scavange for food. Whilst doing this the wolves advanced by", randomrunrandomwolf, "But you have gotten", )
        wolfdistance = wolfdistance - randomrunrandomwolf
        foodamt = foodamt + foodscavange
    if wolfdistance <= 50:
        print("\033[1;31;48m", "WARNING the hungry dogs are getting close") #red
    if distancefromhome <= 20:
        print("WARN- oops i meant good job you are close to home! keep going")

#  "\033[1;31;48m" Red
#  "\033[1;32;48m" Green
#  "\033[1;33;48m" Yellow
#  "\033[1;34;48m" Blue
#  "\033[1;35;48m" Purple
#  "\033[1;36;48m" Cyan






'''
CURRENT BUGS:
Need random number removals (EX health) to actually apply -  done
Program does not quit when health is below 0
needs finish line 
just add more things in general to it to make it more usable 
add a warning if they get close 
'''




