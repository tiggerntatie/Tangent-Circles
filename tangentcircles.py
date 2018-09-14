"""
tangentcircles.py
Author: E Dennison
Sources: W Tucker

new stuff
"""

from ggmath import MathApp, Circle
from math import  acos, pi, cos, sin

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
    angle = thtot(n,a)  # angle to center
    return (r*cos(angle), r*sin(angle))

# Angle sum formula, should be zero when solution is found
opt = lambda n, a: thtot(n, a) + thlast(n, a) - 2*pi

# Optimizer for a given number of child circles (n). Function to 
# optimize (func), and two initial guesses (a and b). Optimizer will seek
# a value of shrink factor that minimizes output of func (to less than 1E-12)
def optimize(n, func, a, b):
    nb = func(n,b)
    while abs(nb) > 1E-12:
        nb = func(n,b)
        na = func(n,a)
        b, a = (a*nb-b*na)/(nb-na), b
    return b



circleqty = int(input("How many circles shall I show? "))

# Figure out scale factor for given number of circles
a = optimize(circleqty, opt, .9, .99)
print("The scale factor for {} circles is {}".format(circleqty, a))

# base circle radius, logical units
r = 0.5

# draw the base circle
Circle((0,0), r)

# draw the children
for n in range(1, circleqty+1):
    center = pos(n, a, r)
    Circle(center, r*a**n)


app = MathApp()
app.run()
