# PHSX815_Week6

## HW 6
Contains the code for HW 6

### HW6.py
This is the code that numerically integrates Cos(2 * Pi * x) over the interval [0, 2] using the rectangle rule, trapazoid rule, and Gaussian quadrature. The results will by default be printed in the console.

The user can also add the following flags before running the code to achieve the following described effects.
- -step : allows the user to change the step size for the integration
- -xmin : allows the user to change the lower bounds of integration
- -xmax : allows the user to change the upper bounds of integration
- -numnodes : allows the user the number of nodes to use in the Gaussian quadrature integration 
- -output : allows the user to choose to save to a text file or some other file format

### Results.txt
This text file contains the results from running HW6.py with the following flags: -step 0.25 -output Results.txt

### Results
Since the Cos(2 Pi x) was integrated from 0 to 2, the result should be 0. As we see in the "analytical result" using math.pi for the calculation, we get an answer that is close to 0, but not actually 0. It is -7.796343665038751e-17.

Surprisingly, one of the approximations got a better result than this. The trapazoid rule got -2.7755575615628914e-17, which is closer to 0. It also beat out the Gaussian quadrature method which obtained -8.604228440844963e-16 for its calculation of the integral.

This amount that the function is off though, at least for this case, is not necessarily indicative of their actual error in general. The interval used in this example was specifically chosen make the trapazoid rule maximally effective. Normally we would expect the Gaussian quadrature method to produce a result with less error, but the fact that math.pi is just an approximation and that the interval used was specifically chosen for the trapazoid method allowed us to get a better answer this way with the trapazoid method.

### Dependancies
This program depends on the numpy package.

### Asistance
Received help on the coding part of the Gaussian quadrature method from ChatGPT. More details about this are included in the code above the `gauss_quad_integrate` functionn


## HW 7
This file contains the code for HW 7. 

### HW7.py 
This file runs the integration for for the function F(x,y) defined over the domain x^2 + y^2 < 1 [Student's note: in order to get anything interesting, this interval was modified to only be the first quadrant (x, y > 0) since F is an odd function]. The integral is then printed to a file or console, according to user included flags.

The flags available to the user are:
- -nmc : allows the user to select the number of Monte Carlo measurements to be made
- -output : allows the user to choose to save to a text file or some other file format

The output of the file are the analytical results for the integration (or rather the numerical integration done by Mathematica: [0.281081]) and the results obtained by our numerical method.

### Results.txt
This is the text file made by HW7.py

### Dependancies
This program is dependant on the following packages:
- numpy
- math

