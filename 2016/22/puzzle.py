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

grid = {}
for line in data[2:]:
    x,y,size,used,avail,_ = aoc.tokenize(line, '/dev/grid/node-xyT')
    grid[(int(x),int(y))] = {'size':int(size), 'used':int(used), 'avail':int(avail)}

valid_pairs = []
node_map = {}
for a,b in itertools.permutations(grid.keys(), 2):
    if grid[a]['used'] > 0 and grid[a]['used'] <= grid[b]['avail']:
        valid_pairs.append((a,b))
        if a in node_map:
            node_map[a].append(b)
        else:
            node_map[a] = [b]

        if b in node_map:
            node_map[b].append(a)
        else:
            node_map[b] = [a]

print 'Part 1:', len(valid_pairs)

grid_maze = collections.defaultdict(lambda: '#')
for key in node_map.keys():
    grid_maze[key] = '.'

open_node = (35,18)
home_node = (0, 0)
data_node = (36, 0)

# steps to move the empty node into itial position (one less since we move into slot next to data)
steps_open_setup = len(aoc.astar_route(grid_maze, open_node, data_node, aoc.CARDINAL_DIRS, '#')) - 1

# steps to move data from data location to home
steps_data_move = len(aoc.astar_route(grid_maze, data_node, home_node, aoc.CARDINAL_DIRS, '#'))

print 'Part 2:', steps_open_setup + ((steps_data_move-1) * 5) + 1


