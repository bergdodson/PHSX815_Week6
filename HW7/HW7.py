#! /usr/bin/env python
"""
Created on Mon Feb 27 10:25:10 2023

@author: bergd
"""

#Preamble ###########################################################
import sys
import math
import numpy as np


sys.path.append("C:\\Users\\bergd\\Desktop\\github")#\\PHSX815_Project1") # For running in the IDE console
sys.path.append('/mnt/c/Users/bergd/Desktop/github') # For running in the Ubuntu terminal
from PHSX815_Week6.HW7.Random import Random

#Defining the function to be integrated
def FoXY(x, y):
    return math.cos(x) * math.sin(y)

#Start Program ###############################################################
if __name__ == "__main__":
    # if the user includes the flag -h or --help print the options
    if '-h' in sys.argv or '--help' in sys.argv:
        print ("Usage: %s [-seed number]" % sys.argv[0])
        print
        sys.exit(1)
        
    #Setup instance of random class
    ran = Random()
    boxarea = 1
    totmeas = 1000
    doOutputFile = False
    #Define my function in the area Piecewise function 
    #for x,y x^2+y^2 < 1, f = cos(x)*cos(y)
    #for x,y x^2+y^2 > 1, f = 0

 
    if '-nmc' in sys.argv:
        p = sys.argv.index('-nmc')
        totmeas = float(sys.argv[p+1])
    if '-seed' in sys.argv:
        p = sys.argv.index('-seed')
        seed = float(sys.argv[p+1])
        ran = Random(seed)
    if '-output' in sys.argv:
        p = sys.argv.index('-output')
        OutputFileName = sys.argv[p+1]
        doOutputFile = True
    
    #preparing to integrate    
    nmeas = 0 
    throwtot = 0
    
    while nmeas < totmeas:
        #Doing the MC throw
        x = ran.rand()
        y = ran.rand()
        z = ran.rand()
        
        #Seeing if the MonteCarlo numbers fit in the box we've put around the function
        if x**2 + y**2 > 1 or z > FoXY(x, y):
            throwtot += 1
            continue
        
        #Successful throw
        nmeas += 1
        throwtot += 1
        
    MCint = nmeas/throwtot * boxarea
        
    if doOutputFile:
        outfile = open(OutputFileName, 'w')
        outfile.write("The function to that was integrated was Cos(x)*Sin(y) over the domain x, y: x^2 + y^2 < 1")
        outfile.write("The numerical result obtained using mathematica, because I spent too long looking for a analytical solution, is 0.281081")
        outfile.write("The Monte Carlo integration method result with %s successful measures is %s \n" % (totmeas, MCint))
        outfile.write("\n")
        outfile.close()
    else:
        print("The function to that was integrated was Cos(x)*Sin(y) over the domain x, y: x^2 + y^2 < 1")
        print("The numerical result obtained using mathematica, because I spent too long looking for a analytical solution, is 0.281081")
        print("The Monte Carlo integration method result with %s successful measures is %s \n" % (totmeas, MCint))
        print("\n")
          