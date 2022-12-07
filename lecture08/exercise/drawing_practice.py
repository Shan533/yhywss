'''
Sample Code
CS 5001, Sample Code, Lecture 8
This module demonstrates drawing basic shapes with Turtle graphics.
'''
import turtle


def draw_line(a_turtle, length):
    '''
        Function -- draw_line
            Draw a line of a given length.
        Parameters:
            a_turtle -- an instance of Turtle
            length -- the length of the line
        Returns:
            Nothing. Draws the line in the graphics window.
    '''
    a_turtle.pendown()
    a_turtle.forward(length)
    a_turtle.penup()


def draw_square(a_turtle, size):
    '''
        Function -- draw_square
            Draw a square of a given size.
        Parameters:
            a_turtle -- an instance of Turtle
            size -- the length of each side of the square
        Returns:
            Nothing. Draws a square in the graphics window.
    '''
    RIGHT_ANGLE = 90
    a_turtle.pendown()
    for i in range(4):
        a_turtle.forward(size)
        a_turtle.left(RIGHT_ANGLE)
    a_turtle.penup()


def draw_triangle(a_turtle, size):
    '''
        Function -- draw_triangle
            Draw an equilateral triangle of a given size.
        Parameters:
            a_turtle -- an instance of Turtle
            size -- the length of each side of the triangle
        Returns:
            Nothing. Draws a triangle in the graphics window.
    '''
    ANGLE = 120
    a_turtle.pendown()
    for i in range(3):
        a_turtle.forward(size)
        a_turtle.left(ANGLE)
    a_turtle.penup()


def draw_circle(a_turtle, size):
    '''
        Function -- draw_circle
            Draw a circle with a given radius.
        Parameters:
            a_turtle -- an instance of Turtle
            size -- the radius of the circle
        Returns:
            Nothing. Draws a circle in the graphics windo.
    '''
    a_turtle.pendown()
    a_turtle.circle(size)
    a_turtle.penup()


def main():
    turtle.setup(420, 420)  # open a window
    turtle.screensize(400, 400)  # set the drawing canvas size
    turtle.bgcolor("white")

    pen = turtle.Turtle()
    pen.hideturtle()
    pen.speed(0)
    draw_line(pen, 100)
    pen.setposition(-100, 0)
    draw_square(pen, 30)
    pen.setposition(100, 100)
    draw_triangle(pen, 50)
    pen.setposition(-100, 100)
    draw_circle(pen, 15)

    turtle.done()  # Important! Stops the window from closing immediately


if __name__ == "__main__":
    main()
