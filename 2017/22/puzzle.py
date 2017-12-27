#!/usr/bin/env python

import sys

infilename = 'input.txt'
if len(sys.argv) > 2 and sys.argv[1] == '-i':
    infilename = sys.argv[2]

print 'Using input file: %s' % infilename

f = open(infilename, 'r')
data = f.readlines()
f.close()

def cart_move(pos, offset):
    return (pos[0]+offset[0], pos[1]+offset[1])

def print_grid(grid):
    for rr in xrange(len(grid)):
        for cc in xrange(len(grid[rr])):
            print str(grid[rr][cc]),
        print ''

directions = [(0,1), (1,0), (0,-1), (-1,0)]

# init the grid
grid_size = 10001
grid_size = 11
grid = [[0 for x in xrange(grid_size)] for y in xrange(grid_size)]
pos_x = grid_size//2
pos_y = grid_size//2
curr_dir = 0

# load the input into the grid
in_rows = len(data)
in_cols = len(data[0].strip())
for rr in xrange(in_rows):
    for cc in xrange(in_cols):
        if data[rr][cc] == '#':
            grid[grid_size//2 - in_rows//2 + rr][grid_size//2 - in_cols//2 + cc] = 1

# infect!
num_infections = 0
num_cleans = 0
#for ii in xrange(10000):
for ii in xrange(7):
    print '################'
    print_grid(grid)
    if grid[pos_x][pos_y] == 1:
        grid[pos_x][pos_y] = 0
        turn = 1
        num_cleans += 1
    else:
        grid[pos_x][pos_y] = 1
        turn = -1
        num_infections += 1

    curr_dir = (curr_dir + turn) % len(directions)
    pos_x,pos_y = cart_move((pos_x,pos_y), directions[curr_dir])

print 'Part 1: num infections %d' % num_infections

