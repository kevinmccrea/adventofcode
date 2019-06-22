#!/usr/bin/env python

import sys

infilename = 'input.txt'
if len(sys.argv) > 2 and sys.argv[1] == '-i':
    infilename = sys.argv[2]

print 'Using input file: %s' % infilename

f = open(infilename, 'r')
data = f.readlines()
f.close()

#data = ['10000']
#target_len = 20

target_len = 272
target_len = 35651584
fill = [True if ch == '1' else False for ch in data[0].strip()]


while len(fill) < target_len:
    fill = fill + [False] + [not val for val in fill[::-1]]

done = False
checksum = fill[:target_len]
while not done:
    #print ''.join(['1' if checksum[ii] else '0' for ii in xrange(len(checksum))])

    checksum = [not(checksum[ii] ^ checksum[ii+1]) for ii in xrange(0,len(checksum), 2)]

    if len(checksum) % 2:
        done = True


print ''.join(['1' if checksum[ii] else '0' for ii in xrange(len(checksum))])
