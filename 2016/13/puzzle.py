#!/usr/bin/env python

import sys

infilename = 'input.txt'
if len(sys.argv) > 2 and sys.argv[1] == '-i':
    infilename = sys.argv[2]

print 'Using input file: %s' % infilename

f = open(infilename, 'r')
data = f.readlines()
f.close()

dims = (45,45)

for rr in xrange(dims[0]):
    for cc in xrange(dims[1]):
        val = cc*cc + 3*cc + 2*cc*rr + rr +rr*rr + 1352
        ones = bin(val).count('1')
        if cc == 31 and rr == 39:
            print 'X',
        else:
            if ones % 2 == 0:
                print '.',
            else:
                print ' ',
    print ' '



