import sys
import math

# Write a more general and more robust version of quadratic.py
# (Program 1.2.4) that writes the roots of the polynomial ax**2 + bx +c, writes an ap-
# propriate message if the discriminant is negative, and behaves appropriately (avoid-
# ing division by zero) if a is zero.

# Original parameters for 1.2.4:

# Accept floats b and c as command-line arguments. Compute the 
# roots of the polynomial x^2 + bx + c using the quadratic 
# formula. Write the roots to standard output.
if len(sys.argv) < 3:
    print("not enough floating point numbers")
elif len(sys.argv) > 3:
    print("Too many numbers!")
else:
    
    b = float(sys.argv[1])
    c = float(sys.argv[2])

    discriminant = b*b - 4.0*c
    if discriminant > 0:
        d = math.sqrt(discriminant)
        print((-b + d) / 2.0)
        print((-b -d) / 2.0)
    else:
        print("no intersection")
