#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 02 - Temperature Converter
source = raw_input('Enter the source temperature unit (K/F/C).\n>>> ')[0].upper()

if source in ['K', 'F', 'C']:
    temperature = raw_input('Enter a temperature in {0}°.\n>>> '.format(source))
    try: 
	temperature = float(temperature)
	if source == 'K':
	    celsius = temperature - 273.15
	    fahrenheit = (celsius * 1.8) + 32
	    print '\n{0} K° = {1} C°'.format(temperature, celsius)
	    print '{0} K° = {1} F°'.format(temperature, fahrenheit)
	elif source == 'F':
	    celsius = (temperature - 32) / 1.8
	    kelvin = celsius + 273.15
	    print '\n{0} F° = {1:.2f} C°'.format(temperature, celsius)
	    print '{0} F° = {1:.2f} K°'.format(temperature, kelvin)
	elif source == 'C':
	    kelvin = temperature + 273.15
	    fahrenheit = temperature * 1.8 + 32
	    print '\n{0} F° = {1} C°'.format(temperature, kelvin)
	    print '{0} F° = {1} K°'.format(temperature, fahrenheit)
    except:
	print '\nERROR: Failed to convert temperature.'
else:
    print '\nERROR: That temperature unit was not found.'
