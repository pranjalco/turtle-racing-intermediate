from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()
tim.speed(1)

def move_forwards():
    tim.forward(10)


def move_backwards():
    tim.backward(10)

tim.forward(100)
tim.right(180)
screen.resetscreen()



screen.exitonclick()
