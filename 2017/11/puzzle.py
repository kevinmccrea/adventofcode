#!/usr/bin/env python

import sys
import collections
import operator

infilename = 'input.txt'
if len(sys.argv) > 2 and sys.argv[1] == '-i':
    infilename = sys.argv[2]

print 'Using input file: %s' % infilename

f = open(infilename, 'r')
data = f.readlines()
f.close()

ops = {'s':(0,-1),
       'n':(0,1),
       'se':(1,-1),
       'nw':(-1,1),
       'sw':(-1,0),
       'ne':(1,0)}

def dist(p):
    z = -1 * (p[0] + p[1])
    return max([abs(z), abs(p[0]), abs(p[1])])

position = (0,0)
max_dist = 0
counts = collections.defaultdict(int)
for move in data[0].strip().split(','):
    counts[move] += 1
    
    position = tuple(map(operator.add, position, ops[move]))

    d = dist(position)
    if d > max_dist:
        max_dist = d

print counts
print "Part 1: %s   dist: %d" % (str(position), dist(position))
print "Part 2: %d" % (max_dist)

