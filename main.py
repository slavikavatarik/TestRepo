
import turtle

turtle.bgcolor("white")

rainbow_colors = ["red", 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet']
turtle.pensize(5)
turtle.speed(0)

for i in range(360):
    turtle.pencolor(rainbow_colors[i % 7])
    turtle.forward(i)
    turtle.right(60)

turtle.done()