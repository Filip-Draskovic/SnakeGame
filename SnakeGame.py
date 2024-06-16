import turtle
import time
import random

delay = 0.1

# Score
score = 0
high_score = 0


# Screen Setup
wn = turtle.Screen()
wn.title("Snake Game")
wn.bgcolor("Green")
wn.setup(width=600, height=600)
wn.tracer(0)

# Snake Head
head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("black")
head.penup()
head.goto(0, 0)
head.direction = "stop"

# Apple (Food)
food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("red")
food.penup()
food.goto(0, 100)

segments = []

# Instruction Pen
ins_pen = turtle.Turtle()
ins_pen.speed(0)
ins_pen.shape("square")
ins_pen.color("white")
ins_pen.penup()
ins_pen.hideturtle()
ins_pen.goto(0, -260)
ins_pen.write("Movement: W, A, S, D", align="center",
              font=("Courier", 16, "normal"))

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("score: 0     high score: 0", align="center",
          font=("Courier", 16, "normal"))

# Functions
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

# Keyboard Binding
wn.listen()
wn.onkeypress(go_up, "w")
wn.onkeypress(go_down, "s")
wn.onkeypress(go_left, "a")
wn.onkeypress(go_right, "d  ")

# Main Game Loop
while True:
    wn.update()

    # Border Collision Check
    if head.xcor()>290 or head.xcor()<-290 or head.ycor()>290 or head.ycor()<-290:
        time.sleep(1)
        head.goto(0, 0)
        head.direction = "stop"

        # Hide Lost Segments
        for segment in segments:
            segment.goto(1000, 1000)

        # Clear Lost Segments
        segments.clear()

        # Reset/Update Score
        score = 0
        pen.clear()
        pen.write("Score: {} High Score: {}".format(score, high_score),
                  align="center", font=("Courier", 16, "normal"))

    # Moving food to random spot, after snake collision
    if head.distance(food) < 20:
        x = random.randint(-290, 290)
        y = random.randint(-290, 290)
        food.goto(x, y)

        # Add a segment
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("black")
        new_segment.penup()
        segments.append(new_segment)

        # Increase the Score
        score += 10
        if score > high_score:
            high_score = score
        pen.clear()
        pen.write("Score: {} High Score: {}".format(score, high_score),
                  align="center", font=("Courier", 16, "normal"))

    # Move the end segments first in reverse order
    for index in range(len(segments)-1, 0, -1):
        x = segments[index-1].xcor()
        y = segments[index - 1].ycor()
        segments[index].goto(x, y)

    # Move segment 0 to the head
    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x, y)

    move()

    # Body Hit by Head Check
    for segment in segments:
        if segment.distance(head) < 20:
            time.sleep(1)
            head.goto(0, 0)
            head.direction = "stop"

            # Hide Lost Segments
            for segment in segments:
                segment.goto(1000, 1000)

            # Clear Lost Segments
            segments.clear()



    time.sleep(delay)
wn.mainloop()