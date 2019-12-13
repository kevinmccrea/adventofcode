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

(x,y) = map(int,data[0].split('-'))

def validate(password):
    password = str(password)
    prev = int(str(password)[0])
    prevprev = None
    double = False
    inc = True
    double2 = False
    for c in password[1:]:
        if int(c) == prev:
            double = True
            double2 = True
            if prevprev is not None:
                if prev != prevprev:
                    double2 = True
                else:
                    double2 = False
        
        if int(c) < prev:
            inc = False

        prevprev = prev
        prev = int(c)
        
    return double and inc, inc and double2

passwords1 = []
passwords2 = []

for p_int in xrange(x,y):
    (v1, v2)=validate(p_int)
    if v1:
        passwords1.append(p_int)
    if v2:
        passwords2.append(p_int)

print 'Part 1:', len(passwords1)
print 'Part 2:', len(passwords2)
