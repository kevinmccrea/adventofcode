#!/usr/bin/env python

import sys

infilename = 'input.txt'
if len(sys.argv) > 2 and sys.argv[1] == '-i':
    infilename = sys.argv[2]

print 'Using input file: %s' % infilename

f = open(infilename, 'r')
data = f.readlines()
f.close()

rotate = 312
#rotate = 3

cbuff = [0]
curr_index = 0
for ii in xrange(1,2017+1):
#for ii in xrange(1,10):
    curr_index = (curr_index + rotate) % len(cbuff) + 1
    cbuff.insert(curr_index, ii)
    
    if curr_index == 1:
        print ii

print cbuff, cbuff[curr_index]
print cbuff[curr_index-1], cbuff[curr_index], cbuff[curr_index+1]


cbuff = [0]
curr_index = 0
for ii in xrange(1,50000000+1):
    curr_index = (curr_index + rotate) % ii + 1

    if curr_index == 1:
        print ii

