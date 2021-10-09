import turtle
import random
from turtle import *

pion = turtle.Turtle()
pion2 = turtle.Turtle()
pion.shape("turtle")
pion2.shape("turtle")
pion.pu()
pion2.pu()
pion.goto(-265, 330)
pion2.goto(260, -170)
pion2.right(180)
pion.pd()
pion.color("#FDA05E")
pion2.color("#FAD29E")
pion.speed(0)
pion.width(4)
viteza = 13


cnt = 0
def up():
    pion.setheading(90)
    pion.forward(viteza)

 
def down():
    pion.setheading(270)
    pion.forward(viteza)


def left():
    pion.setheading(180)
    pion.forward(viteza)

def right():
    pion.setheading(0)
    pion.forward(viteza)


def afis():
    lista = ["Don't give up!","You got this!", "Take your time!"]
    print(random.choice(lista))
   

turtle.listen()
turtle.onkey(up, 'w')
turtle.onkey(down, 's')
turtle.onkey(left, 'a')
turtle.onkey(right, 'd')
turtle.onkey(afis, 'x')
#Press x for motivational message

import desenmaze
turtle.done()



