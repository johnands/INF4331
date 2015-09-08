import sys

# convert Fahrenheit F to Celcius C and print to screen
F = float(sys.argv[1])
C = (F - 32)*(5.0/9.0)

print '%.1f Fahrenheit is equal to %.1f Celsius' % (F, C)

