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

def add_clay(board, line):
    single, mult = line.split(',')
    ends = mult.replace('=', ' ').replace('..', ' ').split()
    a = range(int(ends[1]), int(ends[2])+1)
    b = [int(single.split('=')[1])] * len(a)

    if single[0] == 'x':
        r = a
        c = b
    else:
        r = b
        c = a

    for rr, cc in zip(r, c):
        board[(rr,cc)] = '#'

def print_board(board, rows, cols):
    start_col = 500 - (cols/2)
    for rr in xrange(rows):
        line = ''
        for cc in xrange(start_col, start_col + cols+1):
            line += board[(rr,cc)]

        print line

#def can_grow(board, row, col):
#    if board[(row, col)] == '.'
#        surface = board[(row+1, col)]
#        if surface == '~' or surface == '#':
#            return True
#        elif surface == '.':
#            return False
#        else:
#            print 'FUCK', surface
#            sys.exit()

def grow(board, row, col, dir):
    layer = []
    done = False
    while not done:
        if board[(row, col+dir)] == '.' or board[(row,col+dir)] == '|':
            layer.append((row, col+dir))
            col += dir
            surface = board[(row+1, col)]
            if surface == '~' or surface == '#':
                pass
            elif surface == '.':
                done = True
            else:
                print 'FUCK', surface
                sys.exit()
        else:
            done = True
    return layer

def create_layer(board, row, start_col):
    layer = [(row, start_col)]

    layer += grow(board, row, start_col, -1)
    layer += grow(board, row, start_col, 1)

    return sorted(list(set(layer)))
        


def run_spring(board, spring):
    global TOP, BOTTOM
    new = []
    
    # drip down
    drips = []
    start_row, col = spring
    row = start_row+1
    done = False
    while not done:

        #if board[(row, col)] == '.' or board[(row, col)] == '|':
        if board[(row, col)] == '.':
            board[(row, col)] = '|'
            drips.append((row, col))
        else:
            surface = board[(row, col)]
            done = True

        if row > BOTTOM:
            return []

        row += 1

    # if surface is already a flow then quite
    if surface == '|':
        return []

    # flow on surface up drip stack until new flows formed
    while len(new) == 0 and drips:
        start_row, start_col = drips.pop(-1)
    
        layer = create_layer(board, start_row, start_col)

        r,c = layer[0]
        surface = board[(r+1, c)]
        if surface == '.' or surface == '|':
            new.append((r,c))

        r,c = layer[-1]
        surface = board[(r+1, c)]
        if surface == '.' or surface == '|':
            new.append((r,c))

        # draw the water as stable or flow
        if new:
            water = '|'
        else:
            water = '~'
        for w in layer:
            board[w] = water

    return new

board = collections.defaultdict(lambda:'.')

for line in data:
    add_clay(board, line)


TOP = sorted(board.keys())[0][0]
BOTTOM = sorted(board.keys())[-1][0]

print_board(board, 20,50)

print TOP, BOTTOM

def flow(board):
        
    new_springs = set([(0,500)])
    done_springs = set()
    while new_springs:
        spring = new_springs.pop()
        #print 'spring',spring
        if spring in done_springs:
            continue

        #print 'running'
        #new_springs.add(run_spring(board, spring))
        s = run_spring(board, spring)
        #print s
        #print new_springs
        for ss in s:
            new_springs.add(ss)
        done_springs.add(spring)


prev = None
done = False
while not done:

    for k,v in board.items():
        if v == '|':
            board[k]='.'

    flow(board)

    #counts = collections.Counter(board.values())
    counts = collections.Counter()
    for k,v in board.items():
        r,c = k
        if r >= TOP and r <= BOTTOM:
            counts[v] += 1
    if prev == counts:
        print prev, counts
        done = True

    prev = counts 

#print_board(board, BOTTOM+1,200)
print counts['~'] + counts['|']
