"""
tangentcircles.py
Author: E Dennison
Sources: W Tucker

"""

from ggmath import MathApp, Circle
from math import  acos, pi, cos, sin, sqrt

# angle between child circles n and n+1 (one-based), shrink factor "a",
theta = lambda n, a: acos(((1+a**(n+1))**2+(1+a**n)**2-(a**(n+1)+a**n)**2)/(2*(1+a**(n+1))*(1+a**n)))

#angle between child circles n and 1 (last to first) (one-based), shrink factor "a"
thetalast = lambda n, a: acos(((1+a)**2+(1+a**n)**2-(a+a**n)**2)/(2*(1+a)*(1+a**n)))

# distance to center of nth (one-based) child circle, shrink factor "a", base circle radius r
d = lambda n, a, r: r*(1 + a**n)

# total angle for center of nth child circle (recursive)
thetatot = lambda n, a: 0 if n == 1 else theta(n-1,a) + thetatot(n-1,a)

# position of center of nth child circle, shrink factor a, base circle radius r
def pos(n, a, r):
    r = d(n, a, r)  # get distance to center
    angle = thetatot(n,a)  # angle to center
    return (r*cos(angle), r*sin(angle))

# Angle sum formula, should be zero when solution is found
opt = lambda n, a: thetatot(n, a) + thetalast(n, a) - 2*pi

# distance between two points
distance = lambda p1, p2: sqrt((p1[0]-p2[0])**2 + (p1[1]-p2[1])**2)

# Optimizer for a given number of child circles (n). Function to 
# optimize (func), and two initial guesses (a and b). Optimizer will seek
# a value of shrink factor that minimizes func (to less than 1E-12)
def optimize(n, func, a, b):
    nb = func(n,b)
    while abs(nb) > 1E-12:
        nb = func(n,b)
        na = func(n,a)
        b, a = (a*nb-b*na)/(nb-na), b
    return b



circleqty = int(input("How many circles shall I show? "))

# Figure out the necessary scale factor for the number of circles
a = optimize(circleqty, opt, .9, .99)

# base circle radius, logical units
r = 0.5

# generate a list of (center, radius) tuples
circles = [(pos(n, a, r), r*a**n) for n in range(1, circleqty+1)]

# check for overlap on penultimate circle: compare center distance to radius sum
centersdistance = distance(circles[0][0], circles[circleqty-2][0])
radiussum = circles[0][1]+circles[circleqty-2][1]
if centersdistance >= radiussum:
    print("The scale factor for {} circles is {:.6}".format(circleqty, a))
    # draw the base circle
    Circle((0,0), r)
    # draw the children
    for c in circles:
        Circle(c[0], c[1])
else:
    print("I can't display {} circles without overlapping any.".format(circleqty))

# MathApp will handle the drawing and UI 
app = MathApp()
app.run()
