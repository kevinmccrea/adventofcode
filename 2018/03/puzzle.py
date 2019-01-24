#!/usr/bin/env python

import sys
import collections
import itertools
import numpy

infilename = 'input.txt'
if len(sys.argv) > 2 and sys.argv[1] == '-i':
    infilename = sys.argv[2]

print 'Using input file: %s' % infilename

f = open(infilename, 'r')
data = f.readlines()
data = [line.strip() for line in data]
f.close()

fab = numpy.zeros((1000,1000))
fab2 = numpy.zeros((1000,1000))
#fab = numpy.zeros((10,10))
#fab2 = numpy.zeros((10,10))

hits = 0
for line in data:
    tokens = line.split(' ')
    claim = int(tokens[0][1:])
    start = tokens[2].split(',')
    start = [start[0], start[1][:-1]]
    start = map(int, start)
    size = tuple(map(int, tokens[3].split('x')))

    collide = False
    for rr in xrange(start[0], start[0]+size[0]):
        for cc in xrange(start[1], start[1]+size[1]):
            if fab[rr][cc] == 1:
                hits += 1
            fab[rr][cc] += 1
            if fab2[rr][cc] == 0:
                fab2[rr][cc] = claim
            else:
                fab2[rr][cc] = -1


#print hits
#print fab2
for line in data:
    tokens = line.split(' ')
    claim = int(tokens[0][1:])
    start = tokens[2].split(',')
    start = [start[0], start[1][:-1]]
    start = map(int, start)
    size = tuple(map(int, tokens[3].split('x')))

    all_good = True
    for rr in xrange(start[0], start[0]+size[0]):
        for cc in xrange(start[1], start[1]+size[1]):
            if fab2[rr][cc] != claim:
                all_good = False
    if all_good:
        #for rr in xrange(start[0], start[0]+size[0]):
        #    for cc in xrange(start[1], start[1]+size[1]):
        #        print fab2[rr][cc],
        #    print ''

        print claim



