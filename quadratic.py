import stdio
import sys
import math

# Accept floats b and c as command-line arguments. Compute the 
# roots of the polynomial x^2 + bx + c using the quadratic 
# formula. Write the roots to standard output.

b = float(sys.argv[1])
c = float(sys.argv[2])

discriminant = b*b - 4.0*c
d = math.sqrt(discriminant)

stdio.writeln((-b + d) / 2.0)
stdio.writeln((-b -d) / 2.0)
