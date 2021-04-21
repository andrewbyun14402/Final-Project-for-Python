#Shlithering Shnakes
#By Andrew Byun, Lang Li, Vraj Patel
import turtle

import time 

import random

delay=0.1
#Screen
wn=turtle.Screen()
wn.title("Shlithering Shnakes")
wn.bgcolor("black")
wn.setup(width=600,height=600)
wn.tracer(0)

#Shnake
shnake=turtle.Turtle()
shnake.speed(0)
shnake.shape("square")
shnake.color("green")
shnake.penup()
shnake.goto(0,0)
shnake.direction="stop"

#Food 1
food1=turtle.Turtle()
food1.speed(0)
food1.shape("square")
food1.color("red")
food1.penup()
food1.goto(0,100)

#Food 2
food2=turtle.Turtle()
food2.speed(0)
food2.shape("square")
food2.color("blue")
food2.penup()
food2.goto(200,50)

segments = []

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Score: 0  High Score: 0", align="center", font=("Courier", 24, "normal"))

# Functions
def go_up():
    if shnake.direction != "down":
        shnake.direction = "up"

def go_down():
    if shnake.direction != "up":
        shnake.direction = "down"

def go_left():
    if shnake.direction != "right":
        shnake.direction = "left"

def go_right():
    if shnake.direction != "left":
        shnake.direction = "right"

def move():
    if shnake.direction == "up":
        y = shnake.ycor()
        shnake.sety(y + 20)

    if shnake.direction == "down":
        y = shnake.ycor()
        shnake.sety(y - 20)

    if shnake.direction == "left":
        x = shnake.xcor()
        shnake.setx(x - 20)

    if shnake.direction == "right":
        x = shnake.xcor()
        shnake.setx(x + 20)

# Keyboard bindings
wn.listen()
wn.onkeypress(go_up, "w")
wn.onkeypress(go_down, "s")
wn.onkeypress(go_left, "a")
wn.onkeypress(go_right, "d")

#Score
score=0
high_score=0

# Main game loop
while True:
    wn.update()

    # Check for a collision with the border
    if shnake.xcor()>290 or shnake.xcor()<-290 or shnake.ycor()>290 or shnake.ycor()<-290:
        time.sleep(1)
        shnake.goto(0,0)
        shnake.direction = "stop"

        # Hide the segments
        for segment in segments:
            segment.goto(1000, 1000)
        
        # Clear the segments list
        segments.clear()

        # Reset the score
        score = 0

        # Reset the delay
        delay = 0.1

        pen.clear()
        pen.write("Score: {}  High Score: {}".format(score, high_score), align="center", font=("Courier", 24, "normal")) 

    # Check for a collision with the food 1
    if shnake.distance(food1) < 20:
        # Move the food 1 to a random spot
        x = random.randint(-290, 290)
        y = random.randint(-290, 290)
        food1.goto(x,y)
     # Add a segment
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("grey")
        new_segment.penup()
        segments.append(new_segment)

        # Shorten the delay
        delay -= 0.001

        # Increase the score
        score += 10

        if score > high_score:
            high_score = score
        
        pen.clear()
        pen.write("Score: {}  High Score: {}".format(score, high_score), align="center", font=("Courier", 24, "normal")) 
    # Check for a collision with the food 2
    if shnake.distance(food2) < 20:
        # Move the food 2 to a random spot
        x = random.randint(-290, 290)
        y = random.randint(-290, 290)
        food2.goto(x,y)
        
        # Add a segment
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("grey")
        new_segment.penup()
        segments.append(new_segment)

        # Shorten the delay
        delay -= 0.001

        # Increase the score
        score += 10

        if score > high_score:
            high_score = score
        
        pen.clear()
        pen.write("Score: {}  High Score: {}".format(score, high_score), align="center", font=("Courier", 24, "normal")) 

    # Move the end segments first in reverse order
    for index in range(len(segments)-1, 0, -1):
        x = segments[index-1].xcor()
        y = segments[index-1].ycor()
        segments[index].goto(x, y)

    # Move segment 0 to where the head is
    if len(segments) > 0:
        x = shnake.xcor()
        y = shnake.ycor()
        segments[0].goto(x,y)

    move()    

    # Check for shnake collision with the body segments
    for segment in segments:
        if segment.distance(shnake) < 20:
            time.sleep(1)
            shnake.goto(0,0)
            shnake.direction = "stop"
        
            # Hide the segments
            for segment in segments:
                segment.goto(1000, 1000)
        
            # Clear the segments list
            segments.clear()

            # Reset the score
            score = 0

            # Reset the delay
            delay = 0.1
        
            # Update the score display
            pen.clear()
            pen.write("Score: {}  High Score: {}".format(score, high_score), align="center", font=("Courier", 24, "normal"))

    time.sleep(delay)

wn.mainloop()
