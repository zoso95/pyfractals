# pyfractals

This is a simple python script to generate cool random polynomial fractals. 

This is based off of code from https://github.com/neozhaoliang/pywonderland, but I improved the speed and made it work by randomly generating polynomials.

The basic jist of the algorithm is that it will generate a random 5th degree polynomials, with coefficents of normal*binomial(n=1, p=0.5) [this will randomly drop polynomials terms]

Then we iterate through with Newtons method, and count how long it takes to find a zero from each starting point in C. 
