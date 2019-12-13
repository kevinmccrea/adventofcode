#!/usr/bin/env python

import sys
import collections
import itertools

import aoc

infilename = 'input.txt'
if len(sys.argv) > 2 and sys.argv[1] == '-i':
    infilename = sys.argv[2]

print 'Using input file: %s' % infilename

f = open(infilename, 'r')
data = f.readlines()
f.close()

data = [line.strip() for line in data]


image = {}
num_layers = len(data[0]) / (25 * 6)
for ll in xrange(num_layers):
    image[ll] = {}
    for rr in xrange(6):
        for cc in xrange(25):
            image[ll][(rr,cc)] = int(data[0][(ll*25*6) + (rr * 25) + cc])

f_ind = 0
f_val = 999999
for ll in xrange(num_layers):
    val = len([x for x in image[ll].values() if x == 0])
    if val < f_val:
        f_val = val
        f_ind = ll

ones = len([x for x in image[f_ind].values() if x == 1])
twos = len([x for x in image[f_ind].values() if x == 2])


print 'Part 1:', ones * twos

final = {}
for rr in xrange(6):
    for cc in xrange(25):
        for ll in xrange(num_layers):
            v = image[ll][(rr,cc)]
            if v != 2:
                if v == 0:
                    final[(rr,cc)] = ' '
                else:
                    final[(rr,cc)] = 'X'
                break

for rr in xrange(6):
    for cc in xrange(25):
        print final[(rr,cc)], 
    print ''



