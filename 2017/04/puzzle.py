#!/usr/bin/env python

import sys
import collections

infilename = 'input.txt'
if len(sys.argv) > 2 and sys.argv[1] == '-i':
    infilename = sys.argv[2]

print 'Using input file: %s' % infilename

f = open(infilename, 'r')
data = f.readlines()
f.close()

num_valid = 0
num_valid_ana = 0
for line in data:
    counts = collections.Counter()
    counts_ana = collections.Counter()

    for word in line.split():
        counts[word] += 1
    
        counts_ana[''.join(sorted(list(word)))] += 1

    if counts.most_common(1)[0][1] == 1:
        num_valid += 1

    if counts_ana.most_common(1)[0][1] == 1:
        num_valid_ana += 1

print num_valid
print num_valid_ana

