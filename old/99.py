#!/usr/bin/env python
# 99 - Hailstone Sequence
from sys import argv
number = int(argv[1])
    
print number, 
while number != 1:
    if number % 2 == 1:
        number = number * 3 + 1
    else:
        number /= 2
    print number, 
