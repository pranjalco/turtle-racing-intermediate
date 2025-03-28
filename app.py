from turtle import Turtle, Screen
from other_functions import *
import random

"""
# Project 14: Turtle Racing

## Author
- **Name**: Pranjal Sarnaik
- **Date**: 2024-12-18

## Description:
Turtle Racing is a fun and interactive game built using Python's `turtle` and `random` modules. 
The game involves six colorful turtles racing to the finish line. The player places a bet on one of 
the turtles' colors, and if the selected turtle wins, the player wins; otherwise, they lose. The turtles
start at the same x-position but are positioned at different y-positions. Each turtle moves forward randomly with 
varying speeds to add unpredictability to the race.

## How to Use:
1. Run the game by executing `app.py`.
2. When prompted, type the color of the turtle you want to bet on (options: red, orange, green, yellow, blue, purple).
3. The race will start automatically, and the result will be displayed once the race ends.

## Level
- **Level**: Intermediate
- **Skills:** Python programming, use of `turtle` and `random` modules, basic user interaction, and logic implementation.
- **Domain:** Game Development

## Features
- Six turtles with distinct colors (red, orange, green, yellow, blue, purple).
- User betting functionality for an interactive experience.
- Randomized turtle movements to ensure unpredictable results.
- Dynamic display of the winner at the end of the race.
- Instructions provided at the start of the game.
- Experimentation folder containing temporary or practice files for the project.

## Project Updates
- **Initial Version:** 2024-12-18
- **Last Modified:** 2024-12-27

## Running the Program
1. Ensure Python 3.9 or later is installed on your system.
2. To run the program:
   - **Using PyCharm**: Open the project in PyCharm and run `app.py`.
   - **Using Terminal/Command Prompt**: Navigate to the project folder and execute:
     ```bash
     python app.py
     ```
   - **By Double-Clicking**: You can double-click `app.py` to run it directly, provided Python is set up to execute 
   `.py` files on your system.
3. If the console window closes immediately, run the program from the terminal/command prompt or IDE to see the output.
"""
is_race_on = False
screen = Screen()

screen.title(my_n)
screen.setup(width=500, height=400)
print(instructions)
user_bet = screen.textinput(title="Make a bet", prompt="Which turtle will win the race? Enter a color: ")
print(user_bet)

colors = ["red", "orange", "green", "yellow", "blue", "purple"]
all_turtle = []
y_positions = [-70, -40, -10, 20, 50, 80]

for turtle_index in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y_positions[turtle_index])
    all_turtle.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:

    for turtle in all_turtle:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! the {winning_color} turtle is the winner!")
            else:
                print(f"You've lost! the {winning_color} turtle is the winner!")

        rand_distance = random.randint(5, 11)
        turtle.forward(rand_distance)

name_l()
screen.exitonclick()
