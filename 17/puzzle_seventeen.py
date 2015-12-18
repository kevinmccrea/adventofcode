#!/usr/bin/python

import itertools

f = open('input', 'r')
data = [int(str.strip()) for str in f.readlines()]
f.close()

count = 0

min_conts = len(data)
min_count = 0

for num_conts in xrange(1,len(data)-1):
    for comb in itertools.combinations(data, num_conts):
        if sum(comb) == 150:
            count += 1
            if (num_conts < min_conts):
                min_conts = num_conts
                min_count = 1
            elif num_conts == min_conts:
                min_count += 1

print 'Number of combinations: %d' % count
print 'Number of combinations at %d containers: %d' % (min_conts, min_count)

