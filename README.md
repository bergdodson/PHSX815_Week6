# PHSX815_Week6

## HW 6
Contains the Code for HW 6

### HW6.py
This is the code that numerically integrates Cos(2 * Pi * x) over the interval [0, 2] using the rectangle rule, trapazoid rule, and Gaussian quadrature. The results will by default be printed in the console.

The user can also add the following flags before running the code to achieve the following described effects.
- -step: allows the user to change the step size for the integration
- -xmin: allows the user to change the lower bounds of integration
- -xmax: allows the user to change the upper bounds of integration
- -numnodes: allows the user the number of nodes to use in the Gaussian quadrature integration 
- -output: allows the user to choose to save to a text file or some other file

### Results.txt
This text file contains the results from running HW6.py with the following flags: -step 0.25 -output Results.txt

### Results
Since the Cos(2 Pi x) was integrated from 0 to 2, the result should be 0. As we see in the "analytical result" using math.pi for the calculation, we get an answer that is close to 0, but not actually 0. It is -7.796343665038751e-17.

Surprisingly, one of the approximations got a better result than this. The trapazoid rule got -2.7755575615628914e-17, which is closer to 0. It also beat out the Gaussian quadrature method which obtained -8.604228440844963e-16 for its calculation of the integral.

This amount that the function is off though, at least for this case, is not necessarily indicative of their actual error in general. The interval used in this example was specifically chosen make the trapazoid rule maximally effective. Normally we would expect the Gaussian quadrature method to produce a result with less error, but the fact that math.pi is just an approximation and that the interval used was specifically chosen for the trapazoid method allowed us to get a better answer this way with the trapazoid method.
