import sys

# count number of words in files given as input arguments
# and print to screen
for r in sys.argv[1:]:
    infile = open(r, 'r')
    N = 0
    for line in  infile:
        N += len(line.split())
    print r, ": ", N
