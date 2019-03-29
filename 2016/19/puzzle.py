#!/usr/bin/env python

import sys
import collections
import itertools

infilename = 'input.txt'
if len(sys.argv) > 2 and sys.argv[1] == '-i':
    infilename = sys.argv[2]

print 'Using input file: %s' % infilename

f = open(infilename, 'r')
data = f.readlines()
f.close()

data = [line.strip() for line in data]

num_elves = int(data[0])

circle = collections.deque()
for ii in xrange(1,num_elves+1):
    circle.append((ii, 1))

while len(circle) > 1:
    curr_id, curr_presents = circle.popleft()
    next_id, next_presents = circle.popleft()

    curr_presents += next_presents

    circle.append((curr_id, curr_presents))

print 'Print 1:', circle[0][0]

circle = collections.deque()
for ii in xrange(1,num_elves+1):
    circle.append((ii, 1))
circle.rotate(-(int(len(circle)/2)))

while len(circle) > 1:
    circle.rotate(-(1-(len(circle)%2)))
    circle.popleft()
print 'Part 2:', circle[0][0]
