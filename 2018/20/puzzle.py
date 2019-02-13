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

data = data[0]

DIRS = { 'N': (-1,0), 'W': (0,-1), 'E': (0,1), 'S': (1, 0)}

maze = { (0,0):0 }

stack = []
pos = (0,0)
dist = 0
for cc in data[1:-1]:
    if cc == '(':
        stack.append(pos)
    elif cc == '|':
        pos = stack[-1]
        dist = maze[pos]
    elif cc == ')':
        pos = stack.pop(-1)
        dist = maze[pos]
    else:
        pos = aoc.tup_add(pos, DIRS[cc])
        dist += 1

        if not maze.has_key(pos):
            maze[pos] = dist

print 'Part 1: ', max(maze.values())

print 'Part 2:', len([dd for dd in maze.values() if dd >= 1000])
