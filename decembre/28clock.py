#!/usr/bin/env python3

import turtle

turtle.speed(0)
turtle.hideturtle()

for i in range(22):

    # bas du cercle, i.e. 6h
    x = -280 + (i % 6) * 110
    y = 200 - (i // 6) * 150

    # centre du cercle
    xc = x
    yc = y + 40

    turtle.pensize(1)
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.setheading(0)
    turtle.circle(40, steps=60)
    turtle.penup()

    h = (90 + 180 * i) / 11
    m = (12 * h) % 360

    # l'heure
    turtle.goto(x, y - 10)
    turtle.write(f"{int(h/30):02d}:{int(m/6):02d}", align="center")

    # aiguille des heures
    turtle.pensize(2)
    turtle.goto(xc, yc)
    turtle.pendown()
    turtle.setheading(90 - h)
    turtle.forward(27)
    turtle.penup()

    # aiguille des minutes
    turtle.pensize(1)
    turtle.goto(xc, yc)
    turtle.pendown()
    turtle.setheading(90 - m)
    turtle.forward(37)
    turtle.penup()

turtle.mainloop()
