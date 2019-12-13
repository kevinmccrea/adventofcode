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


grid = {}

dirs = {'R': (0,1),
        'L': (0,-1),
        'U': (-1,0),
        'D': (1,0)}

crossings = []
wire_steps = []

for xx in xrange(len(data)):
    line = data[xx]

    pos = (0,0)
   
    step_count = 0
    tokens = line.split(',')
    step_map = {}
    for tok in tokens:
        dir = dirs[tok[0]]
        count = int(tok[1:])

        for cc in xrange(count):
            new_pos = aoc.tup_add(pos, dir)
            step_count += 1

            #if new_pos in step_map and step_map[new_pos] < step_count:
                # short circuit
                #step_count = step_map[new_pos]

            step_map[new_pos] = step_count

            if new_pos in grid and grid[new_pos] != xx:
                crossings.append(new_pos)
                grid[new_pos] = 'X'
            else:
                grid[new_pos] = xx

            pos = new_pos

    wire_steps.append(step_map)

first_cross = crossings[0]
min_val = (crossings[0], aoc.mandist((0,0), crossings[0]))
min_both = wire_steps[0][first_cross]
min_both += wire_steps[1][first_cross]
print min_both
for c in crossings:
    d = aoc.mandist((0,0), c)
    if d < min_val[1]:
        min_val = (c, d)

    d_both = wire_steps[0][c] + wire_steps[1][c]
    print c, d_both
    if d_both < min_both:
        min_both = d_both

print 'Part 1:', min_val




print 'Part 2:', min_both

