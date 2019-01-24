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

def dist(s1, s2):
    diff = 0
    for ii in xrange(len(s1)):
        if s1[ii] != s2[ii]:
            diff += 1
    return diff

two = 0
three = 0
for line in data:
    two_found = False
    three_found = False
    cnt = collections.Counter()
    for cc in line.strip():
        cnt[cc] += 1
    for cc, num in cnt.items():
        if num == 2:
            two_found = True
        if num == 3:
            three_found = True
    if two_found:
        two+=1
    if three_found:
        three+=1

print two, three, two * three

for s1,s2 in itertools.combinations(data, 2):
    s1 = s1.strip()
    s2 = s2.strip()
    if dist(s1, s2) == 1:
        print 'ONE', s1, s2
        for ii in xrange(len(s1)):
            if s1[ii] == s2[ii]:
                sys.stdout.write(s1[ii])
    #if dist(s1, s2) == 3:
    #    print 'THREE', s1, s2
