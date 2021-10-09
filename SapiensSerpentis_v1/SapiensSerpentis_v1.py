import turtle
import random
from turtle import *
import math
import time
import tkinter


t = turtle.Turtle()
ecran = turtle.Screen()
t.getscreen().bgcolor("white")
turtle.title("The maze of LIFE")
ecran.setup(800,800)
ecran.bgpic('maze.gif')
ecran.addshape("logo3.gif")
t.shape("logo3.gif")
time.sleep(2)


t.goto(0, 0)
t.speed(1)
#t.color("white")
t.pu()
t.width(5)

def up():
    t.setheading(90)
    t.forward(10)
   
def down():
    t.setheading(270)
    t.forward(10)

def left():
    t.setheading(180)
    t.forward(10)

def right():
    t.setheading(0)
    t.forward(10)

turtle.listen()
turtle.onkey(up, 'w')
turtle.onkey(down, 's')
turtle.onkey(left, 'a')
turtle.onkey(right, 'd')



turtle.mainloop()

