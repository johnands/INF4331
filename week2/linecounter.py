import sys

# count number of lines in files given as input arguments
# and print to screen
for r in sys.argv[1:]:
    infile = open(r, 'r')
    N = len(infile.readlines())
    print r, ": ", N
