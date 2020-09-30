# -*- coding: utf-8 -*-
"""
Created on Tue Sep 29 16:08:45 2020

@author: Rishab
"""
import matplotlib.pyplot as plt
import math as m


#These values are only being used for verifying that hypotenuse is the longest side in a right traingle.
a = [0,5]
b = [0,0]  
c = [5,0]

def distancebetn(P,Q):
    return float(m.sqrt((Q[0]-P[0])**2 + (Q[1]-P[1])**2))

d1 = distancebetn(a,b)
d2 = distancebetn(b,c)
d3 = distancebetn(c,a)

d3 = round(d3,2)

if(d3>d1 and d3>d2):
    print("Hypotenuse is the longest side in a right triangle.")
else:
    print("Hypotenuse is not the longest side in a right triangle.")


plt.plot(a[0],a[1],'o')
plt.text(0,5,'A')
plt.plot(b[0],b[1],'o')
plt.text(0,0,'B')
plt.plot(c[0],c[1],'o')
plt.text(5,0,'C')


x=[0,0,5]
y=[5,0,0]

plt.plot(x,y,'ro')

def connect(x,y,p1,p2):
    x1, x2 = x[p1], x[p2]
    y1, y2 = y[p1], y[p2]
    plt.plot([x1,x2],[y1,y2],'k-')

connect(x,y,0,1)
connect(x,y,1,2)
connect(x,y,2,0)

plt.axis('equal')
plt.show()

