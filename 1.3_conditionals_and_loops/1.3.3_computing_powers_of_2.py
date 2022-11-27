# A small program that accepts integer n as a command-line argument and writes a table containing the first n powers of 2. Eche time through the loop, we increment i and double power. We show only the first three and last three lines of the table; the program write n+1 lines

import sys

n = int(sys.argv[1])
power = 1
i = 0 

while i<= n:
    #write the ith power of 2.
    print(str(i) + ' ' + str(power))
    power = 2 * power
    i = i + 1
