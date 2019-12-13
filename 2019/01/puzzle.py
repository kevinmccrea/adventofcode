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



data = map(float, data)
mass = sum(data)
mass = int(mass/3) - 2


mass_sum = 0
for d in data:
    mass_sum += int(d/3) - 2
print 'Part 1:', mass_sum

def fuel(x):
    return int(x/3) - 2

mass_sum = 0
for d in data:
    f = fuel(d)
    while f > 0:
        mass_sum += f
        f = fuel(f)

print 'Part 2:', mass_sum
