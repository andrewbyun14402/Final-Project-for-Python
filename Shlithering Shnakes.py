#Shlithering Shnakes
#By Andrew Byun, Lang Li, Vraj Patel
#Class of 2024
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

#Shnake 1
shnake=turtle.Turtle()
shnake.speed(0)
shnake.shape("square")
shnake.color("green")
shnake.penup()
shnake.goto(-100,0)
shnake.direction="stop"

#Shnake 2
shnake2=turtle.Turtle()
shnake2.speed(0)
shnake2.shape("square")
shnake2.color("blue")
shnake2.penup()
shnake2.goto(100,0)
shnake2.direction="stop"

#Food 1
food1=turtle.Turtle()
food1.speed(0)
food1.shape("circle")
food1.color("red")
food1.penup()
food1.goto(0,100)

#Food 2
food2=turtle.Turtle()
food2.speed(0)
food2.shape("circle")
food2.color("white")
food2.penup()
food2.goto(200,50)

segments=[]
segments2=[]

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player1: 0  Player2: 0", align="center", font=("Courier", 24, "normal"))

# Functions for Shnake 1
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

# Functions for Shnake 2
def go_up2():
    if shnake2.direction != "down":
        shnake2.direction = "up"

def go_down2():
    if shnake2.direction != "up":
        shnake2.direction = "down"

def go_left2():
    if shnake2.direction != "right":
        shnake2.direction = "left"

def go_right2():
    if shnake2.direction != "left":
        shnake2.direction = "right"

def move2():
    if shnake2.direction == "up":
        y = shnake2.ycor()
        shnake2.sety(y + 20)

    if shnake2.direction == "down":
        y = shnake2.ycor()
        shnake2.sety(y - 20)

    if shnake2.direction == "left":
        x = shnake2.xcor()
        shnake2.setx(x - 20)

    if shnake2.direction == "right":
        x = shnake2.xcor()
        shnake2.setx(x + 20)


# Keyboard bindings for Shnake 1
wn.listen()
wn.onkeypress(go_up, "w")
wn.onkeypress(go_down, "s")
wn.onkeypress(go_left, "a")
wn.onkeypress(go_right, "d")

# Keyboard bindings for Shnake 2
wn.onkeypress(go_up2, "Up")
wn.onkeypress(go_down2, "Down")
wn.onkeypress(go_left2, "Left")
wn.onkeypress(go_right2, "Right")

#Score
Player1=0
Player2=0

# Main game loop
while True:
    wn.update()

    # Check for a collision with the border (Shnake 1)
    if shnake.xcor()>290 or shnake.xcor()<-290 or shnake.ycor()>290 or shnake.ycor()<-290:
        time.sleep(1)
        shnake.goto(-100,0)
        shnake.direction = "stop"

        # Hide the segments
        for segment in segments:
            segment.goto(1000, 1000)
        
        # Clear the segments list
        segments.clear()

        # Reset the score
        Player1 = 0

        # Reset the delay
        delay = 0.1

        pen.clear()
        pen.write("Player1: {}  Player2: {}".format(Player1, Player2), align="center", font=("Courier", 24, "normal")) 

