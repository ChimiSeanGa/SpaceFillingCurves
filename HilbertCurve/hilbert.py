import sys
import turtle
import math

patternA = '-BF+AFA+FB-'	# recursive pattern A
patternB = '+AF-BFB-FA+'	# recursive pattern B

def getPattern(pattern):
	newPattern = ''

	# obtain new pattern by recursing through given pattern
	for c in pattern:
		if c == 'A':
			newPattern += patternA
		elif c == 'B':
			newPattern += patternB
		else:
			newPattern += c

	return newPattern

def recursePattern(n):
	pattern = patternB

	# get new pattern
	while n > 0:
		pattern = getPattern(pattern)
		n -= 1

	return pattern

def displayPattern(pattern):
	# initialize turtle
	tur = turtle.Turtle()
	tur.hideturtle()
	tur.tracer(0, 0)
	tur.speed(speed=0)
	# tur.pencolor(1.0, 1.0, 1.0)

	# set position of turtle
	tur.penup()
	tur.setpos(-323, 323)
	tur.pendown()

	i = 0			# frequency multiplier
	freq = 0.00017	# frequency of color

	for c in pattern:
		# if movement, set color
		if c != 'A' and c != 'B':
			r = math.sin(freq*i + 2) * 0.5 + 0.5
			g = math.sin(freq*i + 4) * 0.5 + 0.5
			b = math.sin(freq*i) * 0.5 + 0.5

			i += 1

			tur.pencolor(r, g, b)

		if c == '+':
			tur.right(90)
		elif c == '-':
			tur.left(90)
		elif c == 'F':
			tur.forward(5)

def main(argv):
	# create pattern through recursion
	pattern = recursePattern(6)
	print pattern

	# initialize screen
	win = turtle.Screen()
	win.setup(656, 656)
	win.bgcolor('black')

	# draw curve
	displayPattern(pattern)

	# update screen
	win.update()

	win.exitonclick()

if __name__ == "__main__":
   main(sys.argv)
   