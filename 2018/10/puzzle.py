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

coords = []
vels = []

for line in data:
    tokens = line.replace('<', ' ').replace('>', ' ').replace(',', ' ').split()
    coords.append((int(tokens[1]), int(tokens[2])))
    vels.append((int(tokens[4]), int(tokens[5])))

def print_board(coords):
    x, y = zip(*coords)
    min_x = min(x)
    min_y = min(y)
    max_x = max(x)
    max_y = max(y)

    if max_x-min_x > 300 or max_y-min_y>100:
        print 'Nope'
        return

    board = [[' '] * (max_x - min_x+1) for xx in xrange(max_y - min_y+1)]
    print len(board)
    print len(board[0])
    for x,y in coords:
        print 'y', y-min_y, 'x', x-min_x
        board[y-min_y][x-min_x] = 'X'

    for row in board:
        print ''.join(row)

def get_height(coords):
    x,y=zip(*coords)
    return max(x)-min(x)

states = {0: list(coords)}
done = False
time = 1
prev_height = get_height(coords)
while not done:
    new_coords = [(coords[xx][0] + vels[xx][0], coords[xx][1] + vels[xx][1]) for xx in xrange(len(coords))]
    hh = get_height(new_coords)
    if (hh > prev_height):
        done = True
    else:
        states[time] = list(new_coords)
        coords = list(new_coords)
        prev_height = hh
        time += 1

print 'Time', time
print_board(coords)
    
