from swampy.TurtleWorld import *
import math

def draw(t, length, n):
    """Givena turtle, length, and number, draw a shell-like Koch curve.
    """
    if n == 0:
        return
    angle = 50
    fd(t, length*n)
    lt(t, angle)
    draw(t, length, n-1)
    rt(t, 2*angle)
    draw(t, length, n-1)
    lt(t, angle)
    bk(t, length*n)

world = TurtleWorld()
bob = Turtle()
draw(bob, 3, 4)
lt(bob, 60)
draw(bob, 3, 4)
rt(bob, 120)
draw(bob, 3, 4)
lt(bob, 60)
wait_for_user()

