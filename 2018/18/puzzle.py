#!/usr/bin/env python

import sys
import numpy
import collections

infilename = 'input.txt'
if len(sys.argv) > 2 and sys.argv[1] == '-i':
    infilename = sys.argv[2]

print 'Using input file: %s' % infilename

f = open(infilename, 'r')
data = f.readlines()
f.close()

data = [line.strip() for line in data]

board = numpy.zeros((50,50), numpy.int32)
syms = {'.':0, '|':1, '#':2}

for rr in xrange(len(data)):
    for cc in xrange(len(data[rr])):
        sym = data[rr][cc]
        board[rr][cc] = syms[sym]

def get_counts(board, row, col):
    c = collections.defaultdict(int)

    for rr in xrange(row-1, row+2):
        for cc in xrange(col-1, col+2):
            if rr >= 0 and rr < board.shape[0] and cc >= 0 and cc < board.shape[1]:
                char = board[rr][cc]
                if not (rr == row and cc == col):
                    c[char] += 1
    return c

def alter_board(board):
    new_board = numpy.array(board)

    for rr in xrange(len(board)):
        for cc in xrange(len(board[rr])):
            counts = get_counts(board, rr, cc)
            char = board[rr][cc]

            if char == 0:
                if counts[1] >= 3:
                    new_board[rr][cc] = 1
            if char == 1:
                if counts[2] >=3:
                    new_board[rr][cc] = 2
            if char == 2:
                if counts[2] >= 1 and counts[1] >= 1:
                    pass
                else:
                    new_board[rr][cc] = 0

    return new_board

def print_board(board):
    for rr in xrange(len(board)):
        line = ''
        for cc in xrange(len(board[rr])):
            char = board[rr][cc]
            if char == 1:
                line += '|'
            elif char == 2:
                line += '#'
            else:
                line += '.'
        print line

def to_string(x):
    return ''.join([str(ii) for ii in x.flatten()])

start_board = numpy.array(board)
print_board(board)
#for tic in xrange(10):
states = {}

#for tic in xrange(10):
#    board = alter_board(board)

key = to_string(board)
for tic in xrange(1000000000):
    if tic % 1000000 == 0:
        print tic
    if states.has_key(key):
        #print 'cycle', tic
        key, board, counts = states[key]
    else:
        board = alter_board(board)
        counts = collections.Counter(board.flatten())
        next_key = to_string(board)
        states[key] = (next_key, board, counts)

        key = next_key


    #print 'Round', tic
    #print_board(board)

counts = collections.Counter(board.flatten())
print '.', counts[0]
print '|', counts[1]
print '#', counts[2]

print 'Value', counts[1] * counts[2]

