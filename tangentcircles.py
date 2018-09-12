"""
tangentcircles.py
Author: E Dennison
Sources: W Tucker

"""

from ggmath import MathApp, Circle
from math import  acos, pi, cos, sin


# angle between circles n and n+1, shrink factor "a"
th = lambda n, a: acos(((1+a**(n+1))**2+(1+a**n)**2-(a**(n+1)+a**n)**2)/(2*(1+a**(n+1))*(1+a**n)))

# distance to center of nth circle, shrink factor "a", base circle radius r
d = lambda n, a, r: r*(1 + a**(n+1))

# total angle for center of nth circle (recursive)
thtot = lambda n, a: 0 if n == 0 else th(n,a) + th(n-1,a)

# position of center of nth circle, shrink factor a, base circle radius r
def pos(n, a, r):
    r = d(n, a, r)  # get distance to center
    angle = thtot(n,a)  # angle to center
    return (r*cos(angle), r*sin(angle))

circleqty = 5
a = 0.8
r = 2
angle = 0

# draw the base circle
Circle((0,0), (r,0))

# draw the children
for n in range(circleqty):
    center = pos(n, a, r)
    Circle(center, (center[0]+r*a**(n+1), center[1]))


app = MathApp()
app.run()