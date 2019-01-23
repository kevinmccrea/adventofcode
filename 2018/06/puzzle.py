#!/usr/bin/env python

import sys
import numpy

infilename = 'input.txt'
if len(sys.argv) > 2 and sys.argv[1] == '-i':
    infilename = sys.argv[2]

print 'Using input file: %s' % infilename

f = open(infilename, 'r')
data = f.readlines()
f.close()

data = [ll.strip() for ll in data]


def dist(p1,p2):
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])
def print_board(board):
    for xx in xrange(BOARD_SIZE):
        for yy in xrange(BOARD_SIZE):
            id =  board[xx][yy]['id']
            if id == -1:
                print '.',
            else:
                print id,
        print ''


BOARD_SIZE = 15
BOARD_SIZE = 400

board = [[{} for b in xrange(BOARD_SIZE)] for bb in xrange(BOARD_SIZE)]
centers = []
for ii in xrange(len(data)):

    x,y = map(int, data[ii].split(','))

    centers.append((x,y))
    board[x][y]['id'] = ii
    board[x][y]['dist'] = 0
    board[x][y]['is_center'] = True


    if x > BOARD_SIZE or y > BOARD_SIZE:
        print 'TOO BIG:', x, y
        sys.exit()

counts = [0] * len(data)
infs = []
for xx in xrange(BOARD_SIZE):
    for yy in xrange(BOARD_SIZE):
        if board[xx][yy].has_key('id'):
            continue

        dists = [dist(centers[ii], (xx,yy)) for ii in xrange(len(centers))]
        min_d = min(dists)

        if dists.count(min_d) == 1:
            min_id = numpy.argmin(dists)
            board[xx][yy]['id'] = min_id
            board[xx][yy]['dist'] = min_d

            counts[min_id] += 1

            if xx in [0,BOARD_SIZE-1] or yy in [0, BOARD_SIZE-1]:
                infs.append(min_id)
        else:
            board[xx][yy]['id'] = -1
            board[xx][yy]['dist'] = min_d


s_count_ids = numpy.argsort(counts)
non_inf = [ii for ii in s_count_ids if ii not in set(infs)]
biggest_id = non_inf[-1]
#biggest_id = list(set(s_counts) - set(infs))[-1]

print counts
print s_count_ids
print non_inf
print set(infs)
print 'id: %d    size:  %d' % (biggest_id, counts[biggest_id]+1)

safe_size = 0
S = 400
Sh = S/2
for xx in xrange(S):
    for yy in xrange(S):
        offsets = [(x + Sh, y + Sh) for x,y in centers]
        dists = [dist(offsets[ii], (xx+Sh,yy+Sh)) for ii in xrange(len(offsets))]
        if sum(dists) < 10000:
            safe_size +=1

print safe_size
