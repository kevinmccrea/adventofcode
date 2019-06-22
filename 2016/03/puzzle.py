#!/usr/bin/env python

import sys
import itertools

infilename = 'input.txt'
if len(sys.argv) > 2 and sys.argv[1] == '-i':
    infilename = sys.argv[2]

print infilename

f = open(infilename, 'r')
data = f.readlines()
f.close()


num_valid = 0
for line in data:
    valid = True
    items = line.strip().split()
    for comb in itertools.permutations([int(num.strip()) for num in items], 3):
        if comb[0] >= comb[1] + comb[2]:
            valid = False
    
    if valid:
        num_valid += 1

print num_valid

triags = []
for ii in xrange(0,len(data),3):
    entries = [[] for yy in xrange(3)]
    for xx in xrange(3):
        line = data[ii+xx].strip().split()
        for yy in xrange(3):
            entries[yy].append(line[yy])

    triags.extend(entries)

num_valid2 = 0
for entry in triags:
    valid = True
    for comb in itertools.permutations([int(num) for num in entry], 3):
        if comb[0] >= comb[1] + comb[2]:
            valid = False

    if valid:
        num_valid2 += 1

print num_valid2

