#!/usr/bin/env python
# 01 - Higher or Lower / Heads or Tails
from random import randint
number = randint(1,100)

while 1:
    try:
        guess = int(input("Guess a number between 1 and 100: "))
        if guess not in range(1,101):
            raise
        elif guess > number:
            print "Lower"
        elif guess < number: 
            print "Higher"
        else:
            print "Congratulations, you won!"
            break
    except:
        print "Try again."
