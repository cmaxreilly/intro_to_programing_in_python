import sys

# A small program that prints conversions from fahrenheit to celcius. 
# Copied from excercise 1.2 in Kernighan and Ritchie text on C 

lower = -80
upper = 500
step = 20

fahr = int(sys.argv[1])

celc = (5/9) * (fahr - 32)
print(str(fahr) + "        " +  str(round(celc, 2)))
