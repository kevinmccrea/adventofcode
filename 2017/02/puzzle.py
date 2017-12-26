#!/usr/bin/env python

import sys
import itertools

infilename = 'input.txt'
if len(sys.argv) > 2 and sys.argv[1] == '-i':
    infilename = sys.argv[2]

print 'Using input file: %s' % infilename

f = open(infilename, 'r')
data = f.readlines()
f.close()

checksum = 0

for line in data:
    vals = map(int, line.split())
    min = vals[0]
    max = vals[0]
    for val in vals:
        if val < min:
            min = val
        if val > max:
            max = val
    checksum += max - min

print checksum

checksum = 0
for line in data:
    vals = map(int, line.split())
    for perm in itertools.permutations(vals, 2):
        if (perm[0] % perm[1]) == 0:
            checksum += perm[0] / perm[1]
print checksum

