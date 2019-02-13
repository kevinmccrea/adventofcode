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

DEPTH = int(data[0].split()[1])
TARGET = tuple(map(int, data[1].split()[1].split(',')))

print 'Depth:', DEPTH, 'Target:', TARGET

board = {}

def get_node(board, row, col):
    if col == 0 and row == 0:
        geo = 0
    elif col == TARGET[1] and row == TARGET[0]:
        geo = 0
    elif col == 0:
        geo = row * 16807
    elif row == 0:
        geo = col * 48271
    else:
        g1, e1, t1 = board[(row-1, col)]
        g2, e2, t2 = board[(row, col-1)]
        geo = e1 * e2

    er = (geo + DEPTH) % 20183
    t = er % 3

    return (geo, er, t)

ROWS = TARGET[0]+1
COLS = TARGET[1]+1
#ROWS = DEPTH
#COLS = DEPTH * 5

for row in xrange(ROWS):
    for col in xrange(COLS):
        board[(row, col)] = get_node(board, row, col)

DIRS = ((-1,0), (0,-1), (0,1), (1, 0))

print 'Part 1:', sum(n for _,_,n in board.values())

class CaveGraph():
    def __init__(self, base_cave, rows, cols):
        # 0-empty  1-torch 2-climbin
        # .-rocky  =-wet   |-narrow
        self.tools_map = {'.': (1,2),        
                          '=': (0,2),
                          '|': (0,1)}

        self.graph = {}
        self.rows = rows
        self.cols = cols
        #self.graph = self.build_graph(base_cave, rows, cols)

    def build_graph(self, base_cave, rows, cols):
        # start cab move to any tool
        # end is a rocky region
        graph = {}
        for row in xrange(rows):
            for col in xrange(cols):
                tools = self.tools_map[base_cave[(row,col)]]

                # start node can use any tool
                if row == 0 and col == 0:
                    tools = (0,1,2)

                for tool in tools:
                    node = []

                    # add the neighbors with same tool
                    for dir in DIRS:
                        new_pos = aoc.tup_add((row, col), dir)
                        if new_pos[0] >= 0 and new_pos[0] < rows and new_pos[1] >= 0 and new_pos[1] < cols:
                            if tool in self.tools_map[base_cave[new_pos]]:
                                node.append(((new_pos[0], new_pos[1], tool), 1))

                    # add same node with different tools
                    for tt in tools:
                        if tt == tool:
                            continue
                        node.append(((row, col, tt), 7))

                    graph[(row,col,tool)] = tuple(node)

        return graph

    def compute_node(self, pos):
        row, col, tool = pos

        tools = self.tools_map[base_cave[(row,col)]]

        # start node can use any tool
        if row == 0 and col == 0:
            tools = (0,1,2)

        if tool not in tools:
            print 'ERROR'
            return ()

        node = []

        # add the neighbors with same tool
        for dir in DIRS:
            new_pos = aoc.tup_add((row, col), dir)
            if new_pos[0] >= 0 and new_pos[0] < self.rows and new_pos[1] >= 0 and new_pos[1] < self.cols:
                if tool in self.tools_map[base_cave[new_pos]]:
                    node.append(((new_pos[0], new_pos[1], tool), 1))

        # add same node with different tools
        for tt in tools:
            if tt == tool:
                continue
            node.append(((row, col, tt), 7))

        return tuple(node)
        
    def neighbors(self, pos):
        if not self.graph.has_key(pos):
            self.graph[pos] = self.compute_node(pos)
            
        return self.graph[pos]

#ROWS = TARGET[0]+1
#COLS = TARGET[1]+1
ROWS = TARGET[0] * 7
COLS = TARGET[1] * 7

print 'Building board...'
board = {}
for row in xrange(ROWS+1):
    for col in xrange(COLS+1):
        board[(row, col)] = get_node(board, row, col)

# start with torch
# end with torch
print 'Building terrain...'
base_cave = {}
terrain = '.=|'
for row in xrange(ROWS):
    for col in xrange(COLS):
        _,_,t_index = board[(row,col)]
        base_cave[(row, col)] = terrain[t_index]
board = None

start = (0,0,1)
end = (TARGET[0], TARGET[1], 1)

print 'Building graph...'
graph = CaveGraph(base_cave, ROWS, COLS)

print 'Finding path...'
prevs, costs = aoc.astar_graph(graph, start, end)

print 'Part 2:', costs[end]
