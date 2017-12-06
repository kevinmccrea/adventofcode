#!/usr/bin/env python

import sys

infilename = 'input.txt'
if len(sys.argv) > 2 and sys.argv[1] == '-i':
    infilename = sys.argv[2]

print 'Using input file: %s' % infilename

f = open(infilename, 'r')
data = f.readlines()
f.close()

# part one
jumps = map(int, data)
addr = 0
steps = 0
while addr >= 0 and addr < len(jumps):
    offset = jumps[addr] 
    jumps[addr] += 1
    steps += 1

    addr += offset
print steps

# part two
jumps = map(int, data)
addr = 0
steps = 0
while addr >= 0 and addr < len(jumps):
    offset = jumps[addr] 
    if offset >= 3:
        jumps[addr] -= 1
    else:
        jumps[addr] += 1
    steps += 1

    addr += offset
print steps
