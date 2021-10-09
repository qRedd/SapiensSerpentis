import turtle

ecran = turtle.Screen()
ecran.bgcolor("white")
ecran.title("The maze of LIFE")
ecran.setup(800, 800)


class desen(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("square")
        self.color("black")
        self.penup()
        self.speed(0)


level_1 = [
"X  XXXXXXXXXXXXXXXXXXXXXX",
"XP XXXXXXX          XXXXX",
"X  XXXXXXX  XXXXXX  XXXXX",
"X       XX  XXXXXX  XXXXX",
"X       XX  XXX        XX",
"XXXXXX  XX  XXX        XX",
"XXXXXX  XX  XXXXXX  XXXXX",
"XXXXXX  XX    XXXX  XXXXX",
"X  XXX        XXXX  XXXXX",
"X  XXX  XXXXXXXXXXXXXXXXX",
"X         XXXXXXXXXXXXXXX",
"X                 XXXXXXX",
"XXXXXXXXXX        XXXX  X",
"XXXXXXXXXXXX      XXXX  X",
"XXX  XXXXXXXX           X",
"XXX                     X",
"XXX       XXXXXXXXXXXXXXX",
"XXXXXXXX  XXXXXXXXXXXXXXX",
"XXXXXXXX                X",
"XX   XXXXX               ",
"XXXXXXXXXX               ",
"XXXXXXXXXXXXXXXXXXXXXXXXX",

]


def creare(level):
    for y in range(len(level)):
        for x in range(len(level[y])):
            character = level[y][x]
            screen_x = -288 + (x * 24)
            screen_y = 288 - (y * 24)
            if character == "X":
                pen.goto(screen_x, screen_y)
                pen.stamp()
           

pen = desen()

creare(level_1)

while True:
    pass
    turtle.done()
    



