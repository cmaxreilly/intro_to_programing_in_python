import stdio
import random

# Simulate a coi flip by writing 'Heads' or 'Tails' to the stdout

if random.randrange(0, 2) ==0:
    stdio.writeln('Heads')
else:
    stdio.writeln('Tails')
