# -*- coding: utf-8 -*-
"""
Created on Sun Jan 28 20:32:27 2018

@author: Dillon
"""

import numpy as np
import random
import matplotlib.pyplot as plt

n = 64.0  #size of square matrix
T = 0.5   #Temp J/kB
nsteps = 100000     #iterations of Metropolis
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

"""Implementing the Metropolis algorithm"""
def metro():   
    i = np.random.randint(n)    #picks i value
    j = np.random.randint(n)    #" jvalue
    r = random.random()
    dE = del_energy(i, j)       #energy diff
    
    Temp_flip = np.exp(dE/T)    
    Temp_flip = float(Temp_flip)
    
    if dE > 0 or r < Temp_flip:
        spinlat[i][j] = -spinlat[i][j]
        
    return np.sum(spinlat)

"""creating a list that contains the magnetisation"""
maglist = []
for z in range(nsteps):
    maglist.append(metro()/n**2)
    if z % 10000 ==0:   #unnecessary loading bar
        print z
        
"""plotting the magnetisation vs number of iterations"""
plt.plot(range(nsteps), maglist)
plt.xlabel('Number of iterations')
plt.ylabel('Magnetisation')
plt.title('Magnetisation vs Number of steps (nsteps)')