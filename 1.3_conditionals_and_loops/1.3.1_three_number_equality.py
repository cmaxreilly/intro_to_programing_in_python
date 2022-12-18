import sys

# Compose a program that takes three integer command-line arguments and writes 'equal' if all three are equal, and 'not equal' otherwise

if len(sys.argv) < 4:
    print("Insufficient numbers")
elif len(sys.argv) > 4:
    print("Too many numbers")
else:
    a = int(sys.argv[1])
    b = int(sys.argv[2])
    c = int(sys.argv[3])
    if a == b and b == c:
        print("equal")
    else:
        print("not equal") 

