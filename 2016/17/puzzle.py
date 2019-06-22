#!/usr/bin/env python

import sys
import collections
import itertools
import md5

import aoc

infilename = 'input.txt'
if len(sys.argv) > 2 and sys.argv[1] == '-i':
    infilename = sys.argv[2]

print 'Using input file: %s' % infilename

f = open(infilename, 'r')
data = f.readlines()
f.close()

data = [line.strip() for line in data]

OPEN = ['b','c','d','e','f']
DIRS = aoc.CARDINAL_DIRS
DIRS = [DIRS[0], DIRS[3], DIRS[1], DIRS[2]]
DIR_CHARS = ['U', 'D', 'L', 'R']

paths = []

dims = 4

curr = ((0,0), data[0])
end = (dims-1, dims-1)
end_bound = (dims-1, dims-1)

part1 = None
part2 = None

paths.append(curr)
while len(paths):
    # sort by shortest path
    paths.sort(key=lambda t: len(t[1]))
    
    # get the next pos to check
    curr_pos, curr_path = paths.pop(0)
    
    if curr_pos == end:
        if not part1:
            part1 = curr_path

        part2 = curr_path
        continue


    combos = md5.md5(curr_path).hexdigest()

    # add the steps
    for step, dir_char, door in zip(DIRS, DIR_CHARS, combos[:4]):
        new_pos = aoc.tup_add(curr_pos, step)
        if aoc.in_bounds(new_pos, end_bound):
            if door in OPEN:
                paths.append((new_pos, curr_path + dir_char))


print 'Part 1:', part1[len(data[0]):]
print 'Part 2:', len(part2[len(data[0]):])

