# -*- coding: utf-8 -*-
"""
Created on Sun Jan 28 19:51:14 2018

@author: Dillon
"""

import numpy as np
import random as rnd

n = 50.0  #size of square matrix
T = 2.25   #Temp J/kB
nsteps = 1000000     #iterations of Metropolis
J = 1       #Coupling constant


"""creating an initial 2D square lattice of random values = +/-1""" 
def init_lattice(n):
    spinlat = np.random.choice([-1, 1],[n,n]) #generates an NxN matrix random spins
    return spinlat
    
spinlat = init_lattice(n)  #makes spinlat global
  
"""defining dE so that the Metropolis can Calculate the energy change for each spin flip"""  
#S0 = random lattice point, Sn = Sum of surrounding lattice points including PBCs
def del_energy(i, j):
    S0 = spinlat[i][j]  
    Sn = spinlat[(i-1)%n, j] + spinlat[(i+1)%n, j] + \
    spinlat[i, (j-1)%n] + spinlat[i, (j+1)%n]
    dE = -2*J*S0*Sn   #energy eq
    return dE
