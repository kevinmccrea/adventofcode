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

def calc_line(prev):
    curr = prev[:]
    for ii in xrange(1, len(prev)-1):
        seq = prev[ii-1] + prev[ii] + prev[ii+1]
        if seq in ['^^.', '.^^', '^..', '..^']:
            curr[ii] = '^'
        else:
            curr[ii] = '.'
    return curr

prev = ['.'] + list(data[0]) + ['.']
count = prev[1:len(prev)-1].count('.')
iters = 1
while iters < 400000:
    curr = calc_line(prev)
    count += curr[1:len(prev)-1].count('.')
    
    #print ''.join(curr), count
    prev = curr
    iters += 1

    if iters == 40:
        print 'Part 1:', count

print 'Part 2:', count
