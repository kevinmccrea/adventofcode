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

bots = []
for line in data:
    tokens = line.replace('=', ' ').replace('<', ' ').replace('>', ' ').replace(',', ' ').split()
    bots.append((int(tokens[1]), int(tokens[2]), int(tokens[3]), int(tokens[5])))

sbots = sorted(bots, key=lambda x: x[3])
print sbots[0]
print sbots[-1]

def dist(x, y):
    return abs(x[0]-y[0]) + abs(x[1]-y[1]) + abs(x[2]-y[2])

strong = sbots[-1]
inrange = [bot for bot in bots if dist(strong, bot) <= strong[3]]

print 'Part one:', len(inrange)

def max_region(sbots, center, radius, dec):
    ibound = int(ceil(radius / dec))

OFFSETS = [[-1, -1, -1], [-1. 1, -1], [1, -1, -1], [1, 1, -1],
           [-1, -1, 1], [-1. 1, 1], [1, -1, 1], [1, 1, 1]]
