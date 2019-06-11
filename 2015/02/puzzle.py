#!/usr/bin/env python

f = open('input.txt', 'r')

total_sqft = 0
total_ribbon = 0
for line in f.readlines():
    if line:
        (l, w, h) = map(int, line.split('x'))
        (side1, side2, side3) = (2*l*w, 2*w*h, 2*h*l)
        slack = min((side1, side2, side3))/2

        total_sqft += side1 + side2 + side3 + slack

        ribbon = min((2*l + 2*w, 2*w + 2*h, 2*h + 2*l))
        bow = l*w*h

        total_ribbon += ribbon + bow

f.close()

print 'Total SQFT: %d' % total_sqft
print 'Total ribbon: %d' % total_ribbon

