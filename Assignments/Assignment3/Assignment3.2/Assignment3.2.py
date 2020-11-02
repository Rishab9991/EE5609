import numpy as np
import matplotlib.pyplot as plt
from numpy import linalg as LA

#Function for Generating a Circle
def circ_gen(O,r):
	len = 50
	theta = np.linspace(0,2*np.pi,len)
	x_circ = np.zeros((2,len))
	x_circ[0,:] = r*np.cos(theta)
	x_circ[1,:] = r*np.sin(theta)
	x_circ = (x_circ.T + O).T
	return x_circ

C = np.array(([4,3])) #Center of the circle
Q1 = np.array(([1,0]))  #Point of Contact Q1
Q2 = np.array(([7,6]))  #Point of Contact Q2
f = 7
r = np.sqrt(LA.norm(C)**2-f)

#Generating the Circle
x_circ= circ_gen(C,r)

#Plotting the Circle
plt.plot(x_circ[0,:],x_circ[1,:],label='Circle with Center C: (4,3)',color='r')

#Naming the points
tri_coords = np.vstack((Q1,Q2,C)).T
plt.scatter(tri_coords[0,:], tri_coords[1,:])
vert_labels = ['$Q_1$','$Q_2$','C']
for i, txt in enumerate(vert_labels):
    plt.annotate(txt, 
                 (tri_coords[0,i], tri_coords[1,i]), 
                 textcoords="offset points",
                 xytext=(0,10), 
                 ha='center')

'''
Note: For this problem, a perpendicular line must also be computed and plotted and the code 
which you have shared with me uses 1D-arrays. The line perpendicular to the given line 
will have a normal vector such that m.T*n = 0 where n is the normal vector to the given line
and m is the normal vector to the line which is perpendicular to the given line. 
Since transpose of a 1D-array is itself, the line_dir_pt method which you have defined 
in your code was not used and the lines were plotted as follows.
'''

#Generating and Plotting the Lines
x = np.linspace(-10,10,20)
y1 = 1 - x                                     #Given Line - Tangent 1 
y2 = 13 - x                                    #Tangent 2 - Parallel to Tangent 1
y3 = x - 1                                     #Normal 1 - Perpendicular to Tangents 1 and 2
plt.plot(x,y1,label = "Tangent 1: x + y = 1")  #Plotting Tangent 1
plt.plot(x,y2,label = "Tangent 2: x + y = 13") #Plotting Tangent 2
plt.plot(x,y3,label = "Normal 1: x - y = -1")  #Plotting Normal 1

#Labelling the Plots
plt.xlabel('$x$')
plt.ylabel('$y$')
plt.legend(fontsize='small',loc='best')
plt.grid()
plt.axis('equal')
plt.show()