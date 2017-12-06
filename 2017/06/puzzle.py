#!/usr/bin/env python

import numpy

f = open('input.txt', 'r')
data = f.readlines()
f.close()

banks = map(int, data[0].split())
history = []

#banks = [0,2,7,0]

done = False
iters = 0
while not done:
    max_ind = numpy.argmax(banks)
    max_val = banks[max_ind]

    banks[max_ind] = 0

    curr_index = (max_ind + 1) % len(banks)
    for ii in xrange(max_val):
        banks[curr_index] += 1
        curr_index = (curr_index + 1) % len(banks)

    iters += 1
    if tuple(banks) in history:
        done = True

    history.append(tuple(banks))
    

print iters
print len(history) - history.index(tuple(banks)) - 1
