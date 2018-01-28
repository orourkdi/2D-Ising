# -*- coding: utf-8 -*-
"""
Created on Sun Jan 28 19:49:48 2018

@author: Dillon
"""

import numpy as np

n = 50.0  #size of square matrix
T = 2.25   #Temp J/kB
nsteps = 1000000     #amount of times the metro algorithim runs
J = 1               #Coupling constant


"""creating an initial 2D square lattice of random values = +/-1""" 
def init_lattice(n):
    spinlat = np.random.choice([-1, 1],[n,n]) #generates an NxN matrix random spins
    return spinlat