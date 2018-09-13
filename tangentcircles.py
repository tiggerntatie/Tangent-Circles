"""
tangentcircles.py
Author: E Dennison
Sources: W Tucker


"""

from ggmath import MathApp, Circle
from math import  acos, pi, cos, sin

# angle between circles n and n+1 (one-based), shrink factor "a",
th = lambda n, a: acos(((1+a**(n+1))**2+(1+a**n)**2-(a**(n+1)+a**n)**2)/(2*(1+a**(n+1))*(1+a**n)))

#angle between circle n and 1 (last to first) (one-based), shrink factor "a"
thlast = lambda n, a: acos(((1+a)**2+(1+a**n)**2-(a+a**n)**2)/(2*(1+a)*(1+a**n)))

# distance to center of nth (one-based) circle, shrink factor "a", base circle radius r
d = lambda n, a, r: r*(1 + a**n)

# total angle for center of nth circle (recursive)
thtot = lambda n, a: 0 if n == 1 else th(n-1,a) + thtot(n-1,a)

# position of center of nth circle, shrink factor a, base circle radius r
def pos(n, a, r):
    r = d(n, a, r)  # get distance to center
    angle = thtot(n,a)  # angle to center
    return (r*cos(angle), r*sin(angle))

def opt(n, a):
    return thtot(n, a) + thlast(n, a) - 2*pi

def optimize(n, opt, a, b):
    nb = opt(n,b)
    while abs(nb) > 1E-12:
        nb = opt(n,b)
        na = opt(n,a)
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
