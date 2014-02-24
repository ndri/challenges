#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 08 - Love Calculator
first = raw_input("Enter the first name.\n>>> ")
second = raw_input("Enter the second name.\n>>> ")

first_value = sum([ord(i) for i in first.lower()]) % 20
second_value = sum([ord(i) for i in second.lower()]) % 20

difference = abs(first_value - second_value)

compatibility = 100 - (5 * difference)

print "{0}'s compatibility with {1} is {2}%.".format(first, second, compatibility)
