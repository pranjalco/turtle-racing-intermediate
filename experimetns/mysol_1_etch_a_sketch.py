# from turtle import Turtle, Screen

# etch a sketch project

# tim = Turtle()
# screen = Screen()
#
#
# def move_forwards():
#     tim.forward(10)
#
#
# def move_backwards():
#     tim.backward(10)
#
#
# def rotate_clockwise():
#     tim.right(10)
#
#
# def rotate_anticlockwise():
#     tim.left(10)
#
#
# def reset_screen():
#     screen.resetscreen()
#
#
# screen.listen()
# screen.onkey(key="w", fun=move_forwards)
# screen.onkey(key="s", fun=move_backwards)
# screen.onkey(key="d", fun=rotate_clockwise)
# screen.onkey(key="a", fun=rotate_anticlockwise)
# screen.onkey(key="c", fun=reset_screen)
# screen.exitonclick()

# ===============================================================================================

# Angela sol


from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()


def move_forwards():
    tim.forward(10)


def move_backwards():
    tim.backward(10)


def turn_right():
    new_heading = tim.heading() - 10
    tim.setheading(new_heading)


def turn_left():
    new_heading = tim.heading() + 10
    tim.setheading(new_heading)


def reset_screen():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()


screen.listen()
screen.onkey(key="w", fun=move_forwards)
screen.onkey(key="s", fun=move_backwards)
screen.onkey(key="d", fun=turn_right)
screen.onkey(key="a", fun=turn_left)
screen.onkey(reset_screen, "c")
screen.exitonclick()
