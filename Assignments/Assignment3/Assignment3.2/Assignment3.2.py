# -*- coding: utf-8 -*-
"""
Created on Sat Oct 24 14:04:53 2020

@author: DELL
"""
import numpy as np
import matplotlib.pyplot as plt

fig, ax = plt.subplots()
ax.set(xlim=(-5, 10), ylim = (-5, 10))
circle = plt.Circle((4, 3), 4.24, fill=False)
ax.add_artist(circle)

a = [1,0]
b = [7,6]
c = [4,3]
d = [1,1]

plt.plot(d[0],d[1])
plt.text(1,1,'  n')

plt.plot(c[0],c[1])
plt.text(4,3,'  C')

x = np.linspace(-5,10,20)
y1 = 1 - x 
y2 = 13 - x
plt.plot(x,y1,label = "Line 1: (1 1)x = 1")
plt.text(1,0,'  $q_1$')
plt.plot(x,y2,label = "Line 2: (1 1)x = 13")
plt.text(7,6,'  $q_2$')
plt.plot(x,y2,label = "Line 2: (1 1)x = 13")
plt.text(7,6,'  $q_2$')
plt.scatter(a[0],a[1], color="black", label='$q_1$: (1,0)')
plt.scatter(b[0],b[1], color="red", label='$q_2$: (7,6)')
plt.scatter(c[0],c[1], color="blue", label='C: (4,3)')
plt.scatter(d[0],d[1], color="purple", label='$n$: (1,1)') #The line passing through n will be the normal to
plt.legend()
plt.axis('equal')
plt.show()