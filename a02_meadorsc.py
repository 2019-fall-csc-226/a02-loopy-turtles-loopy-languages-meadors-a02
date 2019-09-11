######################################################################
# Author: Alex Meadors
# Username: AlexMeadors
#
# Assignment: A02: Loopy Turtles
# Purpose: To demonstrate the turtle library and loops
######################################################################
# Acknowledgements:
#
# original from http://interactivepython.org/runestone/static/thinkcspy/index.html
# first modified by Dr. Jan Pearce
#
# licensed under a Creative Commons
# Attribution-Noncommercial-Share Alike 3.0 United States License.
######################################################################

#Standard enumeration and property setting
import turtle
red = turtle.Turtle()
orange = turtle.Turtle()
yellow = turtle.Turtle()
green = turtle.Turtle()
blue = turtle.Turtle()
purple = turtle.Turtle()
red.color("red")
orange.color("orange")
yellow.color("yellow")
green.color("green")
blue.color("blue")
purple.color("purple")

wn = turtle.Screen()
wn.bgcolor("black")

#Allows me to loop and change turtles with the loop
def setControl(num):
    """
    Sets the target of the commands
    """
    if num == 0:
        target = red
    elif num == 1:
        target = orange
    elif num == 2:
        target = yellow
    elif num == 3:
        target = green
    elif num == 4:
        target = blue
    elif num == 5:
        target = purple
    return target

#Prepping the turtles to have the right attributes
for i in range(6):
    setControl(i).pensize(50)
    setControl(i).speed(0)

#Prep work for starting the loop to start on the left
column = -300

#Creates the rainbow
for counter in range(100):
    for control in range(6):
        setControl(control).penup()
        setControl(control).goto(column,288)
        setControl(control).pendown()
        setControl(control).goto(column,-288)
        column += 60
        #Reseting itself, creating the moving look
        if column >= 330:
            column = -300

wn.exitonclick()