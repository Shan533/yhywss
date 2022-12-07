import turtle
ANGLE = 144


def draw_line(pen, size):
    pen.pendown()
    for i in range(19):
        if i % 5 == 0:
            pen.color("yellow")
        elif i % 5 == 1:
            pen.color("green")
        elif i % 5 == 2:
            pen.color("navy")
        elif i % 5 == 3:
            pen.color("orange")
        else:
            pen.color("red")
        pen.forward(size + i * 10)
        pen.right(ANGLE)
    pen.penup()


def main():

    pen = turtle.Turtle()
    pen.color("black")
    # pen.settiltangle(90)
    pen.right(ANGLE)
    draw_line(pen, 10)

    turtle.done()  # Stops the window from closing.


if __name__ == '__main__':
    main()
