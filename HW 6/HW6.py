#! /usr/bin/env python

# imports of external packages to use in our code
import sys
import math
import numpy as np
#import matplotlib.pyplot as plt


#Generated function by ChatGPT, verified Chat selected functions and then edited result to fit exsisting code here
def gauss_quad_integrate(a, b, num_nodes):
    # Get the Gauss-Legendre nodes and weights
    nodes, weights = np.polynomial.legendre.leggauss(num_nodes)

    # Map the nodes to the integration interval [a, b]
    mapped_nodes = 0.5 * (b - a) * nodes + 0.5 * (b + a)

    # Evaluate the integrand at the mapped nodes
    integrand_values = np.cos(2 * np.pi * mapped_nodes)

    # Compute the integral using the Gaussian Quadrature formula
    integral = np.dot(weights, integrand_values) * 0.5 * (b - a)

    return integral
#Let's use F(x) = cos(2 Pi x) as our integrand and our domain will be [0, 2.5]
#Making the function and the discrete functions #####################################################################

if __name__ == "__main__":
    # if the user includes the flag -h or --help print the options
    if '-h' in sys.argv or '--help' in sys.argv:
        print ("Usage: %s [-seed number]" % sys.argv[0])
        print
        sys.exit(1)

    #Step size, h and the integratable step size
    hdis = 0.125
    #Start,a, and end,b, points of domain under consideration This is the half-open interval [a, b), with the default range being [0,2.5)
    a = 0
    b = 2
    
    # output file defaults
    doOutputFile = False

    # read the user-provided seed from the command line (if there)
    #Note these all assume the user is competent and not trying to break the script
    #This program can and will fail under stupid user conditions
    #“Programming today is a race between software engineers striving to build bigger and better idiot-proof programs, and the Universe trying to produce bigger and better idiots. So far, the Universe is winning.”
        #― Douglas Adams 
    if '-step' in sys.argv:
        p = sys.argv.index('-step')
        hdis = float(sys.argv[p+1])
    if '-xmin' in sys.argv:
        p = sys.argv.index('-xmin')
        a = float(sys.argv[p+1])    
    if '-xmax' in sys.argv:
        p = sys.argv.index('-xmax')
        b = float(sys.argv[p+1])
    #Number of nodes for the Gaussian method
    numnodes = (b-a)/hdis
    if '-numnodes' in sys.argv:
        p = sys.argv.index('numnodes')
        numnodes = int(sys.argv[p+1]) 
    if '-output' in sys.argv:
        p = sys.argv.index('-output')
        OutputFileName = sys.argv[p+1]
        doOutputFile = True
        
        


#Function setup for actual and rule setups############################################
    #Actual function
    #Domain of the function,x
    # x = np.arange(a, b, h)
    # #Function to be integrated, Fx
    # Fx = np.cos(2 * math.pi * x)

    #Method 1: rectangle rule, left aligned
    xdis = np.arange(a, b, hdis) #Domain
    Fxdis = np.cos(2 * math.pi * xdis) #Y-vals at the x's that are evaluated

    #Method2: Trapazoid rule
    xtrap = np.arange(a, b + hdis, hdis)
    Fxtrap = np.cos(2 * math.pi * xtrap)

#Doing the integrations##################################################
    #Actual Function: Integrate[F(x),{x,a,b}] = AntiF(b) - AntiF(a)
    antiFa = 1/(2 * math.pi) * math.sin(2 * math.pi * a)
    antiFb = 1/(2 * math.pi) * math.sin(2 * math.pi * b)
    intactual = antiFb - antiFa

    #rectangle rule: Integrate[F(x),{x,a,b}] = Sum(Fxdis * hdis)
    recsum = 0
    for rec in Fxdis:
        recsum += rec
    recsum *= hdis

    #Trapazoid rule: Integrate[F(x),{x,a,b}] = sum_i=0((Fxtrap_i + Fxtrap_i+1)/2 *hdis)
    Fx0 = float("nan")
    FsumTrap = 0


    #Doing the sum
    for Fx1 in Fxtrap:
        if math.isnan(Fx0):
            Fx0 = Fx1
            continue
        FsumTrap += ((Fx0 + Fx1) / 2) * hdis
        Fx0 = Fx1
    
    

#Doing the Gauss Quadrature Method
    quadintegral = gauss_quad_integrate(a, b, int(numnodes))
    
    
#Outputting Results ######################################################
    if doOutputFile:
        outfile = open(OutputFileName, 'w')
        outfile.write("The function to that was integrated was Cos(2 Pi x) from %s to %s \n" % (a, b))
        outfile.write("The analytical result, using an approximation of Pi, of the integration is %s \n" % intactual)
        outfile.write("The integration result of the rectangle rule is %s \n" % recsum)
        outfile.write("The integration result of the trapazoid rule is %s \n" % FsumTrap)
        outfile.write("The integration result of the Gaussian Quadrature method is %s \n" % quadintegral)
        outfile.write("\n")
        outfile.close()
    else:
        print("The function to that was integrated was Cos(2 Pi x) from %s to %s" % (a, b))
        print("The analytical result, using an approximation of Pi, of the integration is %s" % intactual)
        print("The integration result of the rectangle rule is %s" % recsum)
        print("The integration result of the trapazoid rule is %s" % FsumTrap)
        print("The integration result of the Gaussian Quadrature method is %s" % quadintegral)
        print("\n")