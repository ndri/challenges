#!/usr/bin/env python
# 33 - Area Calculator
import sys

try:
    shape, args = sys.argv[1], ' '.join(sys.argv[2:])
except:
    sys.exit('Error. Use -h for help.')
    
if shape == '-h':
    print 'Challenge 33 - Area Calculator'
    print '-h\t\t\tDisplay this help'
    print '-r width height\t\tArea for a rectangle'
    print '-c radius\t\tArea for a circle'
    print '-t base height\t\tArea for a triangle'
elif shape == '-r':
    try:
        width, height = args.split()[:2]
        area = float(width) * float(height)
        print 'The area of this rectangle is {0:.4}'.format(area)
    except:
        print 'Usage: -r width height'
elif shape == '-c':
    try: 
        radius = float(args.split()[0])
        area = 3.14159265358 * radius**2
        print 'The area of this circle is {0:.4}'.format(area)
    except:
        print 'Usage: -c radius'
elif shape == '-t':
    try: 
        base, height = args.split()[:2]
        area = 0.5 * float(base) * float(height)
        print 'The area of this triangle is {0:.4}'.format(area)
    except:
        print 'Usage: -t base height'
else:
    print 'Error. Use -h for help.'
