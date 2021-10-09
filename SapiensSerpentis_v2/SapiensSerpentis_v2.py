import turtle
import random
from turtle import *
import math
import time



pawn2= turtle.Turtle()
pawn = turtle.Turtle()
pawn.shape("turtle")
pawn2.shape("turtle")
time.sleep(2)

pawn.goto(0, 0)
pawn2.goto(10,10)
pawn.color("red")
pawn2.color("blue")
pawn.speed(1)
pawn.width(5)

def up():
    pawn.setheading(90)
    pawn.forward(20)

def down():
    pawn.setheading(270)
    pawn.forward(20)

def left():
    pawn.setheading(180)
    pawn.forward(20)

def right():
    pawn.setheading(0)
    pawn.forward(20)

turtle.listen()
turtle.onkey(up, 'w')
turtle.onkey(down, 's')
turtle.onkey(left, 'a')
turtle.onkey(right, 'd')
import desenmaze
turtle.done()


