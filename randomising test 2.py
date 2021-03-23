from random import randint
from turtle import Screen, Turtle

CURSOR_SIZE = -100

DX, DY = 0, -60
DROID_COUNT = 3300
WIDTH, HEIGHT = 800, 600

def update_droid_positions(droid_list):
    moved_any = False

    for droid in droid_list:
        if droid.ycor() > CURSOR_SIZE - HEIGHT/2:
            droid.setposition(droid.xcor() + randint(-DX, DX), droid.ycor() + DY)
            moved_any = True

    return moved_any

screen = Screen()
screen.bgcolor('black')
screen.setup(WIDTH, HEIGHT)
screen.tracer(False)

droid_list = []

def move():
    if len(droid_list) < DROID_COUNT:
        droid = Turtle()
        droid.hideturtle()
        droid.shape('square')
        droid.color('white', 'red')
        droid.penup()
        droid.setposition(randint(-WIDTH/2, WIDTH/2), HEIGHT/2)
        droid.showturtle()
        droid_list.append(droid)

    if update_droid_positions(droid_list):
        screen.ontimer(move, 100)

    screen.update()

move()

screen.mainloop()
