import turtle

ecran = turtle.Screen()
ecran.bgcolor("#0D1B2A")
ecran.title("The Maze of LIFE")
ecran.setup(1000, 800)


class desen(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("square")
        self.color("#5777B2")
        self.penup()
        self.speed(0)

levels = [""]

level_1 = [
"X  XXXXXXXXXXXXXXXXXXXXXX",
"X  XXXXXXX          XXXXX",
"X  XXXXXXX  XXXXXX  XXXXX",
"X       XX  XXXXXX  XXXXX",
"X       XX  XXX        XX",
"XXXXXX  XX  XXX        XX",
"XXXXXX  XX  XXXXXX  XXXXX",
"XXXXXX  XX    XXXX  XXXXX",
"X  XXX        XXXX  XXXXX",
"X  XXX  XXXXXXXXXXXXXXXXX",
"X             XXXXXXXXXXX",
"X                 XXXXXXX",
"XXXXXXXXXX        XXXX  X",
"XXXXXXXXXXXX      XXXX  X",
"XXX  XXXXXXXX           X",
"XXX                     X",
"XXX       XXXXXXXXXXXXXXX",
"XXX XXXX  XXXXXXXXXXXXXXX",
"XXX XXXX                X",
"XX    XXXX               ",
"XXXXXXXXXX               ",
"XXXXXXXXXXXXXXXXXXXXXXXXX",

]


level_2 = [
"XXXXXXX XXXXXXXXXXXXX",
"X   X     X   X     X",
"X X XXXXX XXX X X X X",
"X X X       X X X X X",
"X XXXXXXXXX X X XXX X",
"X         X     X X X",
"X X XXX X X XXX X XXX",
"X X X X X   X X X   X",
"X XXX X XXXXX XXXXX X",
"X   X     X       X X",
"X XXXXXXX XXX XXX X X",
"X     X   X X X X   X",
"X X XXXXXXX X X XXX X",
"X X X   X X     X X X",
"XXX X XXX XXXXX X XXX",
"X   X   X   X     X X",
"XXX X X XXX XXX XXX X",
"X   X X X           X",
"X X X X X XXX XXXXX X",
"X X   X   X       X  ",
"XXXXXXXXXXXXXXXXXXXXX",
]



def creare(level):
    for y in range(len(level)):
        for x in range(len(level[y])):
            character = level[y][x]
            screen_x = -288 + (x * 24)
            screen_y = 288 - (y * 24)
            if character == "X":
                p.goto(screen_x, screen_y)
                p.stamp()
           

p = desen()

creare(level_2)

while True:
    pass
    turtle.done()
 
    



