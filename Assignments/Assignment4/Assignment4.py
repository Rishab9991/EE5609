# -*- coding: utf-8 -*-
"""
Created on Wed Nov 18 20:15:00 2020

@author: Rishab
"""

import numpy as np
import matplotlib.pyplot as plt
from numpy import linalg as LA

def ellipse_gen(a,b):
	len = 50
	theta = np.linspace(0,2*np.pi,len)
	x_ellipse = np.zeros((2,len))
	x_ellipse[0,:] = a*np.cos(theta)
	x_ellipse[1,:] = b*np.sin(theta)
	return x_ellipse

#Ellipse parameters
V = np.array(([2,-1],[-1,1]))
u = np.array(([1,-1]))
f = 0
c = -LA.inv(V)@u


#Eigenvalues and Parameters of Ellipse
D = LA.eigvals(V)
a = np.sqrt((1-f)/D[0])
b = np.sqrt((1-f)/D[1])
Ellipse = ellipse_gen(a,b)


#Major and Minor Axes of the Ellipse
Major = np.array(([a,0]))
Minor = np.array(([0,b]))


#Plotting the Ellipse
plt.plot(Ellipse[0,:],Ellipse[1,:],label='Ellipse')

#Labelling the Coordinates
tri_coords = np.vstack((Major,Minor,c)).T
plt.scatter(tri_coords[0,:], tri_coords[1,:])
vert_labels = ['$a$','$b$','$\mathbf{c}$']
for i, txt in enumerate(vert_labels):
    plt.annotate(txt, # this is the text
                 (tri_coords[0,i], tri_coords[1,i]), # this is the point to label
                 textcoords="offset points", # how to position the text
                 xytext=(0,10), # distance from text to points (x,y)
                 ha='center') # horizontal alignment can be left, right or center


plt.xlabel('$x$')
plt.ylabel('$y$')
plt.legend(loc='best')
plt.grid() # minor
plt.axis('equal')
plt.show()