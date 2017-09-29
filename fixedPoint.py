#!/usr/bin/env python2.7

# Will Fritz
# 9/28/2017
# Finds the root of equation in the form of x = f(x) or g(x) = x - f(x) by using the fixed point method
import math

# function to test using python syntax in form g(x) = x - f(x)
def f(x):
    return (1/math.tan(x)) - (1/x) + x
    
def fixedPoint(func,  approx, tol, N):
    for i in range(0, N):
        p = func(approx)
        if abs(p-approx) < tol:
            return p
        approx = p
    return "Method failed after {} iterations".format(N)

print "Fixed point solution: x =", fixedPoint(f, 4.6, 10**-4, 100) 