# Check for a collision with the border (Shnake 2)
    if shnake2.xcor()>290 or shnake2.xcor()<-290 or shnake2.ycor()>290 or shnake2.ycor()<-290:
        time.sleep(1)
        shnake2.goto(100,0)
        shnake2.direction = "stop"

        # Hide the segments
        for segment in segments2:
            segment.goto(1000, 1000)
        
        # Clear the segments list
        segments2.clear()

        # Reset the score
        Player2 = 0

        # Reset the delay
        delay = 0.1

        pen.clear()
        pen.write("Player1: {}  Player2: {}".format(Player1, Player2), align="center", font=("Courier", 24, "normal")) 


    # Check for a collision with the food (Shnake 1)
    if shnake.distance(food1) < 20:
        # Move the food to a random spot
        x = random.randrange(-280,280,20)
        y = random.randrange(-280,280,20)
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
        Player1 += 10

     
        
        pen.clear()
        pen.write("Player1: {}  Player2: {}".format(Player1, Player2), align="center", font=("Courier", 24, "normal")) 
        
    if shnake.distance(food2) < 20:
        x = random.randrange(-280,280,20)
        y = random.randrange(-280,280,20)
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
        Player1 += 10

     
        
        pen.clear()
        pen.write("Player1: {}  Player2: {}".format(Player1, Player2), align="center", font=("Courier", 24, "normal")) 

 # Check for a collision with the food (Shnake 2)
    if shnake2.distance(food1) < 20:
        # Move the food to a random spot
        x = random.randrange(-280,280,20)
        y = random.randrange(-280,280,20)
        food1.goto(x,y)
        
        # Add a segment
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("grey")
        new_segment.penup()
        segments2.append(new_segment)

        # Shorten the delay
        delay -= 0.001

        # Increase the score
        Player2 += 10

        
        
        pen.clear()
        pen.write("Player1: {}  Player2: {}".format(Player1, Player2), align="center", font=("Courier", 24, "normal")) 
        
    if shnake2.distance(food2) < 20:
        x = random.randrange(-280,280,20)
        y = random.randrange(-280,280,20)
        food2.goto(x,y)
        
        
        # Add a segment
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("grey")
        new_segment.penup()
        segments2.append(new_segment)

        # Shorten the delay
        delay -= 0.001

        # Increase the score
        Player2 += 10

        
        
        pen.clear()
        pen.write("Player1: {}  Player2: {}".format(Player1, Player2), align="center", font=("Courier", 24, "normal")) 

    # Move the end segments first in reverse order (Shnake 1)
    for index in range(len(segments)-1, 0, -1):
        x = segments[index-1].xcor()
        y = segments[index-1].ycor()
        segments[index].goto(x, y)

    # Move the end segments first in reverse order (Shnake 2)
    for index in range(len(segments2)-1, 0, -1):
        x = segments2[index-1].xcor()
        y = segments2[index-1].ycor()
        segments2[index].goto(x, y)

    # Move segment 0 to where Shnake 1 is
    if len(segments) > 0:
        x = shnake.xcor()
        y = shnake.ycor()
        segments[0].goto(x,y)

    # Move segment 0 to where Shnake 2 is
    if len(segments2) > 0:
        x = shnake2.xcor()
        y = shnake2.ycor()
        segments2[0].goto(x,y)

    move()
    move2()

    # Check for shnake 1 collision with the body segments
    for segment in segments:
        if segment.distance(shnake) < 20:
            time.sleep(1)
            shnake.goto(-100,0)
            shnake.direction = "stop"
        
            # Hide the segments
            for segment in segments:
                segment.goto(1000, 1000)
        
            # Clear the segments list
            segments.clear()

            # Reset the score
            Player1 = 0

            # Reset the delay
            delay = 0.1
        
            # Update the score display
            pen.clear()
            pen.write("Player1: {}  Player2: {}".format(Player1, Player2), align="center", font=("Courier", 24, "normal"))

    # Check for shnake 2 collision with the body segments
    for segment in segments2:
        if segment.distance(shnake) < 20:
            time.sleep(1)
            shnake2.goto(100,0)
            shnake2.direction = "stop"
        
            # Hide the segments
            for segment in segments2:
                segment.goto(1000, 1000)
        
            # Clear the segments list
            segments2.clear()

            # Reset the score
            Player2 = 0

            # Reset the delay
            delay = 0.1
        
            # Update the score display
            pen.clear()
            pen.write("Player1: {}  Player2: {}".format(Player1, Player2), align="center", font=("Courier", 24, "normal"))
    time.sleep(delay)

wn.mainloop()

Reference:TokyoEdtech Youtube
