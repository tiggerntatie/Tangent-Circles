"""
tangentcircles.py
Author: E Dennison
Sources: W Tucker

"""

from math import  acos, pi

# angle between circles n and n+1, shrink factor "a"
th = lambda n, a: acos(((1+a**(n+1))**2+(1+a**n)**2-(a**(n+1)+a**n)**2)/(2*(1+a**(n+1))*(1+q**n)))

print(th(0,.9))