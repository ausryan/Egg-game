from sense_hat import SenseHat
from time import sleep
import random

#Sense Hat Demo
#Ryan
#Version 1.0
#28/02/18

#Setup Sense Hat
sense = SenseHat()
#Colours for the egg,player and messages
countdownnumbers=[0,0,255]
countdownbackground=[255,0,255]
eggcolour=[255,255,0]
removecolour=[0,0,0]
playercolour=[0,0,255]
red=[255,0,0]

sense.clear()

#Files
file = open("EggHS.txt","r")
hs=file.readline()

#Function change current score into a function
def currentscore(cs):
    return cs+1

#Variables
cs=0
count=0
eggmove=0
playerloc=7
test="Test"
x=7

#Arrays
countdown=["3","2","1"]

#Read high score
file = open("EggHS.txt","r")
hs=file.readline()
file.close()

#Move the basket
def basket_move(pitch,playerloc):
    new_x=playerloc
    if 1 < pitch < 179 and playerloc != 0:
        new_x -=1
    elif 359 > pitch > 179 and playerloc != 7:
        new_x +=1
    return new_x


#Countdown
while(count < len(countdown)):
    sense.show_message(countdown[count],text_colour=countdownnumbers
                       ,back_colour=countdownbackground)
    count=count+1
sense.clear()


eggrandom = random.randrange(0,8)

#Start dropping the egg
while True:
    #Set the basket location
    sense.set_pixel(playerloc,x,removecolour)
    pitch=sense.get_orientation()['pitch']
    playerloc = basket_move(pitch,playerloc)
    sense.set_pixel(playerloc,x,playercolour)
    sleep(0.2)


    #Shows the location of the egg
    sense.set_pixel(eggrandom,eggmove,eggcolour)
    sleep(0.5)
    #Remove the egg colour
    sense.set_pixel(eggrandom,eggmove,removecolour)

    #Checks if the egg location is equal to the basket
    if(eggmove == 6 and playerloc == eggrandom):
        cs=cs+1
        eggrandom = random.randrange(0,8)
        eggmove=0
        print("Current score " + str(cs))
    #If the egg location made it to the bottom without touching the basket ends the loop
    elif(eggmove == 7):
        break
    #Plus 1 to the eggmove so it can move down
    eggmove=eggmove+1
#Display game over message
sense.show_message("GAME OVER",text_colour=red)
sleep(2)
#Show current and high score
sense.show_message("You Scored " + str(cs),text_colour=red)
print("Current high score " + str(hs))
sense.show_message("High Score " + str(hs),text_colour=red)

#Checks high score and current score, if the current score is better change the high score.
if(int(hs) < cs):
    hs=cs
    print("New high score " + str(hs))
    file = open("EggHS.txt","w")
    file.write(str(cs))
    sense.show_message("New high score " + str(cs),text_colour=red)
    file.close()
#Clear the sense screen
sense.clear()
