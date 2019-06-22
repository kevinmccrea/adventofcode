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

filts = [(int(line.split('-')[0]), int(line.split('-')[1])) for line in data]
filts.sort(key=lambda t:t[0])

start = None
end = None

flat_filts = []

count = 0
while filts:
    curr_start, curr_end = filts.pop(0)

    if start == None:
        # no start to init
        start = curr_start
        end = curr_end

        if start > 0:
            count += start - 1
    else:
        if curr_start <= end + 1:
            # check if the current or new filt has a longer range
            end = max(end, curr_end)
        else:
            # new start is past the current end so cycle a new range
            flat_filts.append((start, end))

            count += curr_start - end - 1
            start = curr_start
            end = curr_end

flat_filts.append((start, end))

MAX_IP = 4294967295

if flat_filts[-1][1] < MAX_IP:
    count += MAX_IP - flat_filts[-1][1]

print 'Part 1:', flat_filts[0][1] + 1 
print 'Part 2:', count
