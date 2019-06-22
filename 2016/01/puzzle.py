#!/usr/bin/env python

import numpy

f = open('input.txt', 'r')
data = f.readlines()
f.close()

movements = [numpy.array([0,1]), numpy.array([1,0]), numpy.array([0,-1]), numpy.array([-1,0])]
curr_dir = 0

moves = [val.strip() for val in data[0].split(',')]

location = numpy.array([0,0])
visits = {}
visits[str(location)] = True

for move in moves:
    turn = move[0]
    steps = int(move[1:])

    if turn == 'R':
        curr_dir = (curr_dir + 1) % 4
    else:
        curr_dir = (curr_dir + 3) % 4

    for ii in xrange(steps):
        location += movements[curr_dir]

        if (visits.has_key(str(location))):
            print "HQ: %s    dist: %d" % (str(location), location[0]+location[1])

        visits[str(location)] = True

    #location += movements[curr_dir] * steps


print location
print location[0] + location[1]



