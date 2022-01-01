#!/usr/bin/env python3

import turtle

turtle.speed("fastest")
turtle.hideturtle()


def pizza(fill, x=0, y=0, r=100, color="red"):

    x *= 120
    y *= 120

    for sector in range(0, 8):
        turtle.penup()
        turtle.goto(x, y)

        if sector in fill:
            turtle.fillcolor(color)
            turtle.begin_fill()

        turtle.pendown()
        turtle.setheading(sector * 45)
        turtle.forward(r)
        turtle.setheading(sector * 45 + 90)
        turtle.circle(r, 45)
        if sector in fill:
            turtle.end_fill()


for i in range(8):
    pizza([i, (i + 2) % 8, (i + 4) % 8], -2 + i % 4, 2 - i // 4, 50)
    pizza([i, (i + 2) % 8, (i + 5) % 8], -2 + i % 4, i // 4 - 1, 50, "blue")

turtle.mainloop()
