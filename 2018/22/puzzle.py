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

DEPTH = int(data[0].split()[1])
TARGET = tuple(map(int, data[1].split()[1].split(',')))

print DEPTH, TARGET

board = {}

def get_node(board, x, y):
    if x == 0 and y == 0:
        geo = 0
    elif x == TARGET[0] and y == TARGET[1]:
        geo = 0
    elif y == 0:
        geo = x * 16807
    elif x == 0:
        geo = y * 48271
    else:
        g1, e1, t1 = board[(x-1, y)]
        g2, e2, t2 = board[(x, y-1)]
        geo = e1 * e2

    er = (geo + DEPTH) % 20183
    t = er % 3

    return (geo, er, t)

for yy in xrange(TARGET[1]+1):
    for xx in xrange(TARGET[0]+1):
        board[(xx, yy)] = get_node(board, xx, yy)


print board.items()[0]
print sum(n for _,_,n in board.values())

