#!/usr/bin/env python
# 39 - Stronger Password Generator (with less chance of predicting an outcome)
import random

things = [chr(i) for i in range(33, 126)]
password = ''

for i in range(random.randint(8,24)):
    password += random.choice(things)
    
print password
