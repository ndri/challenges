#!/usr/bin/env python
# 40 - Find the largest number in an array, and print its position
from random import randint
array = [randint(0,99) for i in range(20)]
print array
print array.index(max(array))
