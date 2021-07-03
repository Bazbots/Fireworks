import turtle as t
import random as r
from Crucial._on_click import on_click

t.hideturtle()

t.speed("fastest")

t.title("Fireworks")

t.onscreenclick(on_click)

def draw_firework(points, size, colour, x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.color(r.choice(colours))
    t.begin_fill()
    for i in range(points):
        t.forward(size)
        t.right(angle)
    t.end_fill()

t.Screen().bgcolor("black")

while True:
    colours = ["yellow", "blue", "red", "green", "purple", "orange"]
    size = r.randint(20, 100)
    points = r.randint(2, 5) * 2 + 1
    angle = 180 - 180 / points
    randX = r.randint(-350, 300)
    randY = r.randint(-250, 250)

    draw_firework(points, size, r.choice(colours), randX, randY)
