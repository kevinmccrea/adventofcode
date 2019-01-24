#!/usr/bin/env python

import sys

infilename = 'input.txt'
if len(sys.argv) > 2 and sys.argv[1] == '-i':
    infilename = sys.argv[2]

print 'Using input file: %s' % infilename

f = open(infilename, 'r')
data = f.readlines()
f.close()


freq = 0
freqs = {}
freqs = []
for line in data:
    op = line[0]
    val = int(line[1:])

    if op == '+':
        freq += val
    elif op == '-':
        freq -= val

    if freq in freqs:
        print freq
        sys.exit()
    freqs.append(freq)

found = False
ii = 0
freq = 0
freqs = {}
while not found:
    line = data[ii]
    op = line[0]
    val = int(line[1:])

    if op == '+':
        freq += val
    elif op == '-':
        freq -= val

    if freq in freqs:
        print freq
        sys.exit()
    freqs[freq] = True

    ii = (ii + 1) % len(data)

#print freqs

print 'freq', freq
print 'first', first
