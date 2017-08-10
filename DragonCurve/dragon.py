import sys
import turtle

def iterateTurns(numIter):
	pattern = 'R'	# set initial movement

	# iterate over turns to create pattern
	for i in range(numIter-1):
		pattern = pattern + 'R' + switchPattern(pattern[::-1])

	return pattern

# switch direction in pattern
def switchPattern(pattern):
	switch = ''

	for i in range(len(pattern)):
		if (pattern[i] == 'R'):
			switch += 'L'
		else:
			switch += 'R'

	return switch

def displayPattern(pattern, tilt, r0, g0, b0):
	# initialize turtle
	tur = turtle.Turtle()
	tur.hideturtle()
	tur.speed(0)
	tur.tracer(0, 0)
	tur.right(tilt)

	# set initial color
	r = 0.0
	g = 0.0
	b = 0.0

	# iterate over pattern and draw each movement
	for i in range(len(pattern)):
		r += 1.0 / len(pattern) * r0
		g += 1.0 / len(pattern) * g0
		b += 1.0 / len(pattern) * b0
		tur.pencolor(r, g, b)
		if (pattern[i] == 'R'):
			tur.right(90)
			tur.forward(1)
		else:
			tur.left(90)
			tur.forward(1)

def main(argv):
	# create pattern
	pattern = iterateTurns(15)

	# initialize screen
	win = turtle.Screen()
	win.bgcolor('black')

	# draw each dragon curve
	displayPattern(pattern, 0, 1, 0, 0)
	displayPattern(pattern, 90, 0, 0, 1)
	displayPattern(pattern, 180, 0, 1, 0)
	displayPattern(pattern, 270, 1, 1, 0)

	# update screen
	win.update()

	win.exitonclick()

if __name__ == "__main__":
   main(sys.argv)
