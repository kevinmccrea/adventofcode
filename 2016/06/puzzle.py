#!/usr/bin/env python

import sys
import operator

infilename = 'input.txt'
if len(sys.argv) > 2 and sys.argv[1] == '-i':
    infilename = sys.argv[2]

print 'Using input file: %s' % infilename

f = open(infilename, 'r')
data = f.readlines()
f.close()

counts = [{} for ii in xrange(8)]

for line in data:
    word = list(line.strip())
    for ii in xrange(len(word)):
        if counts[ii].has_key(word[ii]):
            counts[ii][word[ii]] += 1
        else:
            counts[ii][word[ii]] = 1

password = []
for ii in xrange(len(counts)):
    sorted_d = sorted(counts[ii].items(), key=operator.itemgetter(1), reverse=False)
    password.append(sorted_d[0][0])
    print password, ' ', sorted_d[0][1]

print ''.join(password)

