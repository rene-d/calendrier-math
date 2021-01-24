#!/usr/bin/env python3

import turtle


turtle.speed(1)
turtle.penup()

turtle.goto(115, 0)
turtle.write("A", font=("Menlo", 20, "normal"))

turtle.goto(100, 0)
turtle.pendown()
turtle.goto(-100, 00)
turtle.goto(-80, 150)
turtle.goto(120, 120)
turtle.goto(100, 0)
turtle.goto(-80, 150)
turtle.goto(100, 200)
turtle.goto(120, 120)
turtle.penup()

turtle.goto(135, 120)
turtle.write("B", font=("Menlo", 20, "normal"))


turtle.mainloop()

# conversion de la capture pour la création du GIF animé:
# ffmpeg -i capture.mov -vf "fps=10,scale=-1:200:flags=lanczos,split[s0][s1];[s0]palettegen[p];[s1][p]paletteuse" -loop 0 24.gif