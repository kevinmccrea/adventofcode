#!/usr/bin/env python

import sys

infilename = 'input.txt'
if len(sys.argv) > 2 and sys.argv[1] == '-i':
    infilename = sys.argv[2]

print 'Using input file: %s' % infilename

f = open(infilename, 'r')
data = f.readlines()
f.close()

all_stars = [tuple(map(int, line.split(','))) for line in data]

def mandist(x, y):
    dist = 0
    for vals in zip(x,y):
        dist += abs(vals[1] - vals[0])
    return dist

constellations = []
remaining_stars = all_stars[:]
while len(remaining_stars):
    open_stars = [remaining_stars.pop()]
    closed_stars = []

    while len(open_stars):
        star = open_stars.pop()

        for s in remaining_stars[:]:
            if mandist(star, s) <= 3:
                open_stars.append(s)
                remaining_stars.remove(s)
        
        closed_stars.append(star)

    constellations.append(closed_stars[:])

print constellations
print len(constellations)

