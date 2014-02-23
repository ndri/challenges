#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 03 - Calculate your age in seconds
import time

try: 
    birthtime = int(raw_input("Enter unix time of your birth: "))
    now = int(time.time())
    print "You were born {0} seconds ago.".format(now - birthtime)
except:
    print "An error occurred. Aborting."
