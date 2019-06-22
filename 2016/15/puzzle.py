#!/usr/bin/env python

import sys

infilename = 'input.txt'
if len(sys.argv) > 2 and sys.argv[1] == '-i':
    infilename = sys.argv[2]

print 'Using input file: %s' % infilename

f = open(infilename, 'r')
data = f.readlines()
f.close()

slots = [5, 2]
pos = [4, 1]

slots = [13, 5, 17, 3, 7, 19, 11]
pos = [11, 0, 11, 0, 2, 17, 0]

time = 0

win_pos = [(slots[ii] + (slots[ii] - (ii + 1))) % slots[ii] for ii in xrange(len(slots))]

print win_pos

done = False
while not done:

    if pos == win_pos:
        done = True
    else:
        pos = [(pos[ii] + 1) % slots[ii] for ii in xrange(len(slots))]
        time += 1

print time

