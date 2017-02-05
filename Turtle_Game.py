#Turtle graphics game
import turtle
import math
import random

#Set up screen
wn = turtle.Screen()
wn.bgcolor("light blue")
wn.tracer(3)

#Draw border
mypen = turtle.Turtle()
mypen.penup()
mypen.speed(100)
mypen.setposition(-600, -600)
mypen.pendown()
mypen.pensize(3)
for side in range(4):
    mypen.forward(1200)
    mypen.left(90)
mypen.hideturtle()

#Create player turtle
player = turtle.Turtle()
player.color("darkblue")
player.shape("turtle")
player.speed(0)
player.penup()

#Create goals
maxGoals = 10
goals = []

for count in range(maxGoals):
    goals.append(turtle.Turtle())
    goals[count].penup()
    goals[count].color("red")
    goals[count].shape("arrow")
    goals[count].speed(0)
    goals[count].setposition(random.randint(-600, 600), random.randint(-600, 600))
    

#Set speed variable
speed = 1

#Define functions

def turnleft():
    player.left(90)

def turnright():
    player.right(90)

def increasespeed():
    global speed
    speed += 1
def decreasespeed():
    global speed
    speed += -1
def isCollision(t1, t2):
    d = math.sqrt(math.pow(t1.xcor()-t2.xcor(),2) + math.pow(t1.ycor()-t2.ycor(),2))
    if d < 20:
        return True
    else:
        return False
    
#Set keyboard binfings
turtle.listen()
turtle.onkey(turnleft, "a")

turtle.onkey(turnright, "d")

turtle.onkey(increasespeed, "w")

turtle.onkey(decreasespeed, "s")

while True:
    player.forward(speed)

    #Boundary check
    if player.xcor() > 600 or player.xcor() < -600:
        player.right(180)

    elif player.ycor() > 600 or player.ycor() < -600:
        player.right(180)




    #Move the goal
    for count in range(maxGoals):
        goals[count].forward(3)



        #Boundary check
        if goals[count].xcor() > 590 or goals[count].xcor() < -590:
            goals[count].right(180)

        elif goals[count].ycor() > 590 or goals[count].ycor() < -590:
            goals[count].right(180)

        #Collision checking
        if isCollision(player, goals[count]):
            goals[count].setpos(random.randint(-590, 590), random.randint(-590, 590)
            goals[count].right(random.randint(0,360))

            







delay = raw_input("Press Enter to finish.")
