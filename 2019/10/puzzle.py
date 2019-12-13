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

asts = {}
for rr,cc in itertools.product(range(len(data)), range(len(data[0]))):
    if data[rr][cc] == '#':
        print (rr,cc)
        asts[(rr,cc)] = {}

import fractions

def add_neighbors(asts, target):
    neighbors = {}
    #print '####### Computing', target
    for a in asts.keys():
        if a == target:
            continue

        slope_r = target[0] - a[0]
        slope_c = target[1] - a[1]

        #print 'slope', slope_r, slope_c
        if slope_r != 0 and slope_c != 0:
            line_frac = fractions.Fraction(abs(slope_r), abs(slope_c))
            line_r = line_frac.numerator
            if slope_r < 0:
                line_r *= -1
            line_c = line_frac.denominator
            if slope_c < 0:
                line_c *= -1
        else:
            if slope_r == 0:
                line_c = slope_c / abs(slope_c)
                line_r = 0
            if slope_c == 0:
                line_r = slope_r / abs(slope_r)
                line_c = 0

        neigh = (line_r, line_c)
        #print 'neigh', neigh

        dist = aoc.mandist(target, a)

        if neigh in neighbors:
            # see if this node is closer than the one
            # there already
            n = neighbors[neigh]
            if dist < n[2]:
                #print n[0], ' blocked by ', a
                neighbors[neigh] = (a, neigh, dist)
            else:
                pass
                #print a, ' blocked by ', n[0]

        else:
            # add the node
            neighbors[neigh] = (a, neigh, dist)

    asts[target] = neighbors

max = 0
max_ast = None
for a in asts.keys():
    add_neighbors(asts, a)
    n = len(asts[a].keys())
    if n > max:
        max = n
        max_ast = a

for rr in range(len(data)):
    for cc in range(len(data[0])):
        if (rr,cc) in asts:
            print len(asts[(rr,cc)].keys()),
        else:
            print '.',
    print ''

print asts[max_ast]
print 'Part 1:', max, max_ast

def get_ast_list(asts, target):
    import copy
    import numpy
    new_asts = copy.deepcopy(asts)
    all_ordered = []
    add_neighbors(new_asts, target)
    while len(new_asts[target]):
        #print '######'
        #print new_asts.values()
        ordered = [(x[0], ((numpy.degrees(numpy.arctan2(-1* x[1][1], 1 * x[1][0])) + 360) % 360) ) for x in new_asts[target].values()]
        ordered.sort(key=lambda x: x[1])
        all_ordered += ordered[:]

        for x in ordered:
            del new_asts[x[0]]

        add_neighbors(new_asts, target)

    return all_ordered

print 'len', len(asts[max_ast])

all_ordered = get_ast_list(asts, max_ast)
for x in xrange(10):
    print all_ordered[x]
print 'Part 2:', all_ordered[199]

