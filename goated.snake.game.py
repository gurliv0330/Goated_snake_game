# GOATED SNAKE GAME


import random
import turtle
import time

# Set up the screen
wn = turtle.Screen()
wn.title("Goated Snake Game")
wn.bgcolor("#050125")
wn.setup(width=600, height=600)
wn.tracer(0)

# Score
score = 0
high_score = 0

# Set up the head of the snake
head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("#b54efa")
head.penup()
head.goto(0, 0)
head.direction = "stop"

# Snake Body Segments
segments = []

# Function to draw a custom birthday cake shape for the food
def draw_cake(food_turtle):
    x, y = food_turtle.xcor(), food_turtle.ycor()
    food_turtle.clear()

    # 1. Cake Base (pink)
    food_turtle.penup()
    food_turtle.goto(x - 12, y - 10)
    food_turtle.color("#ff76ba")
    food_turtle.begin_fill()
    food_turtle.pendown()
    food_turtle.goto(x + 12, y - 10)
    food_turtle.goto(x + 12, y)
    food_turtle.goto(x - 12, y)
    food_turtle.goto(x - 12, y - 10)
    food_turtle.end_fill()

    # 2. Cake Frosting (white)
    food_turtle.penup()
    food_turtle.goto(x - 14, y)
    food_turtle.color("white")
    food_turtle.begin_fill()
    food_turtle.pendown()
    food_turtle.goto(x + 12, y)
    food_turtle.goto(x + 12, y + 4)
    food_turtle.goto(x - 12, y + 4)
    food_turtle.goto(x - 12, y)
    food_turtle.end_fill()

    # 3. Candle (Blue)
    food_turtle.penup()
    food_turtle.goto(x - 2, y + 4)
    food_turtle.color("blue")
    food_turtle.begin_fill()
    food_turtle.pendown()
    food_turtle.goto(x + 2, y + 4)
    food_turtle.goto(x + 2, y + 12)
    food_turtle.goto(x - 2, y + 12)
    food_turtle.goto(x - 2, y + 4)
    food_turtle.end_fill()

    # 4. Flame (Yellow)
    food_turtle.penup()
    food_turtle.goto(x, y + 15)
    food_turtle.color("yellow")
    food_turtle.dot(8)
    food_turtle.penup()

    # turtle back to center
    food_turtle.penup()
    food_turtle.goto(x, y)


# Food hide
food = turtle.Turtle()
food.speed(0)
food.hideturtle()
food.penup()
food.goto(0, 100)
draw_cake(food)


# Scoreboard
pen = turtle.Turtle()
pen.speed(0)
pen.color("pink")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write(
    "Score: 0  High Score: 0",
    align="center",
    font=("Courier", 24, "bold"),
)
pen.hideturtle()
#Dedicated pen for the Game Over message
popup_pen = turtle.Turtle()
popup_pen.speed(0)
popup_pen.color("red")
popup_pen.penup()
popup_pen.hideturtle()


# Functions to control the snake's movement
def go_up():
    if head.direction != "down":
        head.direction = "up"


def go_down():
    if head.direction != "up":
        head.direction = "down"


def go_left():
    if head.direction != "right":
        head.direction = "left"


def go_right():
    if head.direction != "left":
        head.direction = "right"


def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 20)

    if head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)

    if head.direction == "left":
        x = head.xcor()
        head.setx(x - 20)

    if head.direction == "right":
        x = head.xcor()
        head.setx(x + 20)


# Keyboard bindings
wn.listen()
wn.onkeypress(go_up, "Up")
wn.onkeypress(go_down, "Down")
wn.onkeypress(go_left, "Left")
wn.onkeypress(go_right, "Right")

# Game over
def trigger_game_over():
    global score

    #SHOW POP UP
    popup_pen.goto(0, 0)
    popup_pen.color("red")
    popup_pen.write(
        f"GAME OVER!\nFinal Score: {score}",
        align="center",
        font=("Courier", 24, "bold")
    
    )
    
    wn.update()
    time.sleep(2)
    popup_pen.clear()

    # Reset state
    head.goto(0, 0)
    head.direction = "stop"
    for segment in segments:
        segment.goto(1000, 1000)
    segments.clear()



    score = 0
    pen.clear()
    pen.write(
    f"Score: {score} High Score: {high_score}",
        align="center",
        font=("Courier", 24, "bold"),
    )


# Main game loop
delay = 0.1
while True:
    wn.update()

    # Check for collision with the border
    if (
        head.xcor() > 280
        or head.xcor() < -280
        or head.ycor() > 280
        or head.ycor() < -280
    ):
        trigger_game_over()

    # Check for collision with the food (eating the cake)
    if head.distance(food) < 20:
        # Move the food to a random spot
        x = random.randint(-280, 280)
        y = random.randint(-280, 280)
        food.goto(x, y)

        # the food is actually js cake
        draw_cake(food)

        # Add a new segment to the snake
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("#d090fa")
        new_segment.penup()
        segments.append(new_segment)

        # Increase the score
        score += 10
        if score > high_score:
            high_score = score

        pen.clear()
        pen.write(
            f"Score: {score} High Score: {high_score}",
            align="center",
            font=("Courier", 24, "bold"),
        )

    # Move the end segments first in reverse order
    for index in range(len(segments) - 1, 0, -1):
        x = segments[index - 1].xcor()
        y = segments[index - 1].ycor()
        segments[index].goto(x, y)

    # Move segment 0 to where the head is
    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x, y)

    move()

    # Check for head collision with the body segments
    for segment in segments:
        if segment.distance(head) < 20:
            trigger_game_over()

    time.sleep(delay) 
