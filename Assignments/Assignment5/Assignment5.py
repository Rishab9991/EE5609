# -*- coding: utf-8 -*-
"""
Created on Tue Nov 24 23:17:17 2020

@author: Rishab
"""

import numpy as np
Q = np.array([[2/np.sqrt(5),1/(np.sqrt(5))],[-1/np.sqrt(5),2/(np.sqrt(5))]])
R = np.array([[np.sqrt(5),-3/np.sqrt(5)],[0,1/(np.sqrt(5))]])
A = Q@R 
print(A)