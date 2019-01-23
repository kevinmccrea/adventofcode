#!/usr/bin/env python

import sys
import collections
import itertools

infilename = 'input.txt'
if len(sys.argv) > 2 and sys.argv[1] == '-i':
    infilename = sys.argv[2]

print 'Using input file: %s' % infilename

f = open(infilename, 'r')
data = f.readlines()
f.close()

data = [line.strip() for line in data]
data = data[0]


def run_poly(poly):
    done = False
    input=list(poly[1:])
    result=[poly[0]]
    while not done:
        if not len(result):
            result.append(input.pop(0))

        left = result.pop()
        right = input.pop(0)

        if (left.upper() == right.upper()) and ((left.isupper() and right.islower()) or (left.islower() and right.isupper())):
                # destroy
                pass
        else:
            result.append(left)
            result.append(right)

        if len(input) == 0:
            done = True
    return len(result)

print run_poly(data)

min_val = 99999999999
min_char = None
for o in xrange(ord('A'), ord('Z')+1):
    fixed = list(data)

    p = chr(o)
    fixed = ''.join(fixed)
    fixed = fixed.replace(p,'').replace(p.lower(), '')
    fixed = list(fixed)
    print "Running with", p,
    l = run_poly(fixed)
    if l < min_val:
        print 'NEW',
        min_val = l
        min_char = p
    print l

print min_char, min_val
