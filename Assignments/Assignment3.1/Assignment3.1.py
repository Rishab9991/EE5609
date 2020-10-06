# -*- coding: utf-8 -*-
"""
Created on Tue Sep 29 16:08:45 2020

@author: Rishab
"""
import matplotlib.pyplot as plt
import math as m


#These values are only being used for verifying that hypotenuse is the longest side in a right traingle.
a = [0,3]
b = [0,0]  
c = [3,-0.5]
d = [3,5]

def distancebetn(P,Q):
    return float(m.sqrt((Q[0]-P[0])**2 + (Q[1]-P[1])**2))

d1 = round(distancebetn(a,b),2)
d2 = round(distancebetn(b,c),2)
d3 = round(distancebetn(c,d),2)
d4 = round(distancebetn(d,a),2)

'''Since AB and CD are the smallest and largest sides in the quadrilateral. If that condition holds true then the problem can be solved'''
if(d1<d2 and d2<d4 and d4<d3): 
    print("AB and CD are the smallest and largest sides in the quadrilateral. Hence the problem can be solved.")
else:
    print("The problem cannot be solved.")

plt.plot(a[0],a[1],'o')
plt.text(0,3,'A')
plt.plot(b[0],b[1],'o')
plt.text(0,0,'B')
plt.plot(c[0],c[1],'o')
plt.text(3,-0.5,'C')
plt.plot(d[0],d[1],'o')
plt.text(3,5,'D')

x=[0,0,3,3]
y=[3,0,-0.5,5]

plt.plot(x,y,'ro')

def connect(x,y,p1,p2):
    x1, x2 = x[p1], x[p2]
    y1, y2 = y[p1], y[p2]
    plt.plot([x1,x2],[y1,y2],'k-')

connect(x,y,0,1)
connect(x,y,1,2)
connect(x,y,2,3)
connect(x,y,3,0)

plt.axis('equal')
plt.show()

