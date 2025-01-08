from turtle import Turtle, Screen


screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make a bet", prompt="Which turtle will win the race? Enter a color: ")
print(user_bet)

colors = ["red", "orange", "yellow", "green", "blue", "purple"]
names = ["turtle_1", "turtle_2", "turtle_3", "turtle_4", "turtle_5", "turtle_6"]

turtle_1 = Turtle(shape="turtle")
turtle_1.color(colors[0])
turtle_1.penup()
turtle_1.goto(x=-230, y=-100)

turtle_2 = Turtle(shape="turtle")
turtle_2.color(colors[1])
turtle_2.penup()
turtle_2.goto(x=-230, y=-60)

turtle_3 = Turtle(shape="turtle")
turtle_3.color(colors[2])
turtle_3.penup()
turtle_3.goto(x=-230, y=-20)

turtle_4 = Turtle(shape="turtle")
turtle_4.color(colors[3])
turtle_4.penup()
turtle_4.goto(x=-230, y=20)

turtle_5 = Turtle(shape="turtle")
turtle_5.color(colors[4])
turtle_5.penup()
turtle_5.goto(x=-230, y=60)

turtle_6 = Turtle(shape="turtle")
turtle_6.color(colors[5])
turtle_6.penup()
turtle_6.goto(x=-230, y=100)











screen.exitonclick()
