# -*- coding: utf-8 -*-
"""
Created on Sat Oct 24 14:04:53 2020

@author: DELL
"""

import matplotlib.pyplot as plt

fig, ax = plt.subplots()
ax.set(xlim=(-15, 15), ylim = (-15, 15))
circle = plt.Circle((4, 3), 4.24, fill=False)
ax.add_artist(circle)


q1 = [7,6]
q2 = [1,0]  
c = [4,3]

plt.plot(q1[0],q1[1])
plt.text(7,6,'  $q_1$')
plt.plot(q2[0],q2[1])
plt.text(1,0,'  $q_2$')
plt.plot(c[0],c[1])
plt.text(4,3,'  C')


x=[1,0,13,0]
y=[0,1,0,13]

plt.plot(x,y,'ro')

def connect(x,y,p1,p2):
    x1, x2 = x[p1], x[p2]
    y1, y2 = y[p1], y[p2]
    plt.plot([x1,x2],[y1,y2],'k-')

connect(x,y,0,1)
connect(x,y,2,3)

plt.axis('equal')
plt.show()