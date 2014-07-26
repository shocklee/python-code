from swampy.TurtleWorld import *
import math

def polyline(turtle, n, length, angle):
    """Draws n line segments with a given length and
    angle (in degrees) between them.  A turtle is specified.
    """
    for i in range(n):
        fd(turtle, length)
        lt(turtle, angle)

def polygon(turtle, numberOfSides, length):
    """Draws a polygon given a specific number of sides
    and a length.  A turtle is specified.
    """
    angle = 360.0 / numberOfSides
    polyline(turtle, numberOfSides, length, angle)
        
def arc(turtle, radius, angle):
    """Draws an arc given a specific radious and angle.
    A turtle is specified.
    """
    arc_length = 2 * math.pi * radius * angle / 360
    numberOfSides = int(arc_length / 3) + 1
    step_length = arc_length / numberOfSides
    step_angle = float(angle) / numberOfSides
    polyline(turtle, numberOfSides, step_length, step_angle)

def square(turtle, length):
    """Draws a square, which is nothing more than a polygon with
    a specific line length.  A turtle is specified.
    """
    polygon(turtle, 4, length)
    
def circle(turtle, radius):
    """Draws a circle for s apecified radius.  This is an arc with
    a 360 dregree angle.  A turtle is specified.
    """
    arc(turtle, radius, 360)

world = TurtleWorld()
bob = Turtle()
#print bob
#square(bob, 100)
#polygon(bob, 6, 20)
circle(bob, 10)
wait_for_user()

