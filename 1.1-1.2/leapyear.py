import stdio
import sys

# Accept an int year as a command-line argument. Write True to 
# standard output if year is a leap year. Otherwise write False.

year = int(sys.argv[1])

isLeapYear = (year % 4 == 0)
isLeapYear = isLeapYear and (year % 100 != 0)
isLeapYear = isLeapYear or (year % 400 == 0)

stdio.writeln(isLeapYear)
