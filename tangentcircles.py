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

def optimize(n, opt, guess1, guess2):
    a = guess1
    b = guess2
    val = 1
    while abs(val) > 1E-12:
        c = (a*opt(n,b)-b*opt(n,a))/(opt(n,b)-opt(n,a))
        a = b
        b = c
        val = opt(n,c)
    return c


circleqty = 30

print(optimize(circleqty, opt, .9, .99))


a = optimize(circleqty, opt, .9, .99)
r = 0.5
angle = 0

# draw the base circle
Circle((0,0), r)

# draw the children
for n in range(1, circleqty+1):
    center = pos(n, a, r)
    Circle(center, r*a**n)

print(thtot(circleqty, a) + thlast(circleqty, a) - 2*pi)


app = MathApp()
app.run()
