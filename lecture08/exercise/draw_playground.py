import turtle
from drawing_practice import draw_line, draw_square


def draw_triangle(pen, size):
    ANGLE = 120
    pen.pendown()
    for i in range(3):
        pen.forward(size)
        pen.left(ANGLE)
    pen.penup()


def draw_circle(pen, size):
    pen.pendown()
    pen.circle(size)
    pen.penup()


def main():
    turtle.setup(420, 420)
    turtle.screensize = (400, 400)
    turtle.bgcolor("white")

    pen = turtle.Turtle()
    pen.hideturtle()
    pen.speed(0)
    draw_line(pen, 100)
    pen.setposition(-50, 50)
    draw_triangle(pen, 45)
    pen.setposition(50, 50)
    draw_circle(pen, 100)
    pen.setposition(50, -50)
    draw_square(pen, 40)

    turtle.done()


if __name__ == '__main__':
    main()
