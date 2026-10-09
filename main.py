# Simple Snake Game
# By Harry Zekkas
# General Python Practice/Fun

import turtle
import time

delay = 0.5

#Screen set up
wn = turtle.Screen()
wn.title("Matrix Snake")
wn.bgcolor("green")
wn.setup(width=600, height=600)
wn.tracer(0)

#Snake Head
head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("black")
head.penup()
head.goto(0,0)
head.direction = "stop"


#Functions
def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 20)

#Main Game Loop
while True:
    wn.update()

    move()

    time.sleep(delay)

wn.mainloop()
