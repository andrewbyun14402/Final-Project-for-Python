#Shlithering Shnakes
#By Andrew Byun, Lang Li, Vraj Patel
import turtle

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
