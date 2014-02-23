#!/usr/bin/env python
# 05 - FizzBuzz
for i in range(1,101):
    print 'fizz'*(not i%3) + 'buzz'*(not i%5) or i
