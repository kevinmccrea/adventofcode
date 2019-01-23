#!/usr/bin/env python

import sys
import collections

infilename = 'input.txt'
if len(sys.argv) > 2 and sys.argv[1] == '-i':
    infilename = sys.argv[2]

print 'Using input file: %s' % infilename

f = open(infilename, 'r')
data = f.readlines()
f.close()

players = 9
top = 25

players = 10
top = 1618

players = 30
top = 5807

players = 427
top = 7072300

scores = [0] * players
ring = collections.deque()
ring.extend([0])
player = 1

for ii in xrange(1, top+1):
    if ii % 23 == 0:
        # special
        scores[player] += ii
        ring.rotate(7)
        marb = ring.popleft()
        scores[player] += marb

    else:
        ring.rotate(-2)
        ring.extendleft([ii])

    player = (player + 1) % players

print max(scores)
