#!/usr/bin/env python
# 16 - Count the vowels in a string
vowels = 0
string = 'the quick brown fox jumps over the lazy dog'
for letter in string:
    if letter in 'aeiou':
        vowels += 1
print vowels
