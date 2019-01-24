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
f.close()

data = [line.strip() for line in data]

serial = 1309
#serial = 57

grid = numpy.zeros((300,300))

for yy in xrange(300):
    for xx in xrange(300):
        rack = xx + 1 + 10
        energy = rack * (yy+1)
        energy += serial
        energy *= rack
        if energy < 100:
            power = 0
        else:
            power = int(str(energy)[-3])
        grid[xx][yy] = power - 5


def get_power(grid, xx, yy, size):
    power = 0
    for y in xrange(yy, yy+size):
        for x in xrange(xx, xx+size):
            power += grid[x][y]
    return power

def run_square(grid, size):
    max_x = 0
    max_y = 0
    peak = 0

    for yy in xrange(0,300-size+1):
        for xx in xrange(0,300-size+1):
            power = get_power(grid, xx, yy, size)
            if power >= peak:
                peak = power
                max_x = xx
                max_y = yy
    return (max_x+1, max_y+1, peak)

print run_square(grid, 3)

for xx in xrange(3,18):
    print run_square(grid, xx), "size", xx
