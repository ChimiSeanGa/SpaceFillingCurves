import sys
import turtle
from math import sqrt, sin

def iterate(dist, pos, iterNum):
	if iterNum == 0:	# base case
		return

	stems = 4	# number of stems to branch off at each iteration

	# create initial turtles
	turs = [turtle.Turtle() for i in range(stems)]
	angle = 0	# angle of path for turtles

	for tur in turs:
		tur.hideturtle()	# hide turtle figure from drawing
		tur.speed(0)		# set speed to maximum
		tur.tracer(0, 0)	# do not show animation of drawing

		tur.penup()			# stop drawing
		tur.setpos(pos)		# move to location
		tur.pendown()		# continue drawing

		# set color of drawing
		r = 1.0
		g = 1.0
		b = 1.0

		tur.pencolor(r, g, b)

		tur.setheading(angle)	# turn toward angle
		tur.forward(dist)		# move forward by given distance

		iterate(dist / 2, tur.pos(), iterNum - 1)	# iterate to branch off
		angle += 90	# rotate 90 degrees

def main(argv):
	win = turtle.Screen()		# initialize screen
	win.setup(610, 610)			# set width and height of screen
	win.screensize(600, 600)	# set width and height of canvas
	win.bgcolor('black')			# set background color

	iterate(600 / 4, (0, 0), 6)	# call drawing function

	win.update()	# update screen

	# save image of screen to file
	ts = turtle.getscreen()
	ts.getcanvas().postscript(file="squaretree.eps")

	win.exitonclick()

if __name__ == "__main__":
   main(sys.argv)