'''
Sample Code
CS 5001, Fall 2021
This code will get you started with the final project, milestone 1.
'''
import turtle


NUM_SQUARES = 8  # The number of squares on each row.
SQUARE = 50  # The size of each square in the checkerboard.
SQUARE_COLORS = ("light gray", "white")
ANGLE = 90


def draw_square(pen, size):
    '''
        Function -- draw_square
            Draw a square of a given size.
        Parameters:
            a_turtle -- an instance of Turtle
            size -- the length of each side of the square
        Returns:
            Nothing. Draws a square in the graphics window.
    '''
    x = - (NUM_SQUARES * SQUARE) / 2
    y = - (NUM_SQUARES * SQUARE) / 2
    pen.setposition(x, y)
    pen.pendown()
    for i in range(4):
        pen.forward(size)
        pen.left(ANGLE)
    pen.penup()


def draw_gray_squares(pen, size):
    for i in range(-4, 4):
        for j in range(-4, 4):
            if (i + j) % 2 != 0:
                pen.color("black", "light gray")
            else:
                pen.color("black", "white")
            pen.setposition(SQUARE * i, SQUARE * j)
            pen.begin_fill()
            pen.pendown()
            for x in range(4):
                pen.forward(size)
                pen.left(ANGLE)
            pen.penup()
            pen.end_fill()


def click_handler(x, y):
    '''
        Function -- click_handler
            Called when a click occurs.
        Parameters:
            x -- X coordinate of the click. Automatically provided by Turtle.
            y -- Y coordinate of the click. Automatically provided by Turtle.
        Returns:
            Does not and should not return. Click handlers are a special type
            of function automatically called by Turtle. You will not have
            access to anything returned by this function.
    '''
    print("Clicked at ", x, y)


def main():
    board_size = NUM_SQUARES * SQUARE
    # Create the UI window. This should be the width of the board plus a
    # little margin
    window_size = board_size + SQUARE  # The extra + SQUARE is the margin
    turtle.setup(window_size, window_size)

    # Set the drawing canvas size. The should be actual board size
    turtle.screensize(board_size, board_size)
    turtle.bgcolor("white")  # The window's background color
    turtle.tracer(0, 0)  # makes the drawing appear immediately

    pen = turtle.Turtle()  # This variable does the drawing.
    pen.penup()  # This allows the pen to be moved.
    pen.hideturtle()  # This gets rid of the triangle cursor.

    # The first parameter is the outline color, the second is the filler
    pen.color("black", "white")

    # YOUR CODE HERE
    # Step 1 - the board outline
    draw_square(pen, board_size)
    # Step 2 & 3 - the checkerboard squares
    draw_gray_squares(pen, SQUARE)

    # Click handling
    screen = turtle.Screen()

    # This will call the click_handler function when a click occurs
    screen.onclick(click_handler)

    turtle.done()  # Stops the window from closing.


if __name__ == "__main__":
    main()

