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

maze = aoc.create_maze(data)
stops = aoc.find_players(maze, background_chars='#.', replace_char='.')

DIRS = ((-1,0), (0, -1), (0, 1), (1,0))

def compute_full_route(graph, start, stops, order):
    total = 0
    path = '0'
    curr_index = 0
    curr_pos, cur_char = start
    while curr_index < len(order):
        next_pos, next_char = stops[order[curr_index]]
        total += graph[(cur_char, next_char)]
        
        path += next_char
        curr_index += 1
        cur_pos = next_pos
        cur_char = next_char

    return total, path

# build the graph of pairwise weights
graph = {}
for start, end in itertools.combinations(stops, 2):
    dist = len(aoc.astar_route(maze, start[0], end[0], DIRS, '#'))
    graph[(start[1], end[1])] = dist
    graph[(end[1], start[1])] = dist

# find and remove the starting position of '0' by sort and removing the first one
stops.sort(key=lambda t: int(t[1]))
start = stops.pop(0)


shortest_route = None
shortest_steps = 0
shortest_return_route = None
shortest_return_steps = 0
for order in itertools.permutations(range(len(stops))):
    total, path = compute_full_route(graph, start, stops, order)
    if shortest_route is None or total < shortest_steps:
        shortest_route = path
        shortest_steps = total

    return_total = total + graph[(path[-1], '0')]
    if shortest_return_route is None or return_total < shortest_return_steps:
        shortest_return_route = path + '0'
        shortest_return_steps = return_total

print 'Part 1:', shortest_steps, shortest_route
print 'Part 2:', shortest_return_steps, shortest_return_route
