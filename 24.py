#!/usr/bin/env python
# 24 - Decimal to Binary
from sys import argv
try:
    decimal = int(argv[1])
    binary = bin(decimal)[2:]
    print '{0} => {1}'.format(decimal, binary)
except:
    print "Use a decimal number as an argument"
